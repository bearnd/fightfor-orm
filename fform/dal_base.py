# coding: utf-8

""" Boilerplate SQLAlchemy to SQL-server interaction module.

This module contains the `DalBase` class which is meant to facilitate safe
interaction between SQLAlchemy and SQL-servers.
"""

import inspect
import contextlib
from typing import Dict, List, Any, Type, Union

import decorator
import sqlalchemy
import sqlalchemy.orm

from fform.orm_base import OrmBase
from fform.loggers import create_logger
from fform.excs import MissingAttributeError
from fform.excs import InvalidArgumentsError


def with_session_scope(**dec_kwargs):
    """Decorator factory, takes arguments accepted by the `session_scope` method
    of the `self` object of its wrapped function.

    This allows methods to declare that they want a session context, support a
    default way to make one, but still allow the caller to pass a preexisting
    session and control transaction scope.

    Note:
        Wrapped function must accept a defaultable `session` parameter, as well
        as a `self` parameter supporting the `sesson_scope` method.

        If call to wrapped function doesn't pass a session, will create a new
        session according to the args passed to the decorator factory.
        Otherwise, will leave session alone and become a noop.
    """

    @decorator.decorator
    def wrapper(target, *args, **kwargs):
        kwargs = inspect.getcallargs(target, *args, **kwargs)

        if "session" in kwargs and kwargs["session"]:
            return target(**kwargs)
        else:
            with kwargs["self"].session_scope(**dec_kwargs) as session:
                kwargs["session"] = session
                return target(**kwargs)

    return wrapper


class DalBase(object):
    """Basic Python boilerplate for interaction with an SQL database.

    Attributes:
        sql_user (str): SQL database username
        sql_password (str): SQL database password
        sql_host (str): SQL database hostname
        sql_port (str): SQL database port
        sql_dbname (str): SQL database name
        sql_url_template (str): SQL URL template containing the type of database
            and driver to be used for the connection.
    """

    def __init__(
        self,
        sql_username,
        sql_password,
        sql_host,
        sql_port,
        sql_db,
        sql_url_template=("postgresql+psycopg2://{username}:"
                          "{password}@{host}:{port}/{db}"),
        **kwargs
    ):
        """Initializes database connection and session"""

        # Internalize arguments.
        self.sql_username = sql_username
        self.sql_password = sql_password
        self.sql_host = sql_host
        self.sql_port = sql_port
        self.sql_db = sql_db
        self.sql_url_template = sql_url_template

        # Inspecting the presence of keyword arguments and (should they not be
        # defined) setting defaults.
        self.sql_engine_pool_size = kwargs.get("sql_engine_pool_size", 1)
        self.sql_engine_pool_recycle = kwargs.get(
            "sql_engine_pool_recycle", 3600
        )
        self.sql_engine_echo = kwargs.get("sql_engine_echo", False)
        self.expire_on_commit = kwargs.get("expire_on_commit", False)

        # create DB engine.
        self.engine = self.connect()

        # create new session.
        self.session_factory = sqlalchemy.orm.sessionmaker(
            bind=self.engine,
            expire_on_commit=self.expire_on_commit
        )

    def create_url(self):
        """Renders the database URL for the given template"""

        # Format the template strings with the user credentials and host
        # information provided upon instantiation.
        url = self.sql_url_template
        url = url.format(
            username=self.sql_username,
            password=self.sql_password,
            host=self.sql_host,
            port=self.sql_port,
            db=self.sql_db
        )

        return url

    def connect(self, url=None):
        """Connects to the database and returns the SQLAlchemy engine

        Args:
            url (str): The database URL.

        Returns:
            sqlalchemy.engine.base.Engine: The SQLAlchemy connection engine.
        """

        # If no URL was provided then create one through `self.create_url`.
        if not url:
            url = self.create_url()

        # Create the engine.
        engine = sqlalchemy.create_engine(
            url,
            pool_size=self.sql_engine_pool_size,
            pool_recycle=self.sql_engine_pool_recycle,
            echo=self.sql_engine_echo,
        )

        # Connect to the database.
        engine.connect()

        return engine

    @contextlib.contextmanager
    def session_scope(self, expunge_objects=True, refresh_objects=False):
        """Provide a transactional scope around a series of operations

        Args:
            expunge_objects (bool, optional): Mark objects as detached from this
                session. Objects can then be read after the session terminates.
                Defaults to `True`.
            refresh_objects (bool, optional): Explicitly re-query objects after
                committing session. Defaults to `False`.

        Note:
            If `expunge_objects` is set to `False` then any database record ORM
            object either retrieved through queries performed through this
            session or objects added through this session can no longer be
            accessed after the session is closed. Doing so will raise a
            `DetachedInstance` exception.

        Yields:
            sqlalchemy.orm.session.Session: A new session established through
                `self.engine`.
        """

        # Create a new session.
        session = self.session_factory()

        try:
            # Yield the session and allow the caller to perform DB work.
            yield session

            # At this point the context-manager has closed. The session is
            # flushed and committed thus persisting changes to the database.
            session.flush()
            session.commit()
        # In the event of an exception the session is rolled back and the
        # exception is raised.
        except Exception as exc:
            session.rollback()
            raise exc
        # Close the session.
        finally:
            if refresh_objects:
                for obj in session:
                    session.refresh(obj)
            if expunge_objects:
                session.expunge_all()

            session.close()


