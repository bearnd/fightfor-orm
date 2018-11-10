# coding=utf-8

import hashlib

import sqlalchemy.orm

from fform.orm_base import Base
from fform.orm_base import OrmFightForBase
from fform.utils import EnumBase


class DescriptorClassType(EnumBase):
    """Enumeration of the descriptor-class types."""

    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"


class RelationNameType(EnumBase):
    """Enumeration of the relation-name types."""

    NRW = "NRW"
    BRD = "BRD"
    REL = "REL"


class LexicalTagType(EnumBase):
    """Enumeration of the lexical-tag types."""

    ABB = "ABB"
    ABX = "ABX"
    ACR = "ACR"
    ACX = "ACX"
    EPO = "EPO"
    LAB = "LAB"
    NAM = "NAM"
    NON = "NON"
    TRD = "TRD"
    Frelex = "Frelex"


class EntryCombinationType(EnumBase):
    """Enumeration of the entry-combination types."""

    ECIN = "ECIN"
    ECOUT = "ECOUT"


class SupplementalClassType(EnumBase):
    """Enumeration of the supplemental-class types."""

    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"


class DescriptorDefinitionSourceType(EnumBase):
    """ Enumeration of the descriptor definition source types."""

    AIR = "AIR"
    ALT = "ALT"
    AOT = "AOT"
    CCC = "CCC"
    CHV = "CHV"
    CSP = "CSP"
    FMA = "FMA"
    GO = "GO"
    HL7V30 = "HL7V3.0"
    HPO = "HPO"
    ICF = "ICF"
    ICF_CY = "ICF-CY"
    JABL = "JABL"
    LNC = "LNC"
    MCM = "MCM"
    MDR = "MDR"
    MDRCZE = "MDRCZE"
    MDRDUT = "MDRDUT"
    MDRFRE = "MDRFRE"
    MDRGER = "MDRGER"
    MDRHUN = "MDRHUN"
    MDRITA = "MDRITA"
    MDRJPN = "MDRJPN"
    MDRPOR = "MDRPOR"
    MDRSPA = "MDRSPA"
    MEDLINEPLUS = "MEDLINEPLUS"
    MSH = "MSH"
    MSHCZE = "MSHCZE"
    MSHFRE = "MSHFRE"
    MSHNOR = "MSHNOR"
    MSHPOR = "MSHPOR"
    MSHSCR = "MSHSCR"
    MSHSPA = "MSHSPA"
    NANDA_I = "NANDA-I"
    NCI = "NCI"
    NCI_BRIDG = "NCI_BRIDG"
    NCI_BioC = "NCI_BioC"
    NCI_CDISC = "NCI_CDISC"
    NCI_CRCH = "NCI_CRCH"
    NCI_CTCAE = "NCI_CTCAE"
    NCI_CTEP_SDC = "NCI_CTEP-SDC"
    NCI_CareLex = "NCI_CareLex"
    NCI_DICOM = "NCI_DICOM"
    NCI_FDA = "NCI_FDA"
    NCI_GAIA = "NCI_GAIA"
    NCI_KEGG = "NCI_KEGG"
    NCI_NCI_GLOSS = "NCI_NCI-GLOSS"
    NCI_NICHD = "NCI_NICHD"
    NDFRT = "NDFRT"
    NIC = "NIC"
    NOC = "NOC"
    NUCCPT = "NUCCPT"
    OMS = "OMS"
    PDQ = "PDQ"
    PNDS = "PNDS"
    PSY = "PSY"
    SCTSPA = "SCTSPA"
    SNOMEDCT_US = "SNOMEDCT_US"
    SOP = "SOP"
    SPN = "SPN"
    UMD = "UMD"
    UWDA = "UWDA"


