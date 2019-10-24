# -*- coding: utf-8 -*-

import sqlalchemy.orm

from fform.orm_base import Base
from fform.orm_base import OrmFightForBase
from fform.utils import EnumBase


class HealthTopicGroup(Base, OrmFightForBase):
    """ Table of `<group>` element records representing a health-topic group."""

    # Set table name.
    __tablename__ = "health_topic_groups"

    # Autoincrementing primary key ID.
    health_topic_group_id = sqlalchemy.Column(
        name="health_topic_group_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `id` attribute.
    ui = sqlalchemy.Column(
        name="ui",
        type_=sqlalchemy.types.Integer(),
        nullable=False,
        unique=True,
        index=True,
    )

    # Referring to the value of the `<group>` element.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
        index=True,
    )

    # Referring to the `url` attribute.
    url = sqlalchemy.Column(
        name="url",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )
