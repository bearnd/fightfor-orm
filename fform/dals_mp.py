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