class TreeNumber(Base, OrmFightForBase):
    """Table of `<TreeNumber>` element records."""

    # Set table name.
    __tablename__ = "tree_numbers"

    # Autoincrementing primary key ID.
    tree_number_id = sqlalchemy.Column(
        name="tree_number_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<TreeNumber>` element.
    tree_number = sqlalchemy.Column(
        name="tree_number",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # MD5 hash of the tree-number.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `Descriptor` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="Descriptor",
        secondary="mesh.descriptor_tree_numbers",
        back_populates="tree_numbers",
    )

    # Relationship to a list of `Qualifier` records.
    qualifiers = sqlalchemy.orm.relationship(
        argument="Qualifier",
        secondary="mesh.qualifier_tree_numbers",
        back_populates="tree_numbers",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "mesh"
    }

    @sqlalchemy.orm.validates("tree_number")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "tree_number": self.tree_number,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class ThesaurusId(Base, OrmFightForBase):
    """Table of `<ThesaurusID>` element records."""

    # Set table name.
    __tablename__ = "thesaurus_ids"

    # Autoincrementing primary key ID.
    thesaurus_id_id = sqlalchemy.Column(
        name="thesaurus_id_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<ThesaurusID>` element.
    thesaurus_id = sqlalchemy.Column(
        name="thesaurus_id",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # MD5 hash of the tree-number.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `Term` records.
    terms = sqlalchemy.orm.relationship(
        argument="Term",
        secondary="mesh.term_thesaurus_ids",
        back_populates="thesaurus_ids",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "mesh"
    }

    @sqlalchemy.orm.validates("thesaurus_id")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "thesaurus_id": self.thesaurus_id,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Term(Base, OrmFightForBase):
    """Table of `<Term>` element records."""

    # Set table name.
    __tablename__ = "terms"

    # Autoincrementing primary key ID.
    term_id = sqlalchemy.Column(
        name="term_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<ConceptUI>` element.
    ui = sqlalchemy.Column(
        name="ui",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
    )

    # Referring to the `<ConceptName>` element.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the value of the `<DateCreated>` element.
    created = sqlalchemy.Column(
        name="created",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the `<Abbreviation>` element.
    abbreviation = sqlalchemy.Column(
        name="abbreviation",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<SortVersion>` element.
    sort_version = sqlalchemy.Column(
        name="sort_version",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<EntryVersion>` element.
    entry_version = sqlalchemy.Column(
        name="entry_version",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `ThesaurusId` records.
    thesaurus_ids = sqlalchemy.orm.relationship(
        argument="ThesaurusId",
        secondary="mesh.term_thesaurus_ids",
        back_populates="terms",
    )

    # Referring to the `<TermNote>` element.
    note = sqlalchemy.Column(
        name="note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Relationship to a list of `Concept` records.
    concepts = sqlalchemy.orm.relationship(
        argument="Concept",
        secondary="mesh.concept_terms",
        back_populates="terms",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "mesh"
    }


class TermThesaurusId(Base, OrmFightForBase):
    """Associative table between `Term` and `ThesaurusId` records."""

    # Set table name.
    __tablename__ = "term_thesaurus_ids"

    # Autoincrementing primary key ID.
    term_thesaurus_id_id = sqlalchemy.Column(
        name="term_thesaurus_id_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the term ID.
    term_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.terms.term_id"),
        name="term_id",
        nullable=False,
    )

    # Foreign key to the tree-number ID.
    thesaurus_id_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.thesaurus_ids.thesaurus_id_id",
        ),
        name="thesaurus_id_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('term_id', 'thesaurus_id_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class Concept(Base, OrmFightForBase):
    """Table of `<Concept>` element records."""

    # Set table name.
    __tablename__ = "concepts"

    # Autoincrementing primary key ID.
    concept_id = sqlalchemy.Column(
        name="concept_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<ConceptUI>` element.
    ui = sqlalchemy.Column(
        name="ui",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
    )

    # Referring to the `<ConceptName>` element.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the `<CASN1Name>` element.
    casn1_name = sqlalchemy.Column(
        name="casn1_name",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<RegistryNumber>` element.
    registry_number = sqlalchemy.Column(
        name="registry_number",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # Referring to the `<ScopeNote>` element.
    scope_note = sqlalchemy.Column(
        name="scope_note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the `<TranslatorsEnglishScopeNote>` element.
    translators_english_scope_note = sqlalchemy.Column(
        name="translators_english_scope_note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the `<TranslatorsScopeNote>` element.
    translators_scope_note = sqlalchemy.Column(
        name="translators_scope_note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # TODO: RelatedRegistryNumberList (nullable)

    # Relationship to a list of `Term` records.
    terms = sqlalchemy.orm.relationship(
        argument="Term",
        secondary="mesh.concept_terms",
        back_populates="concepts",
    )

    # Relationship to a list of `Qualifier` records.
    qualifiers = sqlalchemy.orm.relationship(
        argument="Qualifier",
        secondary="mesh.qualifier_concepts",
        back_populates="concepts",
    )

    # Relationship to a list of `Descriptor` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="Descriptor",
        secondary="mesh.descriptor_concepts",
        back_populates="concepts",
    )

    # Relationship to a list of `Supplemental` records.
    supplementals = sqlalchemy.orm.relationship(
        argument="Supplemental",
        secondary="mesh.supplemental_concepts",
        back_populates="concepts",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "mesh"
    }


class ConceptRelatedConcept(Base, OrmFightForBase):
    """Associative table between `Concept` and other `Concept` records
    referenced in concept-relation elements."""

    # Set table name.
    __tablename__ = "concept_related_concepts"

    # Autoincrementing primary key ID.
    concept_related_concept_id = sqlalchemy.Column(
        name="concept_related_concept_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    concept_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.concepts.concept_id"),
        name="concept_id",
        nullable=False,
    )

    # Foreign key to the related descriptor ID.
    related_concept_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.concepts.concept_id"),
        name="related_concept_id",
        nullable=False,
    )

    # Referring to the value of the `RelationName` attribute of the
    # `<ConceptRelation>` element casted to a boolean.
    relation_name = sqlalchemy.Column(
        name="relation_name",
        type_=sqlalchemy.types.Enum(RelationNameType),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('concept_id', 'related_concept_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class ConceptTerm(Base, OrmFightForBase):
    """Associative table between `Concept` and `Term` records."""

    # Set table name.
    __tablename__ = "concept_terms"

    # Autoincrementing primary key ID.
    concept_term_id = sqlalchemy.Column(
        name="concept_term_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the concept ID.
    concept_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.concepts.concept_id"),
        name="concept_id",
        nullable=False,
    )

    # Foreign key to the term ID.
    term_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.terms.term_id"),
        name="term_id",
        nullable=False,
    )

    # Referring to the value of the `ConceptPreferredTermYN` attribute of the
    # `<Term>` element casted to a boolean.
    is_concept_preferred_term = sqlalchemy.Column(
        name="is_concept_preferred_term",
        type_=sqlalchemy.types.Boolean(),
        nullable=False,
    )

    # Referring to the value of the `IsPermutedTermYN` attribute of the `<Term>`
    # element casted to a boolean.
    is_permuted_term = sqlalchemy.Column(
        name="is_permuted_term",
        type_=sqlalchemy.types.Boolean(),
        nullable=False,
    )

    # Referring to the value of the `LexicalTag` attribute of the `<Term>`
    # element casted to a boolean.
    lexical_tag = sqlalchemy.Column(
        name="lexical_tag",
        type_=sqlalchemy.types.Enum(LexicalTagType),
        nullable=False,
    )

    # Referring to the value of the `RecordPreferredTermYN` attribute of the
    # `<Term>` element casted to a boolean.
    is_record_preferred_term = sqlalchemy.Column(
        name="is_record_preferred_term",
        type_=sqlalchemy.types.Boolean(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('concept_id', 'term_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class Qualifier(Base, OrmFightForBase):
    """Table of `<QualifierRecord>` element records."""

    # Set table name.
    __tablename__ = "qualifiers"

    # Autoincrementing primary key ID.
    qualifier_id = sqlalchemy.Column(
        name="qualifier_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<QualifierUI>` element.
    ui = sqlalchemy.Column(
        name="ui",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
    )

    # Referring to the `<QualifierName>` element.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the value of the `<DateCreated>` element.
    created = sqlalchemy.Column(
        name="created",
        type_=sqlalchemy.types.Date(),
        nullable=False,
    )

    # Referring to the value of the `<DateRevised>` element.
    revised = sqlalchemy.Column(
        name="revised",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<DateEstablished>` element.
    established = sqlalchemy.Column(
        name="established",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the `<Annotation>` element.
    annotation = sqlalchemy.Column(
        name="annotation",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the `<HistoryNote>` element.
    history_note = sqlalchemy.Column(
        name="history_note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the `<OnlineNote>` element.
    online_note = sqlalchemy.Column(
        name="online_note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Relationship to a list of `TreeNumber` records.
    tree_numbers = sqlalchemy.orm.relationship(
        argument="TreeNumber",
        secondary="mesh.qualifier_tree_numbers",
        back_populates="qualifiers",
    )

    # Relationship to a list of `Concept` records.
    concepts = sqlalchemy.orm.relationship(
        argument="Concept",
        secondary="mesh.qualifier_concepts",
        back_populates="qualifiers",
    )

    # Relationship to a list of `Descriptor` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="Descriptor",
        secondary="mesh.descriptor_allowable_qualifiers",
        back_populates="qualifiers",
    )

    # Relationship to a list of `QualifierSynonym` records.
    synonyms = sqlalchemy.orm.relationship(
        argument="QualifierSynonym",
        back_populates="qualifier",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "mesh"
    }


class QualifierConcept(Base, OrmFightForBase):
    """Associative table between `Qualifier` and `Concept` records."""

    # Set table name.
    __tablename__ = "qualifier_concepts"

    # Autoincrementing primary key ID.
    qualifier_concept_id = sqlalchemy.Column(
        name="qualifier_concept_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the qualifier ID.
    qualifier_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.qualifiers.qualifier_id"),
        name="qualifier_id",
        nullable=False,
    )

    # Foreign key to the concept ID.
    concept_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.concepts.concept_id"),
        name="concept_id",
        nullable=False,
    )

    # Referring to the value of the `PreferredConceptYN` attribute of the
    # `<Concept>` element casted to a boolean.
    is_preferred = sqlalchemy.Column(
        name="is_preferred",
        type_=sqlalchemy.types.Boolean(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('qualifier_id', 'concept_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class QualifierTreeNumber(Base, OrmFightForBase):
    """Associative table between `Qualifier` and `TreeNumber` records."""

    # Set table name.
    __tablename__ = "qualifier_tree_numbers"

    # Autoincrementing primary key ID.
    qualifier_tree_number_id = sqlalchemy.Column(
        name="qualifier_tree_number_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the qualifier ID.
    qualifier_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.qualifiers.qualifier_id"),
        name="qualifier_id",
        nullable=False,
    )

    # Foreign key to the tree-number ID.
    tree_number_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.tree_numbers.tree_number_id",
        ),
        name="tree_number_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('qualifier_id', 'tree_number_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class PreviousIndexing(Base, OrmFightForBase):
    """Table of `<PreviousIndexing>` element records."""

    # Set table name.
    __tablename__ = "previous_indexings"

    # Autoincrementing primary key ID.
    previous_indexing_id = sqlalchemy.Column(
        name="previous_indexing_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<PreviousIndexing>` element.
    previous_indexing = sqlalchemy.Column(
        name="previous_indexing",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Relationship to a list of `Descriptors` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="Descriptor",
        secondary="mesh.descriptor_previous_indexings",
        back_populates="previous_indexings",
    )

    # Relationship to a list of `Supplemental` records.
    supplementals = sqlalchemy.orm.relationship(
        argument="Supplemental",
        secondary="mesh.supplemental_previous_indexings",
        back_populates="previous_indexings",
    )

    # MD5 hash of the tree-number.
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
        "schema": "mesh"
    }

    @sqlalchemy.orm.validates("previous_indexing")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "previous_indexing": self.previous_indexing,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class EntryCombination(Base, OrmFightForBase):
    """Associative table between `Descriptor` and `Qualifier` records denoting
    descriptor-qualifier combinations defined in `<EntryCombination>`,
    `<IndexingInformation>`, and `<HeadingMappedTo>` elements."""

    # Set table name.
    __tablename__ = "entry_combinations"

    # Autoincrementing primary key ID.
    entry_combination_id = sqlalchemy.Column(
        name="entry_combination_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Foreign key to the qualifier ID.
    qualifier_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.qualifiers.qualifier_id"),
        name="qualifier_id",
        nullable=True,
    )

    # Whether this combination was defined under an `<ECIN>` or `<ECOUT>`
    # element. This only applies to `<EntryCombination>` elements.
    combination_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Enum(EntryCombinationType),
        nullable=True,
    )

    # Relationship to a list of `Descriptor` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="Descriptor",
        back_populates="entry_combinations",
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('descriptor_id', 'qualifier_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class Descriptor(Base, OrmFightForBase):
    """Table of `<DescriptorRecord>` element records."""

    # Set table name.
    __tablename__ = "descriptors"

    # Autoincrementing primary key ID.
    descriptor_id = sqlalchemy.Column(
        name="descriptor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `DescriptorClass` attribute of the
    # `<DescriptorRecord>` element.
    descriptor_class = sqlalchemy.Column(
        name="class",
        type_=sqlalchemy.types.Enum(DescriptorClassType),
        nullable=False,
    )

    # Referring to the `<DescriptorUI>` element.
    ui = sqlalchemy.Column(
        name="ui",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
        index=False
    )

    # Referring to the `<DescriptorName>` element.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the value of the `<DateCreated>` element.
    created = sqlalchemy.Column(
        name="created",
        type_=sqlalchemy.types.Date(),
        nullable=False,
    )

    # Referring to the value of the `<DateRevised>` element.
    revised = sqlalchemy.Column(
        name="revised",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<DateEstablished>` element.
    established = sqlalchemy.Column(
        name="established",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Relationship to a list of `Qualifier` records.
    qualifiers = sqlalchemy.orm.relationship(
        argument="Qualifier",
        secondary="mesh.descriptor_allowable_qualifiers",
        back_populates="descriptors",
    )

    # Referring to the `<Annotation>` element.
    annotation = sqlalchemy.Column(
        name="annotation",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the `<HistoryNote>` element.
    history_note = sqlalchemy.Column(
        name="history_note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the `<NLMClassificationNumber>` element.
    nlm_classification_number = sqlalchemy.Column(
        name="nlm_classification_number",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<OnlineNote>` element.
    online_note = sqlalchemy.Column(
        name="online_note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the `<PublicMeSHNote>` element.
    public_mesh_note = sqlalchemy.Column(
        name="public_mesh_note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Relationship to a list of `PreviousIndexing` records.
    previous_indexings = sqlalchemy.orm.relationship(
        argument="PreviousIndexing",
        secondary="mesh.descriptor_previous_indexings",
        back_populates="descriptors",
    )

    # Relationship to a list of `EntryCombination` records.
    entry_combinations = sqlalchemy.orm.relationship(
        argument="EntryCombination",
        secondary="mesh.descriptor_entry_combinations",
        back_populates="descriptors",
    )

    # Referring to the `<ConsiderAlso>` element.
    consider_also = sqlalchemy.Column(
        name="consider_also",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `TreeNumber` records.
    tree_numbers = sqlalchemy.orm.relationship(
        argument="TreeNumber",
        secondary="mesh.descriptor_tree_numbers",
        back_populates="descriptors",
    )

    # Relationship to a list of `Concept` records.
    concepts = sqlalchemy.orm.relationship(
        argument="Concept",
        secondary="mesh.descriptor_concepts",
        back_populates="descriptors",
    )

    # Relationship to a list of `DescriptorSynonym` records.
    synonyms = sqlalchemy.orm.relationship(
        argument="DescriptorSynonym",
        back_populates="descriptor",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "mesh"
    }


class DescriptorEntryCombination(Base, OrmFightForBase):
    """Associative table between `Descriptor` and `EntryCombination` records."""

    # Set table name.
    __tablename__ = "descriptor_entry_combinations"

    # Autoincrementing primary key ID.
    descriptor_entry_combination_id = sqlalchemy.Column(
        name="descriptor_entry_combination_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Foreign key to the entry-combination ID.
    entry_combination_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.entry_combinations.entry_combination_id",
        ),
        name="entry_combination_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('descriptor_id', 'entry_combination_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class DescriptorConcept(Base, OrmFightForBase):
    """Associative table between `Descriptor` and `Concept` records."""

    # Set table name.
    __tablename__ = "descriptor_concepts"

    # Autoincrementing primary key ID.
    descriptor_concept_id = sqlalchemy.Column(
        name="descriptor_concept_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Foreign key to the concept ID.
    concept_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.concepts.concept_id"),
        name="concept_id",
        nullable=False,
    )

    # Referring to the value of the `PreferredConceptYN` attribute of the
    # `<Concept>` element casted to a boolean.
    is_preferred = sqlalchemy.Column(
        name="is_preferred",
        type_=sqlalchemy.types.Boolean(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('descriptor_id', 'concept_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class DescriptorPreviousIndexing(Base, OrmFightForBase):
    """Associative table between `Descriptor` and `PreviousIndexing` records."""

    # Set table name.
    __tablename__ = "descriptor_previous_indexings"

    # Autoincrementing primary key ID.
    descriptor_previous_indexing_id = sqlalchemy.Column(
        name="descriptor_previous_indexing_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Foreign key to the previous-indexing ID.
    previous_indexing_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.previous_indexings.previous_indexing_id",
        ),
        name="previous_indexing_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('descriptor_id', 'previous_indexing_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class DescriptorAllowableQualifier(Base, OrmFightForBase):
    """Associative table between `Descriptor` and `Qualifier` records denoting
    which qualifiers are allowed for a given descriptor."""

    # Set table name.
    __tablename__ = "descriptor_allowable_qualifiers"

    # Autoincrementing primary key ID.
    descriptor_allowable_qualifier_id = sqlalchemy.Column(
        name="descriptor_allowable_qualifier_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Foreign key to the qualifier ID.
    qualifier_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.qualifiers.qualifier_id"),
        name="qualifier_id",
        nullable=False,
    )

    # Referring to the `<Abbreviation>` element.
    abbreviation = sqlalchemy.Column(
        name="abbreviation",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('descriptor_id', 'qualifier_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class DescriptorTreeNumber(Base, OrmFightForBase):
    """Associative table between `Descriptor` and `TreeNumber` records."""

    # Set table name.
    __tablename__ = "descriptor_tree_numbers"

    # Autoincrementing primary key ID.
    descriptor_tree_number_id = sqlalchemy.Column(
        name="descriptor_tree_number_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Foreign key to the tree-number ID.
    tree_number_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.tree_numbers.tree_number_id",
        ),
        name="tree_number_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('descriptor_id', 'tree_number_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class DescriptorPharmacologicalActionDescriptor(Base, OrmFightForBase):
    """Associative table between `Descriptor` and other `Descriptor` records
    referenced in pharmacological-actions."""

    # Set table name.
    __tablename__ = "descriptor_pharmacological_action_descriptors"

    # Autoincrementing primary key ID.
    descriptor_pharmacological_action_descriptor_id = sqlalchemy.Column(
        name="descriptor_pharmacological_action_descriptor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Foreign key to the pharmacological-action-referenced descriptor ID.
    pharmacological_action_descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="pharmacological_action_descriptor_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint(
            'descriptor_id',
            'pharmacological_action_descriptor_id',
        ),
        # Set table schema.
        {"schema": "mesh"}
    )


class DescriptorRelatedDescriptor(Base, OrmFightForBase):
    """Associative table between `Descriptor` and other `Descriptor` records
    referenced in see-related elements."""

    # Set table name.
    __tablename__ = "descriptor_related_descriptors"

    # Autoincrementing primary key ID.
    descriptor_related_descriptor_id = sqlalchemy.Column(
        name="descriptor_related_descriptor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # Foreign key to the related descriptor ID.
    related_descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="related_descriptor_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('descriptor_id', 'related_descriptor_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class Source(Base, OrmFightForBase):
    """Table of `<Source>` element records."""

    # Set table name.
    __tablename__ = "sources"

    # Autoincrementing primary key ID.
    source_id = sqlalchemy.Column(
        name="source_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<Source>` element.
    source = sqlalchemy.Column(
        name="source",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # MD5 hash of the tree-number.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `Supplemental` records.
    supplementals = sqlalchemy.orm.relationship(
        argument="Supplemental",
        secondary="mesh.supplemental_sources",
        back_populates="sources",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "mesh"
    }

    @sqlalchemy.orm.validates("source")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "source": self.source,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Supplemental(Base, OrmFightForBase):
    """Table of `<SupplementalRecord>` element records."""

    # Set table name.
    __tablename__ = "supplementals"

    # Autoincrementing primary key ID.
    supplemental_id = sqlalchemy.Column(
        name="supplemental_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `SCRClass` attribute of the
    # `<SupplementalRecord>` element.
    supplemental_class = sqlalchemy.Column(
        name="class",
        type_=sqlalchemy.types.Enum(SupplementalClassType),
        nullable=False,
    )

    # Referring to the `<SupplementalRecordUI>` element.
    ui = sqlalchemy.Column(
        name="ui",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
        index=False
    )

    # Referring to the `<SupplementalRecordName>` element.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the value of the `<DateCreated>` element.
    created = sqlalchemy.Column(
        name="created",
        type_=sqlalchemy.types.Date(),
        nullable=False,
    )

    # Referring to the value of the `<DateRevised>` element.
    revised = sqlalchemy.Column(
        name="revised",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the `<Note>` element.
    note = sqlalchemy.Column(
        name="note",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the `<Frequency>` element.
    frequency = sqlalchemy.Column(
        name="frequency",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `PreviousIndexing` records.
    previous_indexings = sqlalchemy.orm.relationship(
        argument="PreviousIndexing",
        secondary="mesh.supplemental_previous_indexings",
        back_populates="supplementals",
    )

    # Relationship to a list of `EntryCombination` records defined via
    # `<HeadingMappedTo>` elements.
    heading_mapped_tos = sqlalchemy.orm.relationship(
        argument="EntryCombination",
        secondary="mesh.supplemental_heading_mapped_tos",
    )

    # Relationship to a list of `EntryCombination` records defined via
    # `<IndexingInformation>` elements.
    indexing_informations = sqlalchemy.orm.relationship(
        argument="EntryCombination",
        secondary="mesh.supplemental_indexing_informations",
    )

    # Relationship to a list of `Source` records.
    sources = sqlalchemy.orm.relationship(
        argument="Source",
        secondary="mesh.supplemental_sources",
        back_populates="supplementals",
    )

    # Relationship to a list of `Concept` records.
    concepts = sqlalchemy.orm.relationship(
        argument="Concept",
        secondary="mesh.supplemental_concepts",
        back_populates="supplementals",
    )

    # Relationship to a list of `SupplementalSynonym` records.
    synonyms = sqlalchemy.orm.relationship(
        argument="SupplementalSynonym",
        back_populates="supplemental",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "mesh"
    }


class SupplementalHeadingMappedTo(Base, OrmFightForBase):
    """Associative table between `Descriptor` and `EntryCombination` records
    via `<HeadingMappedTo>` elements."""

    # Set table name.
    __tablename__ = "supplemental_heading_mapped_tos"

    # Autoincrementing primary key ID.
    supplemental_heading_mapped_to_id = sqlalchemy.Column(
        name="supplemental_heading_mapped_to_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the supplemental ID.
    supplemental_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.supplementals.supplemental_id"),
        name="supplemental_id",
        nullable=False,
    )

    # Foreign key to the entry-combination ID.
    entry_combination_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.entry_combinations.entry_combination_id",
        ),
        name="entry_combination_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('supplemental_id', 'entry_combination_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class SupplementalIndexingInformation(Base, OrmFightForBase):
    """Associative table between `Descriptor` and `EntryCombination` records
    via `<IndexingInformation>` elements."""

    # Set table name.
    __tablename__ = "supplemental_indexing_informations"

    # Autoincrementing primary key ID.
    supplemental_indexing_information_id = sqlalchemy.Column(
        name="supplemental_indexing_information_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the supplemental ID.
    supplemental_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.supplementals.supplemental_id"),
        name="supplemental_id",
        nullable=False,
    )

    # Foreign key to the entry-combination ID.
    entry_combination_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.entry_combinations.entry_combination_id",
        ),
        name="entry_combination_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('supplemental_id', 'entry_combination_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class SupplementalConcept(Base, OrmFightForBase):
    """Associative table between `Supplemental` and `Concept` records."""

    # Set table name.
    __tablename__ = "supplemental_concepts"

    # Autoincrementing primary key ID.
    supplemental_concept_id = sqlalchemy.Column(
        name="supplemental_concept_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the supplemental ID.
    supplemental_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.supplementals.supplemental_id"),
        name="supplemental_id",
        nullable=False,
    )

    # Foreign key to the concept ID.
    concept_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.concepts.concept_id"),
        name="concept_id",
        nullable=False,
    )

    # Referring to the value of the `PreferredConceptYN` attribute of the
    # `<Concept>` element casted to a boolean.
    is_preferred = sqlalchemy.Column(
        name="is_preferred",
        type_=sqlalchemy.types.Boolean(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('supplemental_id', 'concept_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class SupplementalPreviousIndexing(Base, OrmFightForBase):
    """Associative table between `Supplemental` and `PreviousIndexing`
    records."""

    # Set table name.
    __tablename__ = "supplemental_previous_indexings"

    # Autoincrementing primary key ID.
    supplemental_previous_indexing_id = sqlalchemy.Column(
        name="supplemental_previous_indexing_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the supplemental ID.
    supplemental_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.supplementals.supplemental_id"),
        name="supplemental_id",
        nullable=False,
    )

    # Foreign key to the previous-indexing ID.
    previous_indexing_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.previous_indexings.previous_indexing_id",
        ),
        name="previous_indexing_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('supplemental_id', 'previous_indexing_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class SupplementalPharmacologicalActionDescriptor(Base, OrmFightForBase):
    """Associative table between `Supplemental` and `Descriptor` records
    referenced in pharmacological-actions."""

    # Set table name.
    __tablename__ = "supplemental_pharmacological_action_descriptors"

    # Autoincrementing primary key ID.
    supplemental_pharmacological_action_descriptor_id = sqlalchemy.Column(
        name="supplemental_pharmacological_action_descriptor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the supplemental ID.
    supplemental_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.supplementals.supplemental_id"),
        name="supplemental_id",
        nullable=False,
    )

    # Foreign key to the pharmacological-action-referenced descriptor ID.
    pharmacological_action_descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="pharmacological_action_descriptor_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint(
            'supplemental_id',
            'pharmacological_action_descriptor_id',
        ),
        # Set table schema.
        {"schema": "mesh"}
    )


class SupplementalSource(Base, OrmFightForBase):
    """Associative table between `Supplemental` and `Source` records."""

    # Set table name.
    __tablename__ = "supplemental_sources"

    # Autoincrementing primary key ID.
    supplemental_source_id = sqlalchemy.Column(
        name="supplemental_source_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the supplemental ID.
    supplemental_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.supplementals.supplemental_id"),
        name="supplemental_id",
        nullable=False,
    )

    # Foreign key to the source ID.
    source_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "mesh.sources.source_id",
        ),
        name="source_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('supplemental_id', 'source_id'),
        # Set table schema.
        {"schema": "mesh"}
    )


class DescriptorSynonym(Base, OrmFightForBase):
    """Table of MeSH descriptor synonyms as defined in the UMLS."""

    # Set table name.
    __tablename__ = "descriptor_synonyms"

    # Autoincrementing primary key ID.
    descriptor_synonym_id = sqlalchemy.Column(
        name="descriptor_synonym_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
    )

    # The descriptor synonym.
    synonym = sqlalchemy.Column(
        name="synonym",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # MD5 hash of the synonym.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        index=True,
        nullable=False,
    )

    # Relationship to a `Descriptor` record.
    descriptor = sqlalchemy.orm.relationship(
        argument="Descriptor",
        back_populates="synonyms",
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('descriptor_id', 'md5'),
        # Add a pg_trgm trigram index on the `synonym` field.
        sqlalchemy.Index(
            'ix_mesh_descriptor_synonyms_synonym_trgm',
            sqlalchemy.text("synonym gin_trgm_ops"),
            postgresql_using='gin',
            postgresql_ops={"description": "gin_trgm_ops"},
        ),
        # Set table schema.
        {"schema": "mesh"}
    )

    @sqlalchemy.orm.validates("synonym")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "synonym": self.synonym,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class QualifierSynonym(Base, OrmFightForBase):
    """Table of MeSH qualifier synonyms as defined in the UMLS."""

    # Set table name.
    __tablename__ = "qualifier_synonyms"

    # Autoincrementing primary key ID.
    qualifier_synonym_id = sqlalchemy.Column(
        name="qualifier_synonym_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the qualifier ID.
    qualifier_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.qualifiers.qualifier_id"),
        name="qualifier_id",
        nullable=False,
    )

    # The descriptor synonym.
    synonym = sqlalchemy.Column(
        name="synonym",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # MD5 hash of the synonym.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        index=True,
        nullable=False,
    )

    # Relationship to a `Qualifier` record.
    qualifier = sqlalchemy.orm.relationship(
        argument="Qualifier",
        back_populates="synonyms",
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('qualifier_id', 'md5'),
        # Add a pg_trgm trigram index on the `synonym` field.
        sqlalchemy.Index(
            'ix_mesh_qualifier_synonyms_synonym_trgm',
            sqlalchemy.text("synonym gin_trgm_ops"),
            postgresql_using='gin',
            postgresql_ops={"description": "gin_trgm_ops"},
        ),
        # Set table schema.
        {"schema": "mesh"}
    )

    @sqlalchemy.orm.validates("synonym")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "synonym": self.synonym,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class SupplementalSynonym(Base, OrmFightForBase):
    """Table of MeSH supplemental synonyms as defined in the UMLS."""

    # Set table name.
    __tablename__ = "supplemental_synonyms"

    # Autoincrementing primary key ID.
    supplemental_synonym_id = sqlalchemy.Column(
        name="supplemental_synonym_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the concept ID.
    supplemental_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.supplementals.supplemental_id"),
        name="supplemental_id",
        nullable=False,
    )

    # The descriptor synonym.
    synonym = sqlalchemy.Column(
        name="synonym",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # MD5 hash of the synonym.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        index=True,
        nullable=False,
    )

    # Relationship to a `Supplemental` record.
    supplemental = sqlalchemy.orm.relationship(
        argument="Supplemental",
        back_populates="synonyms",
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('supplemental_id', 'md5'),
        # Add a pg_trgm trigram index on the `synonym` field.
        sqlalchemy.Index(
            'ix_mesh_supplemental_synonyms_synonym_trgm',
            sqlalchemy.text("synonym gin_trgm_ops"),
            postgresql_using='gin',
            postgresql_ops={"description": "gin_trgm_ops"},
        ),
        # Set table schema.
        {"schema": "mesh"}
    )

    @sqlalchemy.orm.validates("synonym")
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "synonym": self.synonym,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class DescriptorDefinition(Base, OrmFightForBase):
    """Table of MeSH descriptor definitions as defined in the UMLS."""

    # Set table name.
    __tablename__ = "descriptor_definitions"

    # Autoincrementing primary key ID.
    descriptor_definition_id = sqlalchemy.Column(
        name="descriptor_definition_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the descriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
        index=True,
    )

    source = sqlalchemy.Column(
        name="source",
        type_=sqlalchemy.types.Enum(DescriptorDefinitionSourceType),
        nullable=False,
        index=True,
    )

    # The descriptor synonym.
    definition = sqlalchemy.Column(
        name="definition",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint(
            'descriptor_id',
            'source',
        ),
        # Set table schema.
        {"schema": "mesh"}
    )
