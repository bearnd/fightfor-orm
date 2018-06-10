# coding=utf-8

import hashlib

import sqlalchemy.orm

from fform.orm_base import Base, OrmBase
from fform.utils import EnumBase


class AbstractTextCategory(EnumBase):
    """Enumeration of the values of the `NlmCategory` attribute under the
    `<AbstractText>` element."""

    BACKGROUND = "Background"
    OBJECTIVE = "Objective"
    METHODS = "Methods"
    RESULTS = "Results"
    CONCLUSIONS = "Conclusions"
    UNASSIGNED = "Unassigned"


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

    PRINT = "Print"
    PRINT_ELECTRONIC = "Print-Electronic"
    ELECTRONIC = "Electronic"
    ELECTRONIC_PRINT = "Electronic-Print"
    ELECTRONIC_ECOLLECTION = "Electronic-eCollection"


class JournalIssnType(EnumBase):
    """Enumeration of the values of the `IssnType` attribute under the
    `<ISSN>` element."""

    PRINT = "Print"
    ELECTRONIC = "Electronic"
    UNDETERMINED = "Undetermined"


class AbstractText(Base, OrmBase):
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
        default=AbstractTextCategory.unassigned,
        index=True
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
        type_=sqlalchemy.types.Binary(),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to an `Article` record.
    article = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="article_abstract_texts",
        back_populates="abstract_texts"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates("text")
    def update_md5(self, key, value):

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        # Encode the abstract text to UTF8 (in case it contains unicode
        # characters).
        text_encoded = str(value).encode("utf-8")

        # Calculate the MD5 hash of the encoded abstract text and store
        # under the `md5` attribute.
        md5 = hashlib.md5(text_encoded).digest()
        self.md5 = md5

        return value


class AccessionNumber(Base, OrmBase):
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
        type_=sqlalchemy.types.Binary(),
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

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        # Encode the accession number to UTF8 (in case it contains unicode
        # characters).
        accession_number_encoded = str(value).encode("utf-8")

        # Calculate the MD5 hash of the encoded accession number  and store
        # under the `md5` attribute.
        md5 = hashlib.md5(accession_number_encoded).digest()
        self.md5 = md5

        return value


class Affiliation(Base, OrmBase):
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
        nullable=False
    )

    # MD5 hash of the `affiliation` field.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.Binary(),
        unique=True,
        index=True
    )

    # Relationship to a list of `Author` records.
    authors = sqlalchemy.orm.relationship(
        argument="Author",
        secondary="article_author_affiliations",
        back_populates="affiliations",
    )

    # Relationship to a list of `Article` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="article_author_affiliations",
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

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        affiliation_full = " ".join([
            str(self.affiliation),
            str(self.affiliation_identifier),
            str(value),
        ])

        # Encode the full concatenated name to UTF8 (in case it contains
        # unicode characters).
        affiliation_encoded = affiliation_full.encode("utf-8")

        # Calculate the MD5 hash of the encoded full concatenated name and store
        # under the `md5` attribute.
        md5 = hashlib.md5(affiliation_encoded).digest()
        self.md5 = md5

        return value


