# -*- coding: utf-8 -*-

import sqlalchemy.orm
from geoalchemy2 import Geometry

from fform.orm_base import Base
from fform.orm_base import OrmFightForBase
from fform.utils import EnumBase


class AbstractTextCategory(EnumBase):
    """Enumeration of the values of the `NlmCategory` attribute under the
    `<AbstractText>` element."""

    BACKGROUND = "background"
    OBJECTIVE = "objective"
    METHODS = "methods"
    RESULTS = "results"
    CONCLUSIONS = "conclusions"
    UNASSIGNED = "unassigned"


class ArticleIdentifierType(EnumBase):
    """Enumeration of the values of the `IdType` attribute under the
    `<ArticleId>` element."""

    DOI = "doi"
    PII = "pii"
    PMCPID = "pmcpid"
    PMPID = "pmpid"
    PMC = "pmc"
    MID = "mid"
    SICI = "sici"
    PUBMED = "pubmed"
    MEDLINE = "medline"
    PMCID = "pmcid"


class ArticlePubModel(EnumBase):
    """Enumeration of the values of the `PubModel` attribute under the
    `<Article>` element."""

    PRINT = "print"
    PRINT_ELECTRONIC = "print_electronic"
    ELECTRONIC = "electronic"
    ELECTRONIC_PRINT = "electronic_print"
    ELECTRONIC_ECOLLECTION = "electronic_ecollection"


class JournalIssnType(EnumBase):
    """Enumeration of the values of the `IssnType` attribute under the
    `<ISSN>` element."""

    PRINT = "print"
    ELECTRONIC = "electronic"
    UNDETERMINED = "undetermined"