class DalFightForBase(DalBase):
    def __init__(
        self,
        sql_username,
        sql_password,
        sql_host,
        sql_port,
        sql_db,
        *args,
        **kwargs
    ):

        self.logger = create_logger(
            logger_name=type(self).__name__,
            logger_level=kwargs.get("logger_level", "DEBUG")
        )

        super(DalFightForBase, self).__init__(
            sql_username=sql_username,
            sql_password=sql_password,
            sql_host=sql_host,
            sql_port=sql_port,
            sql_db=sql_db,
            *args,
            **kwargs
        )

    @with_session_scope()
    def get(
        self,
        orm_class: Type[OrmBase],
        pk: int,
        session: sqlalchemy.orm.Session = None,
    ) -> Union[Type[OrmBase], None]:
        """Retrieves the record object of `orm_class` type through the value of
        its primary-key ID.

        Args:
            orm_class (Type[OrmBase]): An object of a class derived off
                `OrmBase` implementing the `attr_name` attribute.
            pk (int): The primary-key ID of the record to be retrieved.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be retrieved. Defaults to `None`
                in which case a new session is automatically created and
                terminated upon completion.

        Returns:
            Type[OrmBase]: The record object of type `orm_class` matching the
                primary-key ID and `None` if no record exists.
        """

        query = session.query(orm_class)
        query = query.filter(
            getattr(orm_class, orm_class.get_pk_name()) == pk
        )

        obj = query.one_or_none()

        return obj

    @with_session_scope()
    def delete(
        self,
        orm_class: Type[OrmBase],
        pk: int,
        session: sqlalchemy.orm.Session = None,
    ) -> None:
        """Deletes the underlying record corresponding to an object of
        `orm_class` type through its primary-key ID.

        Args:
            orm_class (Type[OrmBase]): A class derived off `OrmBase` which
                represents the record to be deleted.
            pk (int): The primary-key ID of the record to be deleted.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be deleted. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.
        """

        query = session.query(orm_class)
        query = query.filter(
            getattr(orm_class, orm_class.get_pk_name()) == pk
        )
        query.delete()

    @with_session_scope()
    def get_by_attr(
        self,
        orm_class: Type[OrmBase],
        attr_name: str,
        attr_value: Any,
        session: sqlalchemy.orm.Session = None,
    ) -> Union[Type[OrmBase], None]:
        """Retrieves the record object of `orm_class` type through the value of
        a given attribute.

        Note:
            This method should only be used through a unique attribute as it
            uses the `one_or_none` retrieval method and will raise an exception
            should multiple records with a given attribute value be found.

        Args:
            orm_class (Type[OrmBase]): An object of a class derived off
                `OrmBase` implementing the `attr_name` attribute.
            attr_name (str): The attribute name to be used in filtering out a
                single record.
            attr_value (Any): The attribute value to be used in filtering out a
                single record.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be retrieved. Defaults to `None`
                in which case a new session is automatically created and
                terminated upon completion.

        Returns:
            Type[OrmBase]: The record object of type `orm_class` matching the
                attribute value and `None` if no record exists.

        Raises:
            MissingAttributeError: Raised when the `orm_class` does not define
                the `attr_name` attribute.
            sqlalchemy.orm.exc.MultipleResultsFound: Raised when multiple
                records were found with the given attribute value.
        """

        # Log an error and raise an exception if the `orm_class` does not define
        # an `attr_name` attribute.
        if not hasattr(orm_class, attr_name):
            msg = "Class `{}` does not define attribute `{}`."
            msg_fmt = msg.format(orm_class, attr_name)
            self.logger.error(msg_fmt)
            raise MissingAttributeError(msg_fmt)

        query = session.query(orm_class)
        query = query.filter(getattr(orm_class, attr_name) == attr_value)

        obj = query.one_or_none()

        return obj

    @with_session_scope()
    def bget_by_attr(
        self,
        orm_class: Type[OrmBase],
        attr_name: str,
        attr_values: List[Any],
        do_sort: bool = True,
        session: sqlalchemy.orm.Session = None,
    ) -> List[Type[OrmBase]]:
        """Retrieves a list of record objects of `orm_class` type through the
        values of a given attribute.

        Args:
            orm_class (Type[OrmBase]): An object of a class derived off
                `OrmBase` implementing the `attr_name` attribute.
            attr_name (str): The attribute name to be used in filtering out the
                records.
            attr_values (list[Any]): The attribute values to be used in
                filtering out the record.
            do_sort (bool): Whether to sort the returned record objects by the
                same order the attribute values have. Only applied when the
                number of objects is the same as the number of attribute values.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the records will be retrieved . Defaults to `None`
                in which case a new session is automatically created and
                terminated upon completion.

        Returns:
            List[Type[OrmBase]]: The record objects of type `orm_class`
                matching the attribute values.

        Raises:
            MissingAttributeError: Raised when the `orm_class` does not define
                the `attr_name` attribute.
        """

        # Log an error and raise an exception if the `orm_class` does not define
        # an `attr_name` attribute.
        if not hasattr(orm_class, attr_name):
            msg = "Class `{}` does not define attribute `{}`."
            msg_fmt = msg.format(orm_class, attr_name)
            self.logger.error(msg_fmt)
            raise MissingAttributeError(msg_fmt)

        query = session.query(orm_class)
        query = query.filter(getattr(orm_class, attr_name).in_(attr_values))

        objs = query.all()

        # If sorting has been requested and the number of objects matches the
        # number of attribute values, i.e., a record object was found for each
        # combination of attribute values, then do the sorting.
        if do_sort and len(objs) == len(list(attr_values)[0]):
            objs = self.order_objs_by_attr(
                objs=objs,
                attr_name=attr_name,
                attr_values=attr_values,
            )

        return objs

    @with_session_scope()
    def get_by_attrs(
        self,
        orm_class: Type[OrmBase],
        attrs_names_values: Dict[str, Any],
        session: sqlalchemy.orm.Session = None,
    ) -> Union[Type[OrmBase], None]:
        """Retrieves the record object of `orm_class` type through attribute
        name-value pairs.

        Note:
            This method should only be used through unique attributes/fields as
            it uses the `one_or_none` retrieval method and will raise an
            exception should multiple records with a given attribute value be
            found.

        Args:
            orm_class (Type[OrmBase]): An object of a class derived off
                `OrmBase` implementing the defined attributes.
            attrs_names_values (Dict[str, Any]): A dictionary of attribute
                name:value pairs to be used in filtering out a single record.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be retrieved. Defaults to `None`
                in which case a new session is automatically created and
                terminated upon completion.

        Returns:
            Type[OrmBase]: The record object of type `orm_class` matching the
                attribute name-value pairs and `None` if no record exists.

        Raises:
            MissingAttributeError: Raised when the `orm_class` does not define
                any of the the `attrs_names_values` attributes (keys).
            sqlalchemy.orm.exc.MultipleResultsFound: Raised when multiple
                records were found with the given attribute(s).
        """

        # Log an error and raise an exception if the `orm_class` does not define
        # any of the `attrs_names_values` attributes (keys).
        for attr_name in attrs_names_values.keys():
            if not hasattr(orm_class, attr_name):
                msg = "Class `{}` does not define attribute `{}`."
                msg_fmt = msg.format(orm_class, attr_name)
                self.logger.error(msg_fmt)
                raise MissingAttributeError(msg_fmt)

        query = session.query(orm_class)
        for attr_name, attr_value in attrs_names_values.items():
            query = query.filter(
                getattr(orm_class, attr_name) == attr_value
            )

        obj = query.one_or_none()

        return obj

    @with_session_scope()
    def bget_by_attrs(
        self,
        orm_class: Type[OrmBase],
        attrs_names_values: Dict[str, List[Any]],
        session: sqlalchemy.orm.Session = None,
    ) -> List[Type[OrmBase]]:
        """Retrieves a list of record objects of `orm_class` type through
        attribute name-value pairs.

        Args:
            orm_class (Type[OrmBase]): An object of a class derived off
                `OrmBase` implementing the `attr_name` attribute.
            attrs_names_values (Dict[str, List[Any]]): A dictionary of attribute
                name:list of values pairs to be used in filtering out the
                records.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the records will be retrieved. Defaults to `None`
                in which case a new session is automatically created and
                terminated upon completion.

        Returns:
            List[Type[OrmBase]]: The record objects of type `orm_class`
                matching the attribute values.

        Raises:
            MissingAttributeError: Raised when the `orm_class` does not define
                any of the the `attrs_names_values` attributes (keys).
            InvalidArgumentsError: Raised when the lists of values under the
                attrs_names_values dictionary are not of the same length.
        """

        # Retrieve all attribute names.
        attr_names = attrs_names_values.keys()

        # Log an error and raise an exception if the `orm_class` does not define
        # any of the `attrs_names_values` attributes (keys).
        for attr_name in attr_names:
            if not hasattr(orm_class, attr_name):
                msg = "Class `{}` does not define attribute `{}`."
                msg_fmt = msg.format(orm_class, attr_name)
                self.logger.error(msg_fmt)
                raise MissingAttributeError(msg_fmt)

        # Retrieve all attribute value lists.
        attr_values = attrs_names_values.values()

        # Log an error and raise an exception if the list of values are not all
        # of equal length.
        if len(set(map(len, attr_values))) != 1:
            msg_fmt = "The value lists must all be of equal length."
            self.logger.error(msg_fmt)
            raise InvalidArgumentsError(msg_fmt)

        # Retrieve all attributes from the class.
        attrs = [getattr(orm_class, attr_name) for attr_name in attr_names]

        query = session.query(orm_class)
        query = query.filter(sqlalchemy.tuple_(*attrs).in_(zip(*attr_values)))

        objs = query.all()

        return objs

    def order_objs_by_attr(
        self,
        objs: List[Type[OrmBase]],
        attr_name: str,
        attr_values: List[Any]
    ) -> List[Type[OrmBase]]:
        """Matches a list of record objects of a class derived off `OrmBase`
        through a given attribute against a list of attribute values.

        Args:
            objs (List[Type[OrmBase]]): The list of record objects of a class
                derived off `OrmBase` that define the `attr_name` attribute.
            attr_name (str): The attribute to perform the matching against.
            attr_values (List[Any]): The values of the `attr_name` attribute
                through which the matching will be performed.

        Returns:
            List[Type[OrmBase]]: The record objects in order matching the
                attribute values.

        Raises:
            MissingAttributeError: Raised when the `orm_class` does not define
                any of the the `attrs_names_values` attributes (keys).
            InvalidArgumentsError: Raised when the lists of values under the
                attrs_names_values dictionary are not of the same length.
        """

        # Log an error and raise an exception if any of the `objs` do not define
        # the `attr_name` attribute.
        for obj in objs:
            if not hasattr(obj, attr_name):
                msg = "Class `{}` does not define attribute `{}`."
                msg_fmt = msg.format(obj.__class__, attr_name)
                self.logger.error(msg_fmt)
                raise MissingAttributeError(msg_fmt)

        # Log an error and raise an exception if the `objs` and `attr_values`
        # lists are not of equal length.
        if len(objs) != len(attr_values):
            msg_fmt = ("The `objs` and `attr_values` lists must be of equal "
                       "length.")
            self.logger.error(msg_fmt)
            raise InvalidArgumentsError(msg_fmt)

        # Iterate over the `objs` and `attr_values` and match them creating a
        # list of record objects in the order of the attribute values.
        objs_ordered = []
        for attr_value in attr_values:
            for obj in objs:
                if getattr(obj, attr_name) == attr_value:
                    objs_ordered.append(obj)
                    continue

        return objs_ordered