class Article(Base, OrmBase):
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
        sqlalchemy.ForeignKey("journals.journal_id"),
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
        type_=sqlalchemy.types.Binary(),
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
        secondary="article_abstract_texts",
        back_populates="article"
    )

    # Relationship to a list of `Author` records.
    authors = sqlalchemy.orm.relationship(
        argument="Author",
        secondary="article_author_affiliations",
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
        secondary="article_grants",
        back_populates="articles"
    )

    # Relationship to a list of `PublicationType` records.
    publication_types = sqlalchemy.orm.relationship(
        argument="PublicationType",
        secondary="article_publication_types",
        back_populates="articles"
    )

    # Relationship to a list of `Author` records.
    affiliations = sqlalchemy.orm.relationship(
        argument="Affiliation",
        secondary="article_author_affiliations",
        back_populates="articles",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates("title")
    def update_md5(self, key, value):

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        # Encode the title to UTF8 (in case it contains unicode characters).
        title_encoded = str(value).encode("utf-8")

        # Calculate the MD5 hash of the title and store under the `md5`
        # attribute.
        md5 = hashlib.md5(title_encoded).digest()
        self.md5 = md5

        return value


class ArticleAbstractText(Base, OrmBase):
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
        sqlalchemy.ForeignKey("articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the author ID.
    abstract_text_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("abstract_texts.abstract_text_id"),
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
        sqlalchemy.UniqueConstraint("supplemental_id", "concept_id"),
        # Set table schema.
        {"schema": "pubmed"}
    )


class ArticleAuthorAffiliation(Base, OrmBase):
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
        sqlalchemy.ForeignKey("articles.article_id"),
        name="article_id",
        nullable=False
    )

    # Foreign key to the author ID.
    author_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("authors.author_id"),
        name="author_id",
        nullable=False
    )

    # Foreign key to the author ID.
    affiliation_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("affiliations.affiliation_id"),
        name="affiliation_id",
        nullable=True
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


class ArticleDatabankAccessionNumber(Base, OrmBase):
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
        sqlalchemy.ForeignKey("articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the databank ID.
    databank_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("databanks.databank_id"),
        name="databank_id",
        nullable=False,
    )

    # Foreign key to the accession number ID.
    accession_number_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("accession_numbers.accession_number_id"),
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


class ArticleGrant(Base, OrmBase):
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
        sqlalchemy.ForeignKey("articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the grant ID.
    grant_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("grants.grant_id"),
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


class CitationChemical(Base, OrmBase):
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
        sqlalchemy.ForeignKey("citations.citation_id"),
        name="citation_id",
        nullable=False,
    )

    # Foreign key to the chemical ID.
    chemical_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("chemicals.chemical_id"),
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


