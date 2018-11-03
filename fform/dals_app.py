# coding: utf-8

import sqlalchemy.orm
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.dialects.postgresql import Insert
from sqlalchemy.engine.result import ResultProxy

from fform.dal_base import DalFightForBase
from fform.dal_base import with_session_scope
from fform.orm_ct import GenderType
from fform.orm_app import User
from fform.orm_app import Search
from fform.orm_app import SearchDescriptor
from fform.orm_app import UserSearch
from fform.utils import return_first_item


class DalApp(DalFightForBase):
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

        super(DalApp, self).__init__(
            sql_username=sql_username,
            sql_password=sql_password,
            sql_host=sql_host,
            sql_port=sql_port,
            sql_db=sql_db,
            *args,
            **kwargs
        )

    @return_first_item
    @with_session_scope()
    def iodi_user(
        self,
        auth0_user_id: str,
        email: str,
        session: sqlalchemy.orm.Session = None,
    ) -> int:
        """ Creates a new `User` record in an IODI manner.

        Args:
            auth0_user_id (str): The Auth0 user ID.
            email (str): The user email.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `User` record.
        """

        # Upsert the `User` record.
        statement = insert(
            User,
            values={
                "auth0_user_id": auth0_user_id,
                "email": email,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=User,
                attrs_names_values={
                    "auth0_user_id": auth0_user_id,
                },
                session=session,
            )  # type: User
            return obj.user_id

    @return_first_item
    @with_session_scope()
    def iodu_search(
        self,
        search_uuid: str,
        title: str,
        gender: GenderType,
        year_beg: int,
        year_end: int,
        age_beg: int,
        age_end: int,
        session: sqlalchemy.orm.Session = None,
    ) -> int:
        """Creates a new `Search` record in an IODU manner.

        Args:
            search_uuid (str): The search UUID.
            title (str): The search title.
            gender (GenderType): The search title.
            year_beg (int): The beginning of the year-range studies will be
                limited to for this search.
            year_end (int): The end of the year-range studies will be  limited
                to for this search.
            age_beg (int): The beginning of the age-range studies will be
                limited to for this search.
            age_end (int): The end of the age-range studies will be  limited to
                for this search.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Search` record.
        """

        # Upsert the `Search` record.
        statement = insert(
            Search,
            values={
                "search_uuid": search_uuid,
                "title": title,
                "gender": gender,
                "year_beg": year_beg,
                "year_end": year_end,
                "age_beg": age_beg,
                "age_end": age_end,
            }
        ).on_conflict_do_update(
            index_elements=["search_uuid"],
            set_={
                "title": title,
                "gender": gender,
                "year_beg": year_beg,
                "year_end": year_end,
                "age_beg": age_beg,
                "age_end": age_end,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=Search,
                attrs_names_values={
                    "search_uuid": search_uuid,
                },
                session=session,
            )  # type: Search
            return obj.search_id

    @return_first_item
    @with_session_scope()
    def iodi_user_search(
        self,
        user_id: int,
        search_id: int,
        session: sqlalchemy.orm.Session = None,
    ) -> int:
        """ Creates a new `UserSearch` record in an IODI manner.

        Args:
            user_id (int): The linked `User` record primary-key ID.
            search_id (int): The linked `Search` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `UserSearch` record.
        """

        statement = insert(
            UserSearch,
            values={
                "user_id": user_id,
                "search_id": search_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=UserSearch,
                attrs_names_values={
                    "user_id": user_id,
                    "search_id": search_id,
                },
                session=session,
            )  # type: UserSearch
            return obj.user_search_id

    @return_first_item
    @with_session_scope()
    def iodi_search_descriptor(
        self,
        search_id: int,
        descriptor_id: int,
        session: sqlalchemy.orm.Session = None,
    ) -> int:
        """ Creates a new `SearchDescriptor` record in an IODI manner.

        Args:
            search_id (int): The linked `Search` record primary-key ID.
            descriptor_id (int): The linked `Descriptor` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `SearchDescriptor` record.
        """

        statement = insert(
            SearchDescriptor,
            values={
                "search_id": search_id,
                "descriptor_id": descriptor_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=SearchDescriptor,
                attrs_names_values={
                    "search_id": search_id,
                    "descriptor_id": descriptor_id,
                },
                session=session,
            )  # type: SearchDescriptor
            return obj.search_descriptor_id
