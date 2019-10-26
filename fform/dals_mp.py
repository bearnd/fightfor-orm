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