class CitationDescriptorQualifier(Base, OrmBase):
    """Associative table between `Citation`, `Descriptor` and `Qualifier`
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
        sqlalchemy.ForeignKey("citations.citation_id"),
        name="citation_id",
        nullable=False,
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
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
        sqlalchemy.ForeignKey("qualifiers.qualifier_id"),
        name="qualifier_id",
        nullable=True,
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


class CitationIdentifier(Base, OrmBase):
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
        sqlalchemy.ForeignKey("citations.citation_id"),
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
        sqlalchemy.UniqueConstraint("citation_id", "identifier_id"),
        # Set table schema.
        {"schema": "pubmed"}
    )


class CitationKeyword(Base, OrmBase):
    """Associative table between `Citation` and `Keyword` records."""

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
        sqlalchemy.ForeignKey("citations.citation_id"),
        name="citation_id",
        nullable=False,
    )

    # Foreign key to the keyword ID.
    keyword_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("keywords.keyword_id"),
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


class ArticlePublicationType(Base, OrmBase):
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
        sqlalchemy.ForeignKey("articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the publication type ID.
    publication_type_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("publication_types.publication_type_id"),
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


class Author(Base, OrmBase):
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
        type_=sqlalchemy.types.Binary(),
        unique=True,
        index=True,
        nullable=False
    )

    # Relationship to a list of `Article` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="article_author_affiliations",
        back_populates="authors"
    )

    # Relationship to a list of `Affiliation` records.
    affiliations = sqlalchemy.orm.relationship(
        argument="Affiliation",
        secondary="article_author_affiliations",
        back_populates="authors"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    def name_full(self):
        name = " ".join([
            str(self.name_first),
            str(self.name_initials),
            str(self.name_last),
            str(self.name_suffix),
        ])
        return name

    @sqlalchemy.orm.validates(
        "author_identifier",
        "name_first",
        "name_initials",
        "name_last",
        "name_suffix",
        "email",
    )
    def update_md5(self, key, value):

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        # Retrieve the full concatenated name.
        name = " ".join([
            str(self.author_identifier),
            str(self.email),
            self.name_full(),
            str(value),
        ])

        # Encode the full concatenated name to UTF8 (in case it contains
        # unicode characters).
        name_encoded = name.encode("utf-8")

        # Calculate the MD5 hash of the encoded full concatenated name and store
        # it under the `md5` attribute.
        md5 = hashlib.md5(name_encoded).digest()
        self.md5 = md5

        return value


class Chemical(Base, OrmBase):
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
        secondary="citation_chemicals",
        back_populates="chemicals"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class Citation(Base, OrmBase):
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
        sqlalchemy.ForeignKey("articles.article_id"),
        name="article_id",
        nullable=False,
    )

    # Foreign key to the journal info ID.
    journal_info_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("journal_infos.journal_info_id"),
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
        secondary="citation_chemicals",
        back_populates="citations"
    )

    # Relationship to a list of `Keyword` records.
    keywords = sqlalchemy.orm.relationship(
        argument="Keyword",
        secondary="citation_keywords",
        back_populates="citations"
    )

    # # Relationship to a list of `Keyword` records.
    descriptors_qualifiers = sqlalchemy.orm.relationship(
        argument="CitationDescriptorQualifier",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class Databank(Base, OrmBase):
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
        type_=sqlalchemy.types.Binary(),
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

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        # Encode the databank name to UTF8 (in case it contains unicode
        # characters).
        databank_name_encoded = str(value).encode("utf-8")

        # Calculate the MD5 hash of the encoded databank name and store under
        # the `md5` attribute.
        md5 = hashlib.md5(databank_name_encoded).digest()
        self.md5 = md5

        return value


class Descriptor(Base, OrmBase):
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


class Grant(Base, OrmBase):
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
        type_=sqlalchemy.types.Binary(),
        unique=True,
        index=True,
        nullable=False
    )

    # Relationship to a list of `Article` records.
    articles = sqlalchemy.orm.relationship(
        argument="Article",
        secondary="article_grants",
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

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        # Assemble the full grant description.
        description = " ".join([
            str(self.uid),
            str(self.acronym),
            str(self.agency),
            str(self.country),
            str(value),
        ])

        # Encode the full description to UTF8 (in case it contains unicode
        # characters).
        description_encoded = description.encode("utf-8")

        # Calculate the MD5 hash of the encoded full description and store it
        # under the `md5` attribute.
        md5 = hashlib.md5(description_encoded).digest()
        self.md5 = md5

        return value


class Journal(Base, OrmBase):
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
        default=JournalIssnType.undetermined
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
        type_=sqlalchemy.types.Binary(),
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

    @sqlalchemy.orm.validates("title", "abbreviation")
    def update_md5(self, key, value):

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        # Retrieve the full concatenated name.
        journal_title_full = " ".join([
            str(self.title),
            str(self.abbreviation),
            str(value),
        ])

        # Encode the full concatenated name to UTF8 (in case it contains
        # unicode characters).
        journal_title_encoded = journal_title_full.encode("utf-8")

        # Calculate the MD5 hash of the encoded full concatenated name and store
        # under the `md5` attribute.
        md5 = hashlib.md5(journal_title_encoded).digest()
        self.md5 = md5

        return value


class JournalInfo(Base, OrmBase):
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


class Keyword(Base, OrmBase):
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
        type_=sqlalchemy.types.Binary(),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `Citation` records.
    citations = sqlalchemy.orm.relationship(
        argument="Citation",
        secondary="citation_keywords",
        back_populates="keywords",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }

    @sqlalchemy.orm.validates("keyword")
    def update_md5(self, key, value):

        # Dumb hack to make the linter shut up that the `key` isn't used.
        assert key

        # Encode the keyword to UTF8 (in case it contains unicode characters).
        keyword_encoded = str(value).encode("utf-8")

        # Calculate the MD5 hash of the encoded keyword and store under the
        # `md5` attribute.
        md5 = hashlib.md5(keyword_encoded).digest()
        self.md5 = md5

        return value


class PublicationType(Base, OrmBase):
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
        secondary="article_publication_types",
        back_populates="publication_types"
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "pubmed"
    }


class Qualifier(Base, OrmBase):
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