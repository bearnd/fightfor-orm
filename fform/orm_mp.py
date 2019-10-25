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
- The `site` elements are excluded entirely.
"""

import sqlalchemy.orm

from fform.orm_base import Base
from fform.orm_base import OrmFightForBase


class HealthTopicGroupClass(Base, OrmFightForBase):
    """ Table of MedlinePlus health-topic group classes."""

    # Set table name.
    __tablename__ = "health_topic_group_classes"

    # Autoincrementing primary key ID.
    health_topic_group_class_id = sqlalchemy.Column(
        name="health_topic_group_class_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the name of the health-topic group class.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
        index=True,
    )

    # Relationship to a list of `HealthTopicGroup` records.
    health_topic_groups = sqlalchemy.orm.relationship(
        argument="HealthTopicGroup",
        back_populates="health_topic_group_class",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "medline"
    }


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

    # Foreign key to the health-topic group class ID.
    health_topic_group_class_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "medline.health_topic_group_classes.health_topic_group_class_id"
        ),
        name="health_topic_group_class_id",
        nullable=False,
    )

    # Relationship to a `HealthTopicGroupClass` record.
    health_topic_group_class = sqlalchemy.orm.relationship(
        argument="HealthTopicGroupClass",
        back_populates="health_topic_groups",
        uselist=False,
    )

    # Relationship to a list of `BodyPart` records.
    body_parts = sqlalchemy.orm.relationship(
        argument="BodyPart",
        back_populates="health_topic_group",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "medline"
    }


class BodyPart(Base, OrmFightForBase):
    """ Table of MedlinePlus health-topic related body-parts."""

    # Set table name.
    __tablename__ = "body_parts"

    # Autoincrementing primary key ID.
    body_part_id = sqlalchemy.Column(
        name="body_part_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the name of the body part.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
        index=True,
    )

    # Foreign key to the health-topic group ID.
    health_topic_group_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "medline.health_topic_groups.health_topic_group_id"
        ),
        name="health_topic_group_id",
        nullable=False,
    )

    # Relationship to a `HealthTopicGroup` record.
    health_topic_group = sqlalchemy.orm.relationship(
        argument="HealthTopicGroup",
        back_populates="body_parts",
        uselist=False,
    )

    # Relationship to a list of `HealthTopic` records.
    health_topics = sqlalchemy.orm.relationship(
        argument="HealthTopic",
        secondary="medline.health_topic_body_parts",
        back_populates="body_parts",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicBodyPart` records.
    health_topic_body_parts = sqlalchemy.orm.relationship(
        argument="HealthTopicBodyPart",
        back_populates="body_part",
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


class PrimaryInstitute(Base, OrmFightForBase):
    """ Table of `<primary-institute>` element records representing a
        primary-institute.
    """

    # Set table name.
    __tablename__ = "primary_institutes"

    # Autoincrementing primary key ID.
    primary_institute_id = sqlalchemy.Column(
        name="primary_institute_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
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
        argument="HealthTopic", back_populates="primary_institute", uselist=True
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "medline"
    }


class SeeReference(Base, OrmFightForBase):
    """ Table of `<see-reference>` element records representing a reference to a
        health-topic.
    """

    # Set table name.
    __tablename__ = "see_references"

    # Autoincrementing primary key ID.
    see_reference_id = sqlalchemy.Column(
        name="see_reference_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<see-reference>` element.
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
        secondary="medline.health_topic_see_references",
        back_populates="see_references",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicSeeReference` records.
    health_topic_see_references = sqlalchemy.orm.relationship(
        argument="HealthTopicSeeReference",
        back_populates="see_reference",
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


class HealthTopicRelatedHealthTopic(Base, OrmFightForBase):
    """ Associative table between `HealthTopic` and other `HealthTopic`
        records.
    """

    # Set table name.
    __tablename__ = "health_topic_related_health_topics"

    # Autoincrementing primary key ID.
    health_topic_related_health_topic_id = sqlalchemy.Column(
        name="health_topic_related_health_topic_id",
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

    # Foreign key to the related health-topic ID.
    related_health_topic_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("medline.health_topics.health_topic_id"),
        name="related_health_topic_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint(
            "health_topic_id", "related_health_topic_id"
        ),
        # Set table schema.
        {"schema": "medline"},
    )


class HealthTopicSeeReference(Base, OrmFightForBase):
    """ Associative table between `HealthTopic` and `SeeReference` records."""

    # Set table name.
    __tablename__ = "health_topic_see_references"

    # Autoincrementing primary key ID.
    health_topic_see_reference_id = sqlalchemy.Column(
        name="health_topic_see_reference_id",
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

    # Foreign key to the see-reference ID.
    see_reference_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("medline.see_references.see_reference_id"),
        name="see_reference_id",
        nullable=False,
    )

    # Relationship to a `HealthTopic` record.
    health_topic = sqlalchemy.orm.relationship(
        argument="HealthTopic",
        back_populates="health_topic_see_references",
        uselist=False,
    )

    # Relationship to a `SeeReference` record.
    see_reference = sqlalchemy.orm.relationship(
        argument="SeeReference",
        back_populates="health_topic_see_references",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("health_topic_id", "see_reference_id"),
        # Set table schema.
        {"schema": "medline"},
    )


class HealthTopicBodyPart(Base, OrmFightForBase):
    """ Associative table between `HealthTopic` and `BodyPart` records."""

    # Set table name.
    __tablename__ = "health_topic_body_parts"

    # Autoincrementing primary key ID.
    health_topic_body_part_id = sqlalchemy.Column(
        name="health_topic_body_part_id",
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

    # Foreign key to the body-part ID.
    body_part_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("medline.body_parts.body_part_id"),
        name="body_part_id",
        nullable=False,
    )

    # Relationship to a `HealthTopic` record.
    health_topic = sqlalchemy.orm.relationship(
        argument="HealthTopic",
        back_populates="health_topic_body_parts",
        uselist=False,
    )

    # Relationship to a `BodyPart` record.
    body_part = sqlalchemy.orm.relationship(
        argument="BodyPart",
        back_populates="health_topic_body_parts",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("health_topic_id", "body_part_id"),
        # Set table schema.
        {"schema": "medline"},
    )


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

    # Foreign key to the primary-institute ID.
    primary_institute_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "medline.primary_institutes.primary_institute_id"
        ),
        name="primary_institute_id",
        nullable=True,
    )

    # Relationship to a `PrimaryInstitute` record.
    primary_institute = sqlalchemy.orm.relationship(
        argument="PrimaryInstitute",
        back_populates="health_topics",
        uselist=False,
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

    # Relationship to a list of `Descriptor` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="Descriptor",
        secondary="medline.health_topic_descriptors",
        back_populates="health_topics",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicDescriptor` records.
    health_topic_descriptors = sqlalchemy.orm.relationship(
        argument="HealthTopicDescriptor",
        back_populates="health_topic",
        uselist=True,
    )

    # Self-referential relationship via an associative table as described under
    # https://blog.ramosly.com/sqlalchemy-orm-setting-up-self-referential-
    # many-to-many-relationships-866c97d9308b
    related_health_topics = sqlalchemy.orm.relationship(
        "HealthTopic",
        secondary="medline.health_topic_related_health_topics",
        primaryjoin=health_topic_id
        == HealthTopicRelatedHealthTopic.health_topic_id,
        secondaryjoin=health_topic_id
        == HealthTopicRelatedHealthTopic.related_health_topic_id,
        uselist=True,
    )

    # Relationship to a list of `SeeReference` records.
    see_references = sqlalchemy.orm.relationship(
        argument="SeeReference",
        secondary="medline.health_topic_see_references",
        back_populates="health_topics",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicSeeReference` records.
    health_topic_see_references = sqlalchemy.orm.relationship(
        argument="HealthTopicSeeReference",
        back_populates="health_topic",
        uselist=True,
    )

    # Relationship to a list of `BodyPart` records.
    body_parts = sqlalchemy.orm.relationship(
        argument="BodyPart",
        secondary="medline.health_topic_body_parts",
        back_populates="health_topics",
        uselist=True,
    )

    # Relationship to a list of `HealthTopicBodyPart` records.
    health_topic_body_parts = sqlalchemy.orm.relationship(
        argument="HealthTopicBodyPart",
        back_populates="health_topic",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "medline"
    }
