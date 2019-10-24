# -*- coding: utf-8 -*-

"""
This module defines a set of SQLAlchemy ORM classes representing database tables
meant to store the XML records of the MedlinePlus dataset available under
https://medlineplus.gov/xml.html.

Exclusions:
- The `language` attribute of the `health-topic` element is excluded from the
`HealthTopic` class.
- The `language-mapped-topic` elements are excluded entirely.
- The `qualifier` element under the `mesh-heading` element is excluded entirely.
- The `other-language` elements are excluded entirely.
"""

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

    # Relationship to a list of `HealthTopic` records.
    health_topics = sqlalchemy.orm.relationship(
        argument="HealthTopic",
        secondary="medline.health_topic_also_calleds",
        back_populates="also_calleds",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicAlsoCalled` records.
    health_topic_also_calleds = sqlalchemy.orm.relationship(
        argument="HealthTopicAlsoCalled",
        back_populates="also_called",
        uselist=True,
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

    # Relationship to a list of `AlsoCalled` records.
    also_calleds = sqlalchemy.orm.relationship(
        argument="AlsoCalled",
        secondary="medline.health_topic_also_calleds",
        back_populates="health_topics",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicAlsoCalled` records.
    health_topic_also_calleds = sqlalchemy.orm.relationship(
        argument="HealthTopicAlsoCalled",
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


class HealthTopicAlsoCalled(Base, OrmFightForBase):
    """ Associative table between `HealthTopic` and `AlsoCalled` records."""

    # Set table name.
    __tablename__ = "health_topic_also_calleds"

    # Autoincrementing primary key ID.
    health_topic_also_called_id = sqlalchemy.Column(
        name="health_topic_also_called_id",
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

    # Foreign key to the also-called ID.
    also_called_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("medline.also_calleds.also_called_id"),
        name="also_called_id",
        nullable=False,
    )

    # Relationship to a `HealthTopic` record.
    health_topic = sqlalchemy.orm.relationship(
        argument="HealthTopic",
        back_populates="health_topic_also_calleds",
        uselist=False,
    )

    # Relationship to a `AlsoCalled` record.
    also_called = sqlalchemy.orm.relationship(
        argument="AlsoCalled",
        back_populates="health_topic_also_calleds",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("health_topic_id", "also_called_id"),
        # Set table schema.
        {"schema": "medline"},
    )


class HealthTopicDescriptor(Base, OrmFightForBase):
    """ Associative table between `HealthTopic` and `Descriptor` records."""

    # Set table name.
    __tablename__ = "health_topic_descriptors"

    # Autoincrementing primary key ID.
    health_topic_descriptor_id = sqlalchemy.Column(
        name="health_topic_descriptor_id",
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

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Relationship to a `HealthTopic` record.
    health_topic = sqlalchemy.orm.relationship(
        argument="HealthTopic",
        back_populates="health_topic_descriptors",
        uselist=False,
    )

    # Relationship to a `Descriptor` record.
    descriptor = sqlalchemy.orm.relationship(
        argument="Descriptor",
        back_populates="health_topic_descriptors",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("health_topic_id", "descriptor_id"),
        # Set table schema.
        {"schema": "medline"},
    )
