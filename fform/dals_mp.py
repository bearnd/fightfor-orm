# -*- coding: utf-8 -*-

import datetime

import sqlalchemy.orm
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.dialects.postgresql import Insert
from sqlalchemy.engine.result import ResultProxy

from fform.dal_base import DalFightForBase
from fform.dal_base import with_session_scope
from fform.orm_mp import HealthTopicGroupClass
from fform.orm_mp import HealthTopicGroup
from fform.orm_mp import BodyPart
from fform.orm_mp import AlsoCalled
from fform.orm_mp import PrimaryInstitute
from fform.orm_mp import SeeReference
from fform.orm_mp import HealthTopicHealthTopicGroup
from fform.orm_mp import HealthTopicAlsoCalled
from fform.orm_mp import HealthTopicDescriptor
from fform.orm_mp import HealthTopicRelatedHealthTopic
from fform.orm_mp import HealthTopicSeeReference
from fform.orm_mp import HealthTopicBodyPart
from fform.orm_mp import HealthTopic
from fform.utils import return_first_item


class DalMedline(DalFightForBase):
    def __init__(
        self,
        sql_username,
        sql_password,
        sql_host,
        sql_port,
        sql_db,
        *args,
        **kwargs,
    ):

        super(DalMedline, self).__init__(
            sql_username=sql_username,
            sql_password=sql_password,
            sql_host=sql_host,
            sql_port=sql_port,
            sql_db=sql_db,
            *args,
            **kwargs,
        )

    @return_first_item
    @with_session_scope()
    def iodi_health_topic_group_class(
        self, name: str, session: sqlalchemy.orm.Session = None
    ) -> int:
        """ Creates a new `HealthTopicGroupClass` record in an IODI manner.

        Args:
            name (str): The health-topic group class name.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `HealthTopicGroupClass` record.
        """

        self.logger.info(f"IODIing `HealthTopicGroupClass` record.")

        # Upsert the `HealthTopicGroupClass` record.
        statement = insert(
            HealthTopicGroupClass, values={"name": name}
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            # noinspection PyTypeChecker
            obj = self.get_by_attr(
                orm_class=HealthTopicGroupClass,
                attr_name="name",
                attr_value=name,
                session=session,
            )  # type: HealthTopicGroupClass
            return obj.health_topic_group_class_id

    @return_first_item
    @with_session_scope()
    def iodu_health_topic_group(
        self,
        ui: str,
        name: str,
        url: str,
        session: sqlalchemy.orm.Session = None,
    ) -> int:
        """ Creates a new `HealthTopicGroup` record in an IODU manner.

        Args:
            ui (str): The health-topic group UI.
            name (str): The health-topic group name.
            url (str): The health-topic group URL.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `HealthTopicGroup` record.
        """

        self.logger.info(f"IODUing `HealthTopicGroup` record.")

        # Upsert the `HealthTopicGroup` record.
        statement = insert(
            HealthTopicGroup, values={"ui": ui, "name": name, "url": url}
        ).on_conflict_do_update(
            index_elements=["ui"], set_={"url": url}
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_body_part(
        self, name: str, session: sqlalchemy.orm.Session = None
    ) -> int:
        """ Creates a new `BodyPart` record in an IODI manner.

        Args:
            name (str): The body-part name.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `BodyPart` record.
        """

        self.logger.info(f"IODIing `BodyPart` record.")

        # Upsert the `BodyPart` record.
        statement = insert(
            BodyPart, values={"name": name}
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            # noinspection PyTypeChecker
            obj = self.get_by_attr(
                orm_class=BodyPart,
                attr_name="name",
                attr_value=name,
                session=session,
            )  # type: BodyPart
            return obj.body_part_id

    @return_first_item
    @with_session_scope()
    def iodi_also_called(
        self, name: str, session: sqlalchemy.orm.Session = None
    ) -> int:
        """ Creates a new `AlsoCalled` record in an IODI manner.

        Args:
            name (str): The also-called name.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `AlsoCalled` record.
        """

        self.logger.info(f"IODIing `AlsoCalled` record.")

        # Upsert the `AlsoCalled` record.
        statement = insert(
            AlsoCalled, values={"name": name}
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            # noinspection PyTypeChecker
            obj = self.get_by_attr(
                orm_class=AlsoCalled,
                attr_name="name",
                attr_value=name,
                session=session,
            )  # type: AlsoCalled
            return obj.also_called_id

    @return_first_item
    @with_session_scope()
    def iodu_primary_institute(
        self, name: str, url: str, session: sqlalchemy.orm.Session = None
    ) -> int:
        """ Creates a new `PrimaryInstitute` record in an IODU manner.

        Args:
            name (str): The primary-institute group name.
            url (str): The primary-institute group URL.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `PrimaryInstitute` record.
        """

        self.logger.info(f"IODUing `PrimaryInstitute` record.")

        # Upsert the `PrimaryInstitute` record.
        statement = insert(
            PrimaryInstitute, values={"name": name, "url": url}
        ).on_conflict_do_update(
            index_elements=["name"], set_={"url": url}
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_see_reference(
        self, name: str, session: sqlalchemy.orm.Session = None
    ) -> int:
        """ Creates a new `SeeReference` record in an IODI manner.

        Args:
            name (str): The see-reference name.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `SeeReference` record.
        """

        self.logger.info(f"IODIing `SeeReference` record.")

        # Upsert the `SeeReference` record.
        statement = insert(
            SeeReference, values={"name": name}
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            # noinspection PyTypeChecker
            obj = self.get_by_attr(
                orm_class=SeeReference,
                attr_name="name",
                attr_value=name,
                session=session,
            )  # type: SeeReference
            return obj.see_reference_id

    @return_first_item
    @with_session_scope()
    def iodi_health_topic_health_topic_group(
        self,
        health_topic_id: int,
        health_topic_group_id: int,
        session: sqlalchemy.orm.Session = None,
    ) -> int:
        """ Creates a new `HealthTopicHealthTopicGroup` record in an IODI
            manner.

        Args:
            health_topic_id (int): The linked `HealthTopic` record primary-key
                ID.
            health_topic_group_id (int): The linked `HealthTopicGroup` record
                primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `HealthTopicHealthTopicGroup` record.
        """

        self.logger.info(f"IODIing `HealthTopicHealthTopicGroup` record.")

        # Upsert the `HealthTopicHealthTopicGroup` record.
        statement = insert(
            HealthTopicHealthTopicGroup,
            values={
                "health_topic_id": health_topic_id,
                "health_topic_group_id": health_topic_group_id,
            },
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            # noinspection PyTypeChecker
            obj = self.get_by_attrs(
                orm_class=HealthTopicHealthTopicGroup,
                attrs_names_values={
                    "health_topic_id": health_topic_id,
                    "health_topic_group_id": health_topic_group_id,
                },
                session=session,
            )  # type: HealthTopicHealthTopicGroup
            return obj.health_topic_health_topic_group_id

    @return_first_item
    @with_session_scope()
    def iodi_health_topic_also_called(
        self,
        health_topic_id: int,
        also_called_id: int,
        session: sqlalchemy.orm.Session = None,
    ) -> int:
        """ Creates a new `HealthTopicAlsoCalled` record in an IODI manner.

        Args:
            health_topic_id (int): The linked `HealthTopic` record primary-key
                ID.
            also_called_id (int): The linked `AlsoCalled` record
                primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `HealthTopicAlsoCalled` record.
        """

        self.logger.info(f"IODIing `HealthTopicAlsoCalled` record.")

        # Upsert the `HealthTopicAlsoCalled` record.
        statement = insert(
            HealthTopicAlsoCalled,
            values={
                "health_topic_id": health_topic_id,
                "also_called_id": also_called_id,
            },
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            # noinspection PyTypeChecker
            obj = self.get_by_attrs(
                orm_class=HealthTopicAlsoCalled,
                attrs_names_values={
                    "health_topic_id": health_topic_id,
                    "also_called_id": also_called_id,
                },
                session=session,
            )  # type: HealthTopicAlsoCalled
            return obj.health_topic_also_called_id