class AbstractText(Base, OrmFightForBase):
    """Table of `<AbstractText>` element records."""

    # set table name
    __tablename__ = "abstract_texts"

    # Autoincrementing primary key ID.
    abstract_text_id = sqlalchemy.Column(
        name="abstract_text_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Abstract text label (referring to the `Label` attribute under the
    # `<AbstractText>` element).
    label = sqlalchemy.Column(
        name="label",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Abstract text category (referring to the `NlmCategory` attribute of the
    # `<AbstractText>` element).
    category = sqlalchemy.Column(
        name="category",
        type_=sqlalchemy.types.Enum(AbstractTextCategory),
        nullable=True,
        default=AbstractTextCategory.UNASSIGNED,
        index=True,
    )

    # Abstract text (value of the `<AbstractText>` element).
    text = sqlalchemy.Column(
        name="text",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # MD5 hash of the abstract text.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to an `Article` record.
    article = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="pubmed.article_abstract_texts",
        back_populates="abstract_texts"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates("text")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "text": self.text,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class AccessionNumber(Base, OrmFightForBase):
    """Table of `<AccessionNumber>` element records."""

    # set table name
    __tablename__ = "accession_numbers"

    # Autoincrementing primary key ID.
    accession_number_id = sqlalchemy.Column(
        name="accession_number_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Accession number value (referring to the `<AccessionNumber>` element).
    accession_number = sqlalchemy.Column(
        name="accession_number",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        nullable=False,
        index=True,
    )

    # MD5 hash of the accession_number.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates("accession_number")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "accession_number": self.accession_number,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Affiliation(Base, OrmFightForBase):
    """Table of `<Affliliation>` element records."""

    # set table name
    __tablename__ = "affiliations"

    # Autoincrementing primary key ID.
    affiliation_id = sqlalchemy.Column(
        name="affiliation_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Affiliation identifier (referring to the `<Identifier>` element).
    affiliation_identifier = sqlalchemy.Column(
        name="affiliation_identifier",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Affiliation identifier source (referring to the `Source` attribute of the
    # <Identifier>` element).
    affiliation_identifier_source = sqlalchemy.Column(
        name="affiliation_identifier_source",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Affiliation name (referring to the `<Affliliation>` element).
    affiliation = sqlalchemy.Column(
        name="affiliation",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Foreign key to the canonical affiliation ID.
    affiliation_canonical_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "pubmed.affiliations_canonical.affiliation_canonical_id"
        ),
        name="affiliation_canonical_id",
        nullable=True,
    )

    # Relationship to a `AffiliationCanonical` record.
    affiliation_canonical = sqlalchemy.orm.relationship(
        argument="AffiliationCanonical",
    )

    # MD5 hash of the `affiliation` field.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True
    )

    # Relationship to a list of `Author` records.
    authors = sqlalchemy.orm.relationship(
        argument="Author",
        secondary="pubmed.article_author_affiliations",
        back_populates="affiliations",
    )

    # Relationship to a list of `Article` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="pubmed.article_author_affiliations",
        back_populates="affiliations",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates(
        "affiliation",
        "affiliation_identifier",
    )
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "affiliation": self.affiliation,
            "affiliation_identifier": self.affiliation_identifier,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Article(Base, OrmFightForBase):
    """Table of `<Article>` element records."""

    # set table name
    __tablename__ = "articles"

    # Autoincrementing primary key ID.
    article_id = sqlalchemy.Column(
        name="article_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Publication year (referring to the `<Year>` element).
    publication_year = sqlalchemy.Column(
        name="publication_year",
        type_=sqlalchemy.types.SmallInteger(),
        nullable=False,
        index=True,
    )

    # Publication month (referring to the `<Month>` element).
    publication_month = sqlalchemy.Column(
        name="publication_month",
        type_=sqlalchemy.types.SmallInteger(),
        nullable=True,
    )

    # Publication day (referring to the `<Day>` element).
    publication_day = sqlalchemy.Column(
        name="publication_day",
        type_=sqlalchemy.types.SmallInteger(),
        nullable=True,
    )

    # Publication date (referring to either the `<ArticleDate>` element).
    date_published = sqlalchemy.Column(
        name="date_published",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Article publication model (referring to the `PubModel` attribute of the
    # `<Article>` element).
    publication_model = sqlalchemy.Column(
        name="publication_model",
        type_=sqlalchemy.types.Enum(ArticlePubModel),
        nullable=True,
        default=None,
    )

    # Foreign key to the journal this article was published under.
    journal_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.journals.journal_id"),
        name="journal_id",
        nullable=False
    )

    # Journal volume under which the article was published (referring to the
    # `<Volume>` element).
    journal_volume = sqlalchemy.Column(
        name="journal_volume",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Journal issue under which the article was published (referring to the
    # `<Issue>` element).
    journal_issue = sqlalchemy.Column(
        name="journal_issue",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Article title (referring to the `<ArticleTitle>` element).
    title = sqlalchemy.Column(
        name="title",
        type_=sqlalchemy.types.Unicode(),
        nullable=True
    )

    # Article pagination (referring to the `<Pagination>` element).
    pagination = sqlalchemy.Column(
        name="pagination",
        type_=sqlalchemy.types.Unicode(),
        nullable=True
    )

    # Article language (referring to the `<Language>` element).
    language = sqlalchemy.Column(
        name="language",
        type_=sqlalchemy.types.Unicode(length=3),
        nullable=True
    )

    # Article vernacular title (referring to the `<VernacularTitle>` element).
    title_vernacular = sqlalchemy.Column(
        name="title_vernacular",
        type_=sqlalchemy.types.Unicode(),
        nullable=True
    )

    # MD5 hash of the `title` field.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True
    )

    # Relationship to a `Journal` record.
    journal = sqlalchemy.orm.relationship(
        argument="Journal"
    )

    # Relationship to a list of `AbstractText` records.
    abstract_texts = sqlalchemy.orm.relationship(
        argument="AbstractText",
        secondary="pubmed.article_abstract_texts",
        back_populates="article"
    )

    # Relationship to a list of `Author` records.
    authors = sqlalchemy.orm.relationship(
        argument="Author",
        secondary="pubmed.article_author_affiliations",
        back_populates="articles",
    )

    # Relationship to a list of `ArticleDatabankAccessionNumber` records.
    databank_accession_numbers = sqlalchemy.orm.relationship(
        argument="ArticleDatabankAccessionNumber",
        back_populates="article"
    )

    # Relationship to a list of `Grant` records.
    grants = sqlalchemy.orm.relationship(
        argument="Grant",
        secondary="pubmed.article_grants",
        back_populates="articles"
    )

    # Relationship to a list of `PublicationType` records.
    publication_types = sqlalchemy.orm.relationship(
        argument="PublicationType",
        secondary="pubmed.article_publication_types",
        back_populates="articles"
    )

    # Relationship to a list of `Affiliation` records.
    affiliations = sqlalchemy.orm.relationship(
        argument="Affiliation",
        secondary="pubmed.article_author_affiliations",
        back_populates="articles",
    )

    # Relationship to a list of `AffiliationCanonical` records.
    affiliations_canonical = sqlalchemy.orm.relationship(
        argument="AffiliationCanonical",
        secondary="pubmed.article_author_affiliations",
        back_populates="articles"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates(
        "publication_year",
        "publication_month",
        "publication_day",
        "date_published",
        "publication_model",
        "journal_id",
        "journal_volume",
        "journal_issue",
        "title",
        "pagination",
        "language",
        "title_vernacular",
    )
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "publication_year": self.publication_year,
            "publication_month": self.publication_month,
            "publication_day": self.publication_day,
            "date_published": self.date_published,
            "publication_model": self.publication_model,
            "journal_id": self.journal_id,
            "journal_volume": self.journal_volume,
            "journal_issue": self.journal_issue,
            "title": self.title,
            "pagination": self.pagination,
            "language": self.language,
            "title_vernacular": self.title_vernacular,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class ArticleAbstractText(Base, OrmFightForBase):
    """Associative table between `Article` and `AbstractText` records."""

    # set table name
    __tablename__ = "article_abstract_texts"

    # Autoincrementing primary key ID.
    article_abstract_text_id = sqlalchemy.Column(
        name="article_abstract_text_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the article ID.
    article_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the author ID.
    abstract_text_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.abstract_texts.abstract_text_id"),
        name="abstract_text_id",
        nullable=False,
    )

    # Ordinance of the abstract text in the abstract.
    ordinance = sqlalchemy.Column(
        name="ordinance",
        type_=sqlalchemy.types.SmallInteger(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("article_id", "abstract_text_id"),
        # Set table schema.
        {"schema": "pubmed"}
    )


class ArticleAuthorAffiliation(Base, OrmFightForBase):
    """Associative table between `Article`, `Author`, and `Affiliation`
     records."""

    # set table name
    __tablename__ = "article_author_affiliations"

    # Autoincrementing primary key ID.
    article_author_affiliation_id = sqlalchemy.Column(
        name="article_author_affiliation_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the article ID.
    article_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.articles.article_id"),
        name="article_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the author ID.
    author_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.authors.author_id"),
        name="author_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the affiliation ID.
    affiliation_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.affiliations.affiliation_id"),
        name="affiliation_id",
        nullable=True,
        index=True,
    )

    # Foreign key to the canonical affiliation ID.
    affiliation_canonical_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "pubmed.affiliations_canonical.affiliation_canonical_id"
        ),
        name="affiliation_canonical_id",
        nullable=True,
        index=True,
    )

    # Ordinance of the author in the article.
    ordinance = sqlalchemy.Column(
        name="ordinance",
        type_=sqlalchemy.types.SmallInteger(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint(
            "article_id",
            "author_id",
            "affiliation_id",
        ),
        # Set table schema.
        {"schema": "pubmed"}
    )


class ArticleDatabankAccessionNumber(Base, OrmFightForBase):
    """Associative table between `Article`, `Databank` and `AccessionNumber`
    records."""

    # set table name
    __tablename__ = "article_databank_accession_numbers"

    # Autoincrementing primary key ID.
    article_databank_accession_number_id = sqlalchemy.Column(
        name="article_databank_accession_number_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the article ID.
    article_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the databank ID.
    databank_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.databanks.databank_id"),
        name="databank_id",
        nullable=False,
    )

    # Foreign key to the accession number ID.
    accession_number_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.accession_numbers.accession_number_id"),
        name="accession_number_id",
        nullable=False,
    )

    # Relationship to an `Article` record.
    article = sqlalchemy.orm.relationship(
        argument="Article",
        back_populates="databank_accession_numbers"
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint(
            "article_id",
            "databank_id",
            "accession_number_id",
        ),
        # Set table schema.
        {"schema": "pubmed"}
    )


class ArticleGrant(Base, OrmFightForBase):
    """Associative table between `Article` and `Grant` records."""

    # set table name
    __tablename__ = "article_grants"

    # Autoincrementing primary key ID.
    article_grant_id = sqlalchemy.Column(
        name="article_grant_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the article ID.
    article_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the grant ID.
    grant_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.grants.grant_id"),
        name="grant_id",
        nullable=False
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("article_id", "grant_id"),
        # Set table schema.
        {"schema": "pubmed"}
    )


class CitationChemical(Base, OrmFightForBase):
    """Associative table between `Citation` and `Chemical` records."""

    # set table name
    __tablename__ = "citation_chemicals"

    # Autoincrementing primary key ID.
    citation_chemical_id = sqlalchemy.Column(
        name="citation_chemical_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the citation ID.
    citation_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.citations.citation_id"),
        name="citation_id",
        nullable=False,
    )

    # Foreign key to the chemical ID.
    chemical_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.chemicals.chemical_id"),
        name="chemical_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("citation_id", "chemical_id"),
        # Set table schema.
        {"schema": "pubmed"}
    )


class CitationDescriptorQualifier(Base, OrmFightForBase):
    """Associative table between `Citation`, `PmDescriptor` and `PmQualifier`
    records."""

    # set table name
    __tablename__ = "citation_descriptors_qualifiers"

    # Autoincrementing primary key ID.
    citation_descriptor_qualifier_id = sqlalchemy.Column(
        name="citation_descriptor_qualifier_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the citation ID.
    citation_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.citations.citation_id"),
        name="citation_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
        index=True,
    )

    # Whether the descriptor is major or not (referring to the `MajorTopicYN`
    # attribute of the `<DescriptorName>` element).
    is_descriptor_major = sqlalchemy.Column(
        name="is_descriptor_major",
        type_=sqlalchemy.types.Boolean(),
        nullable=False
    )

    # Foreign key to the qualifier ID.
    qualifier_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.qualifiers.qualifier_id"),
        name="qualifier_id",
        nullable=True,
        index=True,
    )

    # Whether the qualifier is major or not (referring to the `MajorTopicYN`
    # attribute of the `<QualifierName>` element).
    is_qualifier_major = sqlalchemy.Column(
        name="is_qualifier_major",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint(
            "citation_id",
            "descriptor_id",
            "qualifier_id",
        ),
        # Set table schema.
        {"schema": "pubmed"}
    )


class CitationIdentifier(Base, OrmFightForBase):
    """Associative table between `Citation` and `Identifier` records."""

    # set table name
    __tablename__ = "citation_identifiers"

    # Autoincrementing primary key ID.
    citation_identifier_id = sqlalchemy.Column(
        name="citation_identifier_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the citation ID.
    citation_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.citations.citation_id"),
        name="citation_id",
        nullable=False,
    )

    # Identifier type (referring to the `IdType` attribute of the `<ArticleId>`
    # element).
    identifier_type = sqlalchemy.Column(
        name="identifier_type",
        type_=sqlalchemy.types.Enum(ArticleIdentifierType),
        nullable=False,
        index=True,
    )

    # Identifier (referring to the value of the `<ArticleId>` element).
    identifier = sqlalchemy.Column(
        name="identifier",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("citation_id", "identifier"),
        # Set table schema.
        {"schema": "pubmed"}
    )


class CitationKeyword(Base, OrmFightForBase):
    """Associative table between `Citation` and `PmKeyword` records."""

    # set table name
    __tablename__ = "citation_keywords"

    # Autoincrementing primary key ID.
    citation_keyword_id = sqlalchemy.Column(
        name="citation_keyword_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the citation ID.
    citation_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.citations.citation_id"),
        name="citation_id",
        nullable=False,
    )

    # Foreign key to the keyword ID.
    keyword_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.keywords.keyword_id"),
        name="keyword_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("citation_id", "keyword_id"),
        # Set table schema.
        {"schema": "pubmed"}
    )


class ArticlePublicationType(Base, OrmFightForBase):
    """Associative table between `Article` and `PublicationType` records."""

    # set table name
    __tablename__ = "article_publication_types"

    # Autoincrementing primary key ID.
    article_publication_type_id = sqlalchemy.Column(
        name="article_publication_type_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the article ID.
    article_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the publication type ID.
    publication_type_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.publication_types.publication_type_id"),
        name="publication_type_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint("article_id", "publication_type_id"),
        # Set table schema.
        {"schema": "pubmed"}
    )


class Author(Base, OrmFightForBase):
    """Table of `<Author>` element records."""

    # set table name
    __tablename__ = "authors"

    # Autoincrementing primary key ID.
    author_id = sqlalchemy.Column(
        name="author_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Author identifier (referring to the `<Identifier>` element).
    author_identifier = sqlalchemy.Column(
        name="author_identifier",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Author identifier source (referring to the `Source` attribute of the
    # <Identifier>` element).
    author_identifier_source = sqlalchemy.Column(
        name="author_identifier_source",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Author first name (referring to the `<ForeName>` element).
    name_first = sqlalchemy.Column(
        name="name_first",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Author last name (referring to the `<LastName>` element).
    name_last = sqlalchemy.Column(
        name="name_last",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Author initials (referring to the `<Initials>` element).
    name_initials = sqlalchemy.Column(
        name="name_initials",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Author suffix (referring to the `<Suffix>` element).
    name_suffix = sqlalchemy.Column(
        name="name_suffix",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Author email (possibly extraction from the affiliation).
    email = sqlalchemy.Column(
        name="email",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # MD5 hash of the author's full name.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False
    )

    # Relationship to a list of `Article` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="pubmed.article_author_affiliations",
        back_populates="authors"
    )

    # Relationship to a list of `Affiliation` records.
    affiliations = sqlalchemy.orm.relationship(
        argument="Affiliation",
        secondary="pubmed.article_author_affiliations",
        back_populates="authors"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates(
        "author_identifier",
        "name_first",
        "name_initials",
        "name_last",
        "name_suffix",
        "email",
    )
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "author_identifier": self.author_identifier,
            "name_first": self.name_first,
            "name_initials": self.name_initials,
            "name_last": self.name_last,
            "name_suffix": self.name_suffix,
            "email": self.email,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Chemical(Base, OrmFightForBase):
    """Table of `<Chemical>` element records."""

    # set table name
    __tablename__ = "chemicals"

    # Autoincrementing primary key ID.
    chemical_id = sqlalchemy.Column(
        name="chemical_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Chemical registry number (referring to the `<RegistryNumber>` element).
    num_registry = sqlalchemy.Column(
        name="num_registry",
        type_=sqlalchemy.types.Unicode(),
        index=True,
        nullable=True
    )

    # Publication type UID (referring to the `UI` attribute of the
    # `<NameOfSubstance>` element).
    uid = sqlalchemy.Column(
        name="uid",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        index=True,
        nullable=False,
    )

    # Chemical name (referring to the `<NameOfSubstance>` element).
    chemical = sqlalchemy.Column(
        name="chemical",
        type_=sqlalchemy.types.Unicode(),
        nullable=False
    )

    # Relationship to a list of `Citation` records.
    citations = sqlalchemy.orm.relationship(
        argument="Citation",
        secondary="pubmed.citation_chemicals",
        back_populates="chemicals"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class Citation(Base, OrmFightForBase):
    """Table of `<MedlineCitation>` element records."""

    # set table name
    __tablename__ = "citations"

    # Autoincrementing primary key ID.
    citation_id = sqlalchemy.Column(
        name="citation_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Citation PMID (referring to the `<PMID>` element).
    pmid = sqlalchemy.Column(
        name="pmid",
        type_=sqlalchemy.types.Integer(),
        unique=True,
        nullable=False,
    )

    # Citation creation date (referring to either the `<DateCreated>` element).
    date_created = sqlalchemy.Column(
        name="date_created",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Citation completion date (referring to either the `<DateCompleted>`
    # element).
    date_completion = sqlalchemy.Column(
        name="date_completion",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Citation revision date (referring to the `<DateRevised>` element).
    date_revision = sqlalchemy.Column(
        name="date_revision",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Foreign key to the article ID.
    article_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the journal info ID.
    journal_info_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("pubmed.journal_infos.journal_info_id"),
        name="journal_info_id",
        nullable=False,
    )

    # Number of references in citation (referring to the `<NumberofReferences>`
    # element).
    num_references = sqlalchemy.Column(
        name="num_references",
        type_=sqlalchemy.types.SmallInteger(),
        nullable=True,
    )

    # Relationship to an `Article` record.
    article = sqlalchemy.orm.relationship(
        argument="Article",
    )

    # Relationship to a `JournalInfo` record.
    journal_info = sqlalchemy.orm.relationship(
        argument="JournalInfo",
    )

    # Relationship to a list of `Identifier` records.
    identifiers = sqlalchemy.orm.relationship(
        argument="CitationIdentifier",
    )

    # Relationship to a list of `Chemical` records.
    chemicals = sqlalchemy.orm.relationship(
        argument="Chemical",
        secondary="pubmed.citation_chemicals",
        back_populates="citations"
    )

    # Relationship to a list of `PmKeyword` records.
    keywords = sqlalchemy.orm.relationship(
        argument="PmKeyword",
        secondary="pubmed.citation_keywords",
        back_populates="citations"
    )

    # Relationship to a list of `PmKeyword` records.
    descriptors_qualifiers = sqlalchemy.orm.relationship(
        argument="CitationDescriptorQualifier",
    )

    # Relationship to a list of `PmDescriptor` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="PmDescriptor",
        secondary="pubmed.citation_descriptors_qualifiers",
    )

    # Relationship to a list of `PmQualifier` records.
    qualifiers = sqlalchemy.orm.relationship(
        argument="PmQualifier",
        secondary="pubmed.citation_descriptors_qualifiers",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class Databank(Base, OrmFightForBase):
    """Table of `<DataBank>` element records."""

    # set table name
    __tablename__ = "databanks"

    # Autoincrementing primary key ID.
    databank_id = sqlalchemy.Column(
        name="databank_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Databank name (referring to the `<DataBankName>` element).
    databank = sqlalchemy.Column(
        name="databank",
        type_=sqlalchemy.types.Unicode(length=20),
        unique=True,
        nullable=False,
        index=True,
    )

    # MD5 hash of the databank name.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates("databank")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "databank": self.databank,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class PmDescriptor(Base, OrmFightForBase):
    """Table of `<DescriptorName>` element records."""

    # set table name
    __tablename__ = "descriptors"

    # Autoincrementing primary key ID.
    descriptor_id = sqlalchemy.Column(
        name="descriptor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Descriptor UID (referring to the `UI` attribute of the `<DescriptorName>`
    # element).
    uid = sqlalchemy.Column(
        name="uid",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        index=True,
        nullable=False,
    )

    # Descriptor qualifier name (value of the `<DescriptorName>` element).
    descriptor = sqlalchemy.Column(
        name="descriptor",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        nullable=False,
        index=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class Grant(Base, OrmFightForBase):
    """Table of `<Grant>` element records."""

    # set table name
    __tablename__ = "grants"

    # Autoincrementing primary key ID.
    grant_id = sqlalchemy.Column(
        name="grant_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Pubmed Grant ID (referring to the `<GrantID>` element).
    uid = sqlalchemy.Column(
        name="uid",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        nullable=True,
    )

    # Grant acronym (referring to the `<Acronym>` element).
    acronym = sqlalchemy.Column(
        name="acronym",
        type_=sqlalchemy.types.Unicode(length=2),
        nullable=True,
    )

    # Grant acronym (referring to the `<Agency>` element).
    agency = sqlalchemy.Column(
        name="agency",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Country of granting agency (referring to the `<Country>` element).
    country = sqlalchemy.Column(
        name="country",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # MD5 hash of the grant's full description.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False
    )

    # Relationship to a list of `Article` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="pubmed.article_grants",
        back_populates="grants"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates(
        "uid",
        "acronym",
        "agency",
        "country",
    )
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "uid": self.uid,
            "acronym": self.acronym,
            "agency": self.agency,
            "country": self.country,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Journal(Base, OrmFightForBase):
    """Table of `<Journal>` element records."""

    # set table name
    __tablename__ = "journals"

    # Autoincrementing primary key ID.
    journal_id = sqlalchemy.Column(
        name="journal_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Unique journal International Standard Serial Number (ISSN) (referring to
    # the `<ISSN>` element).
    issn = sqlalchemy.Column(
        name="issn",
        type_=sqlalchemy.types.Unicode(length=9),
        nullable=True,
        index=True,
    )

    # ISSN type (referring to the `IssnType` attribute of the `<ISSN>` element).
    issn_type = sqlalchemy.Column(
        name="issn_type",
        type_=sqlalchemy.types.Enum(JournalIssnType),
        nullable=True,
        default=JournalIssnType.UNDETERMINED
    )

    # Full journal title (referring to the `<Title>` element).
    title = sqlalchemy.Column(
        name="title",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Journal ISO abbreviation (referring to the `<ISOAbbreviation>` element).
    abbreviation = sqlalchemy.Column(
        name="abbreviation",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # MD5 hash of the journal `title` and `abbreviation` fields.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `Article` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        back_populates="journal"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates(
        "title",
        "abbreviation",
    )
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "title": self.title,
            "abbreviation": self.abbreviation,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class JournalInfo(Base, OrmFightForBase):
    """Table of `<MedlineJournalInfo>` element records."""

    # set table name
    __tablename__ = "journal_infos"

    # Autoincrementing primary key ID.
    journal_info_id = sqlalchemy.Column(
        name="journal_info_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Journal unique NLM ID (referring to the `<NlmUniqueID>` element).
    nlmid = sqlalchemy.Column(
        name="nlmid",
        type_=sqlalchemy.types.Unicode(length=9),
        unique=True,
        index=True,
        nullable=False,
    )

    # Link to a journal ISSN (referring to the `<ISSNLinking>` element).
    issn = sqlalchemy.Column(
        name="issn",
        type_=sqlalchemy.types.Unicode(length=9),
        nullable=True
    )

    # Country of journal publication (referring to the `<Country>` element).
    country = sqlalchemy.Column(
        name="country",
        type_=sqlalchemy.types.Unicode(),
        nullable=True
    )

    # Journal abbreviation (referring to the `<MedlineTA>` element).
    abbreviation = sqlalchemy.Column(
        name="abbreviation",
        type_=sqlalchemy.types.Unicode(),
        nullable=True
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class PmKeyword(Base, OrmFightForBase):
    """Table of `<Keyword>` element records."""

    # set table name
    __tablename__ = "keywords"

    # Autoincrementing primary key ID.
    keyword_id = sqlalchemy.Column(
        name="keyword_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Keyword name (value of the `<Keyword>` element).
    keyword = sqlalchemy.Column(
        name="keyword",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        nullable=False,
        index=True,
    )

    # MD5 hash of the keyword.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `Citation` records.
    citations = sqlalchemy.orm.relationship(
        argument="Citation",
        secondary="pubmed.citation_keywords",
        back_populates="keywords",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates("keyword")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "keyword": self.keyword,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class PublicationType(Base, OrmFightForBase):
    """Table of `<PublicationType>` element records."""

    # set table name
    __tablename__ = "publication_types"

    # Autoincrementing primary key ID.
    publication_type_id = sqlalchemy.Column(
        name="publication_type_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Publication type UID (referring to the `UI` attribute of the
    # `<PublicationType>` element).
    uid = sqlalchemy.Column(
        name="uid",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        nullable=False,
        index=True,
    )

    # Publication type (referring to the `<PublicationType>` element).
    publication_type = sqlalchemy.Column(
        name="publication_type",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Relationship to a list of `Article` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="pubmed.article_publication_types",
        back_populates="publication_types"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class PmQualifier(Base, OrmFightForBase):
    """Table of `<Qualifier>` element records."""

    # set table name
    __tablename__ = "qualifiers"

    # Autoincrementing primary key ID.
    qualifier_id = sqlalchemy.Column(
        name="qualifier_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Qualifier UID (referring to the `UI` attribute of the `<QualifierName>`
    # element).
    uid = sqlalchemy.Column(
        name="uid",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        nullable=False,
        index=True,
    )

    # Unique qualifier name (value of the `<QualifierName>` element).
    qualifier = sqlalchemy.Column(
        name="qualifier",
        type_=sqlalchemy.types.Unicode(),
        unique=True,
        nullable=False,
        index=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class AffiliationCanonical(Base, OrmFightForBase):
    """Table storing canonicalized version of affiliations with data retrieved
    from the Google Maps API."""

    # Set table name.
    __tablename__ = "affiliations_canonical"

    # Autoincrementing primary key ID.
    affiliation_canonical_id = sqlalchemy.Column(
        name="affiliation_canonical_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Google Place ID.
    google_place_id = sqlalchemy.Column(
        name="google_place_id",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
        index=True,
    )

    # Facility name.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Google Maps place URL.
    google_url = sqlalchemy.Column(
        name="google_url",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Facility URL.
    url = sqlalchemy.Column(
        name="url",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Facility formatted address.
    address = sqlalchemy.Column(
        name="address",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Facility phone-number.
    phone_number = sqlalchemy.Column(
        name="phone_number",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Facility coordinates.
    coordinates = sqlalchemy.Column(
        name="coordinates",
        type_=Geometry(geometry_type="POINT", srid=4326),
        nullable=True,
    )

    # Country.
    country = sqlalchemy.Column(
        name="country",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # First-order civil entity below the country level.
    administrative_area_level_1 = sqlalchemy.Column(
        name="administrative_area_level_1",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # Second-order civil entity below the country level.
    administrative_area_level_2 = sqlalchemy.Column(
        name="administrative_area_level_2",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Third-order civil entity below the country level.
    administrative_area_level_3 = sqlalchemy.Column(
        name="administrative_area_level_3",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Fourth-order civil entity below the country level.
    administrative_area_level_4 = sqlalchemy.Column(
        name="administrative_area_level_4",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Fifth-order civil entity below the country level.
    administrative_area_level_5 = sqlalchemy.Column(
        name="administrative_area_level_5",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Incorporated city or town political entity.
    locality = sqlalchemy.Column(
        name="locality",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # First-order civil entity below a locality.
    sublocality = sqlalchemy.Column(
        name="sublocality",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # First-order sublocality.
    sublocality_level_1 = sqlalchemy.Column(
        name="sublocality_level_1",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Second-order sublocality.
    sublocality_level_2 = sqlalchemy.Column(
        name="sublocality_level_2",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Third-order sublocality.
    sublocality_level_3 = sqlalchemy.Column(
        name="sublocality_level_3",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Fourth-order sublocality.
    sublocality_level_4 = sqlalchemy.Column(
        name="sublocality_level_4",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Fifth-order sublocality.
    sublocality_level_5 = sqlalchemy.Column(
        name="sublocality_level_5",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Commonly-used alternative name for the entity.
    colloquial_area = sqlalchemy.Column(
        name="colloquial_area",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Floor of a building address.
    floor = sqlalchemy.Column(
        name="floor",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Room of a building address.
    room = sqlalchemy.Column(
        name="room",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Major intersection, usually of two major roads.
    intersection = sqlalchemy.Column(
        name="intersection",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Named neighborhood.
    neighborhood = sqlalchemy.Column(
        name="neighborhood",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Postal box.
    post_box = sqlalchemy.Column(
        name="post_box",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Postal code as used to address postal mail within the country.
    postal_code = sqlalchemy.Column(
        name="postal_code",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Postal code prefix.
    postal_code_prefix = sqlalchemy.Column(
        name="postal_code_prefix",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Postal code suffix.
    postal_code_suffix = sqlalchemy.Column(
        name="postal_code_suffix",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Grouping of geographic areas, such as `locality` and `sublocality`, used
    # for mailing addresses in some countries.
    postal_town = sqlalchemy.Column(
        name="postal_town",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Named location, usually a building or collection of buildings with a
    # common name.
    premise = sqlalchemy.Column(
        name="premise",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # First-order entity below a named location, usually a singular building
    # within a collection of buildings with a common name.
    subpremise = sqlalchemy.Column(
        name="subpremise",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Named route.
    route = sqlalchemy.Column(
        name="route",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Precise street address.
    street_address = sqlalchemy.Column(
        name="street_address",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Precise street number.
    street_number = sqlalchemy.Column(
        name="street_number",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `Study` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="pubmed.article_author_affiliations",
        back_populates="affiliations_canonical"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }
