# -*- coding: utf-8 -*-

import sqlalchemy.orm

from fform.orm_base import Base
from fform.orm_base import OrmFightForBase


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
        name="url", type_=sqlalchemy.types.UnicodeText(), nullable=False
    )
    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "medline"
    }
class HealthTopic(Base, OrmFightForBase):
    """ Table of `<health-topic>` element records representing a
        health-topic.
    """

    # Set table name.
    __tablename__ = "health_topics"

    # Autoincrementing primary key ID.
    health_topic_id = sqlalchemy.Column(
        name="health_topic_id",
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

    # Referring to the `title` attribute.
    title = sqlalchemy.Column(
        name="title",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
        index=True,
    )

    # Referring to the `url` attribute.
    url = sqlalchemy.Column(
        name="url", type_=sqlalchemy.types.UnicodeText(), nullable=False
    )

    # Referring to the `meta-desc` attribute.
    description = sqlalchemy.Column(
        name="description", type_=sqlalchemy.types.UnicodeText(), nullable=False
    )

    # Referring to the `<full-summary>` element.
    summary = sqlalchemy.Column(
        name="summary", type_=sqlalchemy.types.UnicodeText(), nullable=True
    )

    date_created = sqlalchemy.Column(
        name="date_created", type_=sqlalchemy.types.Date(), nullable=False
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "medline"
    }
