# -*- coding: utf-8 -*-

import sqlalchemy.orm
import sqlalchemy.dialects.postgresql

from fform.orm_base import Base
from fform.orm_base import OrmFightForBase
from fform.orm_ct import GenderType


class User(Base, OrmFightForBase):
    """Table of user records."""

    # set table name
    __tablename__ = "users"

    # Autoincrementing primary key ID.
    user_id = sqlalchemy.Column(
        name="user_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Auth0 user ID.
    auth0_user_id = sqlalchemy.Column(
        name="auth0_user_id",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        nullable=False,
    )

    # User email.
    email = sqlalchemy.Column(
        name="email",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Relationship to a list of `Search` records.
    searches = sqlalchemy.orm.relationship(
        argument="Search",
        secondary="app.user_searches",
        back_populates="user",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="app.user_studies",
        uselist=True,
    )

    # Relationship to a list of `Citation` records.
    citations = sqlalchemy.orm.relationship(
        argument="Citation",
        secondary="app.user_citations",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "app"
    }


class Search(Base, OrmFightForBase):
    """Table of searches."""

    # set table name
    __tablename__ = "searches"

    # Autoincrementing primary key ID.
    search_id = sqlalchemy.Column(
        name="search_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Search UUID.
    search_uuid = sqlalchemy.Column(
        name="search_uuid",
        type_=sqlalchemy.dialects.postgresql.UUID(as_uuid=True),
        unique=True,
        nullable=False,
    )

    # Search title.
    title = sqlalchemy.Column(
        name="title",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # The patient gender.
    gender = sqlalchemy.Column(
        name="gender",
        type_=sqlalchemy.types.Enum(GenderType),
        nullable=True,
    )

    # The beginning of the year-range studies will be limited to for this
    # search.
    year_beg = sqlalchemy.Column(
        name="year_beg",
        type_=sqlalchemy.types.Integer(),
        nullable=True,
    )

    # The end of the year-range studies will be limited to for this search.
    year_end = sqlalchemy.Column(
        name="year_end",
        type_=sqlalchemy.types.Integer(),
        nullable=True,
    )

    # The beginning of the age-range studies will be limited to for this search.
    age_beg = sqlalchemy.Column(
        name="age_beg",
        type_=sqlalchemy.types.Integer(),
        nullable=True,
    )

    # The end of the age-range studies will be limited to for this search.
    age_end = sqlalchemy.Column(
        name="age_end",
        type_=sqlalchemy.types.Integer(),
        nullable=True,
    )

    # Relationship to a `User` record.
    user = sqlalchemy.orm.relationship(
        argument="User",
        secondary="app.user_searches",
        back_populates="searches",
        uselist=False,
    )

    # Relationship to a list of `Descriptor` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="Descriptor",
        secondary="app.search_descriptors",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = (
        # Set table schema.
        {"schema": "app"}
    )


class SearchDescriptor(Base, OrmFightForBase):
    """Associative table between `Search` and `Descriptor` records."""

    # Set table name.
    __tablename__ = "search_descriptors"

    # Autoincrementing primary key ID.
    search_descriptor_id = sqlalchemy.Column(
        name="search_descriptor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the search ID.
    search_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("app.searches.search_id"),
        name="search_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
        index=True,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('search_id', 'descriptor_id'),
        # Set table schema.
        {"schema": "app"}
    )


class UserSearch(Base, OrmFightForBase):
    """Associative table between `User` and `Search` records."""

    # Set table name.
    __tablename__ = "user_searches"

    # Autoincrementing primary key ID.
    user_search_id = sqlalchemy.Column(
        name="user_search_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the user ID.
    user_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("app.users.user_id"),
        name="user_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the search ID.
    search_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("app.searches.search_id"),
        name="search_id",
        nullable=False,
        index=True,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('user_id', 'search_id'),
        # Set table schema.
        {"schema": "app"}
    )


class UserStudy(Base, OrmFightForBase):
    """Associative table between `User` and `Study` records."""

    # Set table name.
    __tablename__ = "user_studies"

    # Autoincrementing primary key ID.
    user_study_id = sqlalchemy.Column(
        name="user_study_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the user ID.
    user_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("app.users.user_id"),
        name="user_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
        index=True,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("user_id", "study_id"),
        # Set table schema.
        {"schema": "app"}
    )


class UserCitation(Base, OrmFightForBase):
    """Associative table between `User` and `Citation` records."""

    # Set table name.
    __tablename__ = "user_citations"

    # Autoincrementing primary key ID.
    user_citation_id = sqlalchemy.Column(
        name="user_citation_id",
        type_=sqlalchemy.types.Integer(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the user ID.
    user_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("app.users.user_id"),
        name="user_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the citation ID.
    citation_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.citations.citation_id"),
        name="citation_id",
        nullable=False,
        index=True,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("user_id", "citation_id"),
        # Set table schema.
        {"schema": "app"}
    )
