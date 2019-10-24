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

    # Relationship to a list of `HealthTopic` records.
    health_topics = sqlalchemy.orm.relationship(
        argument="HealthTopic",
        secondary="medline.health_topic_health_topic_groups",
        back_populates="health_topic_groups",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicHealthTopicGroup` records.
    health_topic_health_topic_groups = sqlalchemy.orm.relationship(
        argument="HealthTopicHealthTopicGroup",
        back_populates="health_topic_group",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "medline"
    }


class AlsoCalled(Base, OrmFightForBase):
    """ Table of `<also-called>` element records representing an alias of a
        health-topic.
    """

    # Set table name.
    __tablename__ = "also_calleds"

    # Autoincrementing primary key ID.
    also_called_id = sqlalchemy.Column(
        name="also_called_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<also-called>` element.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
        index=True,
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

    # Relationship to a list of `HealthTopicGroup` records.
    health_topic_groups = sqlalchemy.orm.relationship(
        argument="HealthTopicGroup",
        secondary="medline.health_topic_health_topic_groups",
        back_populates="health_topics",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicHealthTopicGroup` records.
    health_topic_health_topic_groups = sqlalchemy.orm.relationship(
        argument="HealthTopicHealthTopicGroup",
        back_populates="health_topic",
        uselist=True,
    )
    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "medline"
    }


class HealthTopicHealthTopicGroup(Base, OrmFightForBase):
    """ Associative table between `HealthTopic` and `HealthTopicGroup`
        records.
    """

    # Set table name.
    __tablename__ = "health_topic_health_topic_groups"

    # Autoincrementing primary key ID.
    health_topic_health_topic_group_id = sqlalchemy.Column(
        name="health_topic_health_topic_group_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the health-topic ID.
    health_topic_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("medline.health_topics.health_topic_id"),
        name="health_topic_id",
        nullable=False,
    )

    # Foreign key to the health-topic group ID.
    health_topic_group_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "medline.health_topic_groups.health_topic_group_id"
        ),
        name="health_topic_group_id",
        nullable=False,
    )

    # Relationship to a `HealthTopic` record.
    health_topic = sqlalchemy.orm.relationship(
        argument="HealthTopic",
        back_populates="health_topic_health_topic_groups",
        uselist=False,
    )

    # Relationship to a `HealthTopicGroup` record.
    health_topic_group = sqlalchemy.orm.relationship(
        argument="HealthTopicGroup",
        back_populates="health_topic_health_topic_groups",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("health_topic_id", "health_topic_group_id"),
        # Set table schema.
        {"schema": "medline"},
    )
