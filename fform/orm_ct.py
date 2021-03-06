# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sqlalchemy.orm
from geoalchemy2 import Geometry

from fform.orm_base import Base
from fform.orm_base import OrmFightForBase
from fform.utils import EnumBase


class ActualType(EnumBase):
    """ Enumeration of the actual types."""

    ACTUAL = "Actual"
    ANTICIPATED = "Anticipated"
    ESTIMATE = "Estimate"


class YesNoType(EnumBase):
    """ Enumeration of the yes/no types."""

    YES = "Yes"
    NO = "No"


class RecruitmentStatusType(EnumBase):
    """ Enumeration of the recruitment-status types/"""

    ACTIVE_NOT = "Active, not recruiting"
    COMPLETED = "Completed"
    INVITATION = "Enrolling by invitation"
    NOT_YET = "Not yet recruiting"
    RECRUITING = "Recruiting"
    SUSPENDED = "Suspended"
    TERMINATED = "Terminated"
    WITHDRAWN = "Withdrawn"


class AgencyClassType(EnumBase):
    """ Enumeration of the agency-class types."""

    NIH = "NIH"
    US = "U.S. Fed"
    INDUSTRY = "Industry"
    OTHER = "Other"


class InterventionType(EnumBase):
    """ Enumeration of the intervention types."""

    BEHAVIORAL = "Behavioral"
    BIOLOGICAL = "Biological"
    COMBINATION = "Combination Product"
    DEVICE = "Device"
    DIAGNOSTIC = "Diagnostic Test"
    DIETARY = "Dietary Supplement"
    DRUG = "Drug"
    GENETIC = "Genetic"
    PROCEDURE = "Procedure"
    RADIATION = "Radiation"
    OTHER = "Other"


class SamplingMethodType(EnumBase):
    """ Enumeration of the sampling-method types."""

    PROBABILITY = "Probability Sample"
    NON_PROBABILITY = "Non-Probability Sample"


class GenderType(EnumBase):
    """ Enumeration of the gender types."""

    FEMALE = "Female"
    MALE = "Male"
    ALL = "All"


class RoleType(EnumBase):
    """ Enumeration of the role types."""

    PRINCIPAL = "Principal Investigator"
    SUB = "Sub-Investigator"
    CHAIR = "Study Chair"
    DIRECTOR = "Study Director"


class ResponsiblePartyType(EnumBase):
    """ Enumeration of the responsible-party types."""

    SPONSOR = "Sponsor"
    PRINCIPAL = "Principal Investigator"
    SPONSOR_INVESTIGATOR = "Sponsor-Investigator"


class MeasureParameterType(EnumBase):
    """ Enumeration of the measure-parameter types."""

    GEOMETRIC = "Geometric Mean"
    GLS_MEAN = "Geometric Least Squares Mean"
    LS_MEAN = "Least Squares Mean"
    LOG_MEAN = "Log Mean"
    MEAN = "Mean"
    MEDIAN = "Median"
    NUMBER = "Number"
    PARTICIPANTS = "Count of Participants"
    UNITS = "Count of Units"


class MeasureDispersionType(EnumBase):
    """ Enumeration of the measure-dispersion types."""

    CI_80 = "80% Confidence Interval"
    CI_90 = "90% Confidence Interval"
    CI_95 = "95% Confidence Interval"
    CI_97 = "97.5% Confidence Interval"
    CI_99 = "99% Confidence Interval"
    FULL_RANGE = "Full Range"
    GCV = "Geometric Coefficient of Variation"
    IQR = "Inter-Quartile Range"
    SD = "Standard Deviation"
    SE = "Standard Error"


class NonInferiorityType(EnumBase):
    """ Enumeration of the non-inferiority types."""

    SUPERIORITY = "Superiority"
    NON_INFERIORITY = "Non-Inferiority"
    EQUIVALENCE = "Equivalence"
    OTHER = "Other"


class NumSidesType(EnumBase):
    """ Enumeration of the number of sides."""

    ONE = "1-Sided"
    TWO = "2-Sided"


class AnalysisDispersionType(EnumBase):
    """ Enumeration of the analysis-dispersion types."""

    SD = "Standard Deviation"
    SEM = "Standard Error of the Mean"


class OutcomeType(EnumBase):
    """ Enumeration of the outcome types."""

    PRIMARY = "Primary"
    SECONDARY = "Secondary"
    POST_HOC = "Post-Hoc"
    OTHER = "Other Pre-specified"


class EventAssessmentType(EnumBase):
    """ Enumeration of the event-assessment types."""

    SYSTEMATIC = "Systematic Assessment"
    NON_SYSTEMATIC = "Non-systematic Assessment"


class PiEmployeeType(EnumBase):
    """ Enumeration of the pi-employee types."""

    ARE_EMPLOYED = ("All Principal Investigators ARE employed by the "
                    "organization sponsoring the study.")
    NOT_EMPLOYED = ("Principal Investigators are NOT employed by the "
                    "organization sponsoring the study.")


class ExpandedAccessStatusType(EnumBase):
    """ Enumeration of the expanded-access-status types."""

    AVAILABLE = "Available"
    UNAVAILABLE = "No longer available"
    TEMP_UNAVAILABLE = "Temporarily not available"
    APPROVED = "Approved for marketing"


class RedactedRecordStatusType(EnumBase):
    """ Enumeration of the redacted-record-status types."""

    WITHHELD = "Withheld"


class UnknownStatusType(EnumBase):
    """ Enumeration of the unknown-status types."""

    UNKNOWN = "Unknown status"


class OverallStatusType(EnumBase):
    """ Enumeration of the overall-status types."""

    ACTIVE_NOT = "Active, not recruiting"
    COMPLETED = "Completed"
    INVITATION = "Enrolling by invitation"
    NOT_YET = "Not yet recruiting"
    RECRUITING = "Recruiting"
    SUSPENDED = "Suspended"
    TERMINATED = "Terminated"
    WITHDRAWN = "Withdrawn"
    AVAILABLE = "Available"
    UNAVAILABLE = "No longer available"
    TEMP_UNAVAILABLE = "Temporarily not available"
    APPROVED = "Approved for marketing"
    WITHHELD = "Withheld"
    UNKNOWN = "Unknown status"


class StudyType(EnumBase):
    """ Enumeration of the study types."""

    EXPANDED = "Expanded Access"
    INTERVENTIONAL = "Interventional"
    NA = "N/A"
    OBSERVATIONAL = "Observational"
    OBSERVATIONAL_PR = "Observational [Patient Registry]"


class PhaseType(EnumBase):
    """ Enumeration of the phase types."""

    NA = "N/A"
    PHASE_1_EARLY = "Early Phase 1"
    PHASE_1 = "Phase 1"
    PHASE_1_2 = "Phase 1/Phase 2"
    PHASE_2 = "Phase 2"
    PHASE_2_3 = "Phase 2/Phase 3"
    PHASE_3 = "Phase 3"
    PHASE_4 = "Phase 4"


class BiospecRetentionType(EnumBase):
    """ Enumeration of the biospec-retention types."""

    NONE = "None Retained"
    SAMPLES_W_DNA = "Samples With DNA"
    SAMPLES_WO_DNA = "Samples Without DNA"


class SponsorType(EnumBase):
    """ Enumeration of the sponsor types."""

    LEAD = "lead_sponsor"
    COLLABORATOR = "collaborator"


class InvestigatorType(EnumBase):
    """ Enumeration of the investigator types."""

    LOCATION = "location"
    OVERALL = "overall"


class ReferenceType(EnumBase):
    """ Enumeration of the reference types."""

    STANDARD = "Standard"
    RESULTS = "Results"


class MeshTermType(EnumBase):
    """ Enumeration of the mesh-term types."""

    CONDITION = "Condition"
    INTERVENTION = "Intervention"


class Sponsor(Base, OrmFightForBase):
    """ Table of `<sponsor>` element record."""

    # Set table name.
    __tablename__ = "sponsors"

    # Autoincrementing primary key ID.
    sponsor_id = sqlalchemy.Column(
        name="sponsor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Agency (value of the `<agency>` element).
    agency = sqlalchemy.Column(
        name="agency",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Agency class (value of the `<agency_class>` element).
    agency_class = sqlalchemy.Column(
        name="class",
        type_=sqlalchemy.types.Enum(AgencyClassType),
        nullable=True,
        default=None,
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

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_sponsors",
        back_populates="sponsors",
        uselist=True,
    )

    # Relationship to a list of `StudySponsor` records.
    study_sponsors = sqlalchemy.orm.relationship(
        argument="StudySponsor",
        back_populates="sponsor",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates(
        "agency",
        "agency_class",
    )
    def update_md5(self, key, value):

        # Assemble the class attributes into a `dict`.
        attrs = {
            "agency": self.agency,
            "agency_class": self.agency_class,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Keyword(Base, OrmFightForBase):
    """ Table of `<keyword>` element records."""

    # Set table name.
    __tablename__ = "keywords"

    # Autoincrementing primary key ID.
    keyword_id = sqlalchemy.Column(
        name="keyword_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Keyword name (value of the `<keyword>` element).
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

    # Relationship to a list of `StudyKeyword` records.
    study_keywords = sqlalchemy.orm.relationship(
        argument="StudyKeyword",
        back_populates="keyword",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_keywords",
        back_populates="keywords",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates("keyword")
    def update_md5(self, key, value):

        # Enforce lowercasing of the value in order to avoid needless
        # duplication when the keyword is provided with different casing.
        value = value.lower() if value else None

        # Assemble the class attributes into a `dict`.
        attrs = {
            "keyword": self.keyword,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Condition(Base, OrmFightForBase):
    """ Table of `<condition>` element records."""

    # Set table name.
    __tablename__ = "conditions"

    # Autoincrementing primary key ID.
    condition_id = sqlalchemy.Column(
        name="condition_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Condition name (value of the `<condition>` element).
    condition = sqlalchemy.Column(
        name="condition",
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

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_conditions",
        back_populates="conditions"
    )

    # Relationship to a list of `StudyCondition` records.
    study_conditions = sqlalchemy.orm.relationship(
        argument="StudyCondition",
        back_populates="condition",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates("condition")
    def update_md5(self, key, value):

        # Enforce lowercasing of the value in order to avoid needless
        # duplication when the keyword is provided with different casing.
        value = value.lower() if value else None

        # Assemble the class attributes into a `dict`.
        attrs = {
            "condition": self.condition,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Facility(Base, OrmFightForBase):
    """ Table of `<facility>` elements and their underlying `<address>` element
        records.
    """

    # Set table name.
    __tablename__ = "facilities"

    # Autoincrementing primary key ID.
    facility_id = sqlalchemy.Column(
        name="facility_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the canonical facility ID.
    facility_canonical_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "clinicaltrials.facilities_canonical.facility_canonical_id",
        ),
        name="facility_canonical_id",
        nullable=True,
    )

    # Facility name (referring to the `<name>` element).
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Facility city (referring to the `<city>` element under the `<address>`
    # element).
    city = sqlalchemy.Column(
        name="city",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # Facility state (referring to the `<city>` element under the `<address>`
    # element).
    state = sqlalchemy.Column(
        name="state",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # Facility zip-code (referring to the `<zip>` element under the `<address>`
    # element).
    zip_code = sqlalchemy.Column(
        name="zip_code",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Facility country (referring to the `<country>` element under the
    # `<address>` element).
    country = sqlalchemy.Column(
        name="country",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # MD5 hash of the author's full name.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a `Location` record.
    locations = sqlalchemy.orm.relationship(
        argument="Location",
        back_populates="facility",
        uselist=True,
    )

    # Relationship to a `FacilityCanonical` record.
    facility_canonical = sqlalchemy.orm.relationship(
        argument="FacilityCanonical",
        back_populates="facility",
    )

    # Relationship to a list of `StudyFacility` records.
    study_facilities = sqlalchemy.orm.relationship(
        argument="StudyFacility",
        back_populates="facility",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_facilities",
        back_populates="facilities",
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates(
        "name",
        "city",
        "state",
        "zip_code",
        "country",
    )
    def update_md5(self, key, value):
        # Assemble the class attributes into a `dict`.
        attrs = {
            "name": self.name,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "country": self.country,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Person(Base, OrmFightForBase):
    """ Table of person records normalized out of `<contact>` and
        `<investigator> element records.
    """

    # Set table name.
    __tablename__ = "persons"

    # Autoincrementing primary key ID.
    person_id = sqlalchemy.Column(
        name="person_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Person first name (referring to the `<first_name>` element).
    name_first = sqlalchemy.Column(
        name="name_first",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Person middle name (referring to the `<middle_name>` element).
    name_middle = sqlalchemy.Column(
        name="name_middle",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Person last name (referring to the `<last_name>` element).
    name_last = sqlalchemy.Column(
        name="name_last",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Contact degrees (referring to the `<degrees>` element).
    degrees = sqlalchemy.Column(
        name="degrees",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # MD5 hash of the contact's full name.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `Contacts` record.
    contacts = sqlalchemy.orm.relationship(
        argument="Contact",
        back_populates="person",
        uselist=True,
    )

    # Relationship to a list of `Investigator` record.
    investigators = sqlalchemy.orm.relationship(
        argument="Investigator",
        back_populates="person",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates(
        "name_first",
        "name_middle",
        "name_last",
        "degrees",
    )
    def update_md5(self, key, value):
        # Assemble the class attributes into a `dict`.
        attrs = {
            "name_first": self.name_first,
            "name_middle": self.name_middle,
            "name_last": self.name_last,
            "degrees": self.degrees,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Contact(Base, OrmFightForBase):
    """ Table of `<contact>` elements records."""

    # Set table name.
    __tablename__ = "contacts"

    # Autoincrementing primary key ID.
    contact_id = sqlalchemy.Column(
        name="contact_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the person ID.
    person_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.persons.person_id"),
        name="person_id",
        nullable=False,
    )

    # Contact phone number (referring to the `<phone>` element).
    phone = sqlalchemy.Column(
        name="phone",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Contact phone number extension (referring to the `<phone_ext>` element).
    phone_ext = sqlalchemy.Column(
        name="phone_ext",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Contact email (referring to the `<email>` element).
    email = sqlalchemy.Column(
        name="email",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # MD5 hash of the contact's full name.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a `Person` record.
    person = sqlalchemy.orm.relationship(
        argument="Person",
        back_populates="contacts",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates(
        "person_id",
        "phone",
        "phone_ext",
        "email",
    )
    def update_md5(self, key, value):

        # Enforce lowercasing of the email value in order to avoid needless
        # duplication when the keyword is provided with different casing.
        if key == "email":
            value = value.lower() if value else None

        attrs = {
            "person_id": self.person_id,
            "phone": self.phone,
            "phone_ext": self.phone_ext,
            "email": self.email,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Investigator(Base, OrmFightForBase):
    """ Table of `<investigator>` elements records."""

    # Set table name.
    __tablename__ = "investigators"

    # Autoincrementing primary key ID.
    investigator_id = sqlalchemy.Column(
        name="investigator_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the person ID.
    person_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.persons.person_id"),
        name="person_id",
        nullable=False,
    )

    # Investigator role (referring to the `<role>` element).
    role = sqlalchemy.Column(
        name="role",
        type_=sqlalchemy.types.Enum(RoleType),
        nullable=True,
        index=True,
    )

    # Investigator affiliation (referring to the `<affiliation>` element).
    affiliation = sqlalchemy.Column(
        name="affiliation",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # MD5 hash of the contact's full name.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a `Person` record.
    person = sqlalchemy.orm.relationship(
        argument="Person",
        back_populates="investigators",
        uselist=False,
    )

    # Relationship to a list of `Location` records.
    locations = sqlalchemy.orm.relationship(
        argument="Location",
        secondary="clinicaltrials.location_investigators",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_investigators",
        back_populates="investigators",
        uselist=True,
    )

    # Relationship to a list of `StudyInvestigator` records.
    study_investigators = sqlalchemy.orm.relationship(
        argument="StudyInvestigator",
        back_populates="investigator",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates(
        "person_id",
        "role",
        "affiliation",
    )
    def update_md5(self, key, value):
        # Assemble the class attributes into a `dict`.
        attrs = {
            "person_id": self.person_id,
            "role": self.role,
            "affiliation": self.affiliation,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Location(Base, OrmFightForBase):
    """ Table of `<location>` elements records."""

    # Set table name.
    __tablename__ = "locations"

    # Autoincrementing primary key ID.
    location_id = sqlalchemy.Column(
        name="location_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the facility ID.
    facility_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.facilities.facility_id"),
        name="facility_id",
        nullable=True,
    )

    # Recruitment status (defined by the name of the element of `<status>`
    # type).
    status = sqlalchemy.Column(
        name="status",
        type_=sqlalchemy.types.Enum(RecruitmentStatusType),
        nullable=True,
        index=True,
    )

    # Foreign key to the primary contact ID.
    contact_primary_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.contacts.contact_id"),
        name="contact_primary_id",
        nullable=True,
    )

    # Foreign key to the backup contact ID.
    contact_backup_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.contacts.contact_id"),
        name="contact_backup_id",
        nullable=True,
    )

    # MD5 hash of the location's keys.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a `Facility` record.
    facility = sqlalchemy.orm.relationship(
        argument="Facility",
        foreign_keys=facility_id,
        back_populates="locations",
        uselist=False,
    )

    # Relationship to a `Contact` record for the primary contact.
    contact_primary = sqlalchemy.orm.relationship(
        argument="Contact",
        foreign_keys=contact_primary_id,
        uselist=False,
    )

    # Relationship to a `Contact` record for the backup contact.
    contact_backup = sqlalchemy.orm.relationship(
        argument="Contact",
        foreign_keys=contact_backup_id,
        uselist=False,
    )

    # Relationship to a list of `Investigator` records.
    investigators = sqlalchemy.orm.relationship(
        argument="Investigator",
        secondary="clinicaltrials.location_investigators",
        uselist=True,
    )

    # Relationship to a list of `StudyLocation` records.
    study_locations = sqlalchemy.orm.relationship(
        argument="StudyLocation",
        back_populates="location",
        uselist=True,
    )

    # Relationship to a list of `Studies` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_locations",
        back_populates="locations",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = (
        # Set table schema.
        {"schema": "clinicaltrials"},
    )

    @sqlalchemy.orm.validates(
        "facility_id",
        "contact_primary_id",
        "contact_backup_id",
    )
    def update_md5(self, key, value):

        attrs = {
            "facility_id": self.facility_id,
            "contact_primary_id": self.contact_primary_id,
            "contact_backup_id": self.contact_backup_id,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class LocationInvestigator(Base, OrmFightForBase):
    """ Associative table between `Location` and `Investigator` records."""

    # Set table name.
    __tablename__ = "location_investigators"

    # Autoincrementing primary key ID.
    location_investigator_id = sqlalchemy.Column(
        name="location_investigator_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the location ID.
    location_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.locations.location_id"),
        name="location_id",
        nullable=False,
    )

    # Foreign key to the investigator ID.
    investigator_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.investigators.investigator_id"),
        name="investigator_id",
        nullable=False,
    )

    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('location_id', 'investigator_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class OversightInfo(Base, OrmFightForBase):
    """ Table of `<oversight_info>` elements records."""

    # Set table name.
    __tablename__ = "oversight_infos"

    # Autoincrementing primary key ID.
    oversight_info_id = sqlalchemy.Column(
        name="oversight_info_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<has_dmc>` element.
    has_dmc = sqlalchemy.Column(
        name="has_dmc",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Referring to the `<is_fda_regulated_drug>` element.
    is_fda_regulated_drug = sqlalchemy.Column(
        name="is_fda_regulated_drug",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Referring to the `<is_fda_regulated_device>` element.
    is_fda_regulated_device = sqlalchemy.Column(
        name="is_fda_regulated_device",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Referring to the `<is_unapproved_device>` element.
    is_unapproved_device = sqlalchemy.Column(
        name="is_unapproved_device",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Referring to the `<is_ppsd>` element.
    is_ppsd = sqlalchemy.Column(
        name="is_ppsd",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Referring to the `<is_us_export>` element.
    is_us_export = sqlalchemy.Column(
        name="is_us_export",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="oversight_info",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class ExpandedAccessInfo(Base, OrmFightForBase):
    """ Table of `<expanded_access_info>` elements records."""

    # Set table name.
    __tablename__ = "expanded_access_infos"

    # Autoincrementing primary key ID.
    expanded_access_info_id = sqlalchemy.Column(
        name="expanded_access_info_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<expanded_access_type_individual>` element.
    expanded_access_type_individual = sqlalchemy.Column(
        name="individual",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Referring to the `<expanded_access_type_intermediate>` element.
    expanded_access_type_intermediate = sqlalchemy.Column(
        name="intermediate",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Referring to the `<expanded_access_type_treatment>` element.
    expanded_access_type_treatment = sqlalchemy.Column(
        name="treatment",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="expanded_access_info",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class StudyDesignInfo(Base, OrmFightForBase):
    """ Table of `<study_design_info>` elements records."""

    # Set table name.
    __tablename__ = "study_design_infos"

    # Autoincrementing primary key ID.
    study_design_info_id = sqlalchemy.Column(
        name="study_design_info_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<allocation>` element.
    allocation = sqlalchemy.Column(
        name="allocation",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<intervention_model>` element.
    intervention_model = sqlalchemy.Column(
        name="intervention_model",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<intervention_model_description>` element.
    intervention_model_description = sqlalchemy.Column(
        name="intervention_model_description",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<primary_purpose>` element.
    primary_purpose = sqlalchemy.Column(
        name="primary_purpose",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<observational_model>` element.
    observational_model = sqlalchemy.Column(
        name="observational_model",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<time_perspective>` element.
    time_perspective = sqlalchemy.Column(
        name="time_perspective",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<masking>` element.
    masking = sqlalchemy.Column(
        name="masking",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<masking_description>` element.
    masking_description = sqlalchemy.Column(
        name="masking_description",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_design_info",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class ProtocolOutcome(Base, OrmFightForBase):
    """ Table of `<protocol_outcome>` elements records."""

    # Set table name.
    __tablename__ = "protocol_outcomes"

    # Autoincrementing primary key ID.
    protocol_outcome_id = sqlalchemy.Column(
        name="protocol_outcome_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the `<measure>` element.
    measure = sqlalchemy.Column(
        name="measure",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the `<time_frame>` element.
    time_frame = sqlalchemy.Column(
        name="time_frame",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the `<description>` element.
    description = sqlalchemy.Column(
        name="description",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `StudyOutcome` records.
    study_outcomes = sqlalchemy.orm.relationship(
        argument="StudyOutcome",
        back_populates="protocol_outcome",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_outcomes",
        back_populates="outcomes",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class Enrollment(Base, OrmFightForBase):
    """ Table of `<enrollment>` element records."""

    # Set table name.
    __tablename__ = "enrollments"

    # Autoincrementing primary key ID.
    enrollment_id = sqlalchemy.Column(
        name="enrollment_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<enrollment>` element.
    value = sqlalchemy.Column(
        name="value",
        type_=sqlalchemy.types.Integer(),
        nullable=False,
    )

    # Referring to the value of the `type` attribute.
    enrollment_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Enum(ActualType),
        nullable=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="enrollment",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class ArmGroup(Base, OrmFightForBase):
    """ Table of `<arm_group>` element records."""

    # Set table name.
    __tablename__ = "arm_groups"

    # Autoincrementing primary key ID.
    arm_group_id = sqlalchemy.Column(
        name="arm_group_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<arm_group_label>` element.
    label = sqlalchemy.Column(
        name="label",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the value of the `<arm_group_type>` element.
    arm_group_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<description>` element.
    description = sqlalchemy.Column(
        name="description",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `ArmGroup` records.
    interventions = sqlalchemy.orm.relationship(
        argument="Intervention",
        secondary="clinicaltrials.intervention_arm_groups",
        back_populates="arm_groups",
        uselist=True,
    )

    # Relationship to a list of `StudyArmGroup` records.
    study_arm_groups = sqlalchemy.orm.relationship(
        argument="StudyArmGroup",
        back_populates="arm_group",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_arm_groups",
        back_populates="arm_groups",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class Intervention(Base, OrmFightForBase):
    """ Table of `<intervention>` element records."""

    # Set table name.
    __tablename__ = "interventions"

    # Autoincrementing primary key ID.
    intervention_id = sqlalchemy.Column(
        name="intervention_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<intervention_type>` attribute.
    intervention_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Enum(InterventionType),
        nullable=False,
    )

    # Referring to the value of the `<intervention_name>` element.
    name = sqlalchemy.Column(
        name="name",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the value of the `<description>` element.
    description = sqlalchemy.Column(
        name="description",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # MD5 hash of the keyword.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `ArmGroup` records.
    arm_groups = sqlalchemy.orm.relationship(
        argument="ArmGroup",
        secondary="clinicaltrials.intervention_arm_groups",
        back_populates="interventions",
        uselist=True,
    )

    # Relationship to a list of `Alias` records.
    aliases = sqlalchemy.orm.relationship(
        argument="Alias",
        secondary="clinicaltrials.intervention_aliases",
        back_populates="interventions",
        uselist=True,
    )

    # Relationship to a list of `StudyIntervention` records.
    study_interventions = sqlalchemy.orm.relationship(
        argument="StudyIntervention",
        back_populates="intervention",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_interventions",
        back_populates="interventions",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates(
        "intervention_type",
        "name",
        "description",
    )
    def update_md5(self, key, value):
        attrs = {
            "intervention_type": self.intervention_type,
            "name": self.name,
            "description": self.description,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class Alias(Base, OrmFightForBase):
    """ Table of aliases."""

    # Set table name.
    __tablename__ = "aliases"

    # Autoincrementing primary key ID.
    alias_id = sqlalchemy.Column(
        name="alias_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Alias value.
    alias = sqlalchemy.Column(
        name="alias",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # MD5 hash of the keyword.
    md5 = sqlalchemy.Column(
        name="md5",
        type_=sqlalchemy.types.LargeBinary(length=16),
        unique=True,
        index=True,
        nullable=False,
    )

    # Relationship to a list of `Intervention` records.
    interventions = sqlalchemy.orm.relationship(
        argument="Intervention",
        secondary="clinicaltrials.intervention_aliases",
        back_populates="aliases",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_aliases",
        back_populates="aliases",
        uselist=True,
    )

    # Relationship to a list of `StudyAlias` records.
    study_aliases = sqlalchemy.orm.relationship(
        argument="StudyAlias",
        back_populates="alias",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }

    @sqlalchemy.orm.validates("alias")
    def update_md5(self, key, value):

        # Enforce lowercasing of the value in order to avoid needless
        # duplication when the keyword is provided with different casing.
        value = value.lower() if value else None

        # Assemble the class attributes into a `dict`.
        attrs = {
            "alias": self.alias,
        }
        attrs[key] = value

        # Calculate and update the `md5` attribute.
        self.md5 = self.calculate_md5(attrs=attrs, do_lowercase=True)

        return value


class InterventionAlias(Base, OrmFightForBase):
    """ Associative table between `Intervention` and `Alias` records."""

    # Set table name.
    __tablename__ = "intervention_aliases"

    # Autoincrementing primary key ID.
    intervention_alias_id = sqlalchemy.Column(
        name="intervention_alias_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the intervention ID.
    intervention_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.interventions.intervention_id"),
        name="intervention_id",
        nullable=False,
    )

    # Foreign key to the alias ID.
    alias_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.aliases.alias_id"),
        name="alias_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('intervention_id', 'alias_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class InterventionArmGroup(Base, OrmFightForBase):
    """ Associative table between `Intervention` and `ArmGroup` records."""

    # Set table name.
    __tablename__ = "intervention_arm_groups"

    # Autoincrementing primary key ID.
    intervention_arm_group_id = sqlalchemy.Column(
        name="intervention_arm_group_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the intervention ID.
    intervention_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.interventions.intervention_id"),
        name="intervention_id",
        nullable=False,
    )

    # Foreign key to the arm-group ID.
    arm_group_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.arm_groups.arm_group_id"),
        name="arm_group_id",
        nullable=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('intervention_id', 'arm_group_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class Eligibility(Base, OrmFightForBase):
    """ Table of `<eligibility>` element records."""

    # Set table name.
    __tablename__ = "eligibilities"

    # Autoincrementing primary key ID.
    eligibility_id = sqlalchemy.Column(
        name="eligibility_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<study_pop>` element.
    study_pop = sqlalchemy.Column(
        name="study_pop",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the value of the `<sampling_method>` attribute.
    sampling_method = sqlalchemy.Column(
        name="sampling_method",
        type_=sqlalchemy.types.Enum(SamplingMethodType),
        nullable=True,
    )

    # Referring to the value of the `<criteria>` element.
    criteria = sqlalchemy.Column(
        name="criteria",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the value of the `<gender>` attribute.
    gender = sqlalchemy.Column(
        name="gender",
        type_=sqlalchemy.types.Enum(GenderType),
        nullable=False,
        index=True,
    )

    # Referring to the `<gender_based>` element.
    gender_based = sqlalchemy.Column(
        name="gender_based",
        type_=sqlalchemy.types.Boolean(),
        nullable=True,
    )

    # Referring to the value of the `<gender_description>` element.
    gender_description = sqlalchemy.Column(
        name="gender_description",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<minimum_age>` element.
    minimum_age = sqlalchemy.Column(
        name="minimum_age",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # Referring to the value of the `<maximum_age>` element.
    maximum_age = sqlalchemy.Column(
        name="maximum_age",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
        index=True,
    )

    # Referring to the value of the `<healthy_volunteers>` element.
    healthy_volunteers = sqlalchemy.Column(
        name="healthy_volunteers",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="eligibility",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class Reference(Base, OrmFightForBase):
    """ Table of `<reference>` element records."""

    # Set table name.
    __tablename__ = "references"

    # Autoincrementing primary key ID.
    reference_id = sqlalchemy.Column(
        name="reference_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<citation>` element.
    citation = sqlalchemy.Column(
        name="citation",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<PMID>` element.
    pmid = sqlalchemy.Column(
        name="pmid",
        type_=sqlalchemy.types.Integer(),
        nullable=True,
        unique=True,
    )

    # Relationship to a list of `StudyReference` records.
    study_references = sqlalchemy.orm.relationship(
        argument="StudyReference",
        back_populates="reference",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_references",
        back_populates="references",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class ResponsibleParty(Base, OrmFightForBase):
    """ Table of `<responsible_party>` element records."""

    # Set table name.
    __tablename__ = "responsible_parties"

    # Autoincrementing primary key ID.
    responsible_party_id = sqlalchemy.Column(
        name="responsible_party_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<name_title>` element.
    name_title = sqlalchemy.Column(
        name="name_title",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<organization>` element.
    organization = sqlalchemy.Column(
        name="organization",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<responsible_party_type>` attribute.
    responsible_party_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Enum(ResponsiblePartyType),
        nullable=True,
    )

    # Referring to the value of the `<investigator_affiliation>` element.
    investigator_affiliation = sqlalchemy.Column(
        name="investigator_affiliation",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<investigator_full_name>` element.
    investigator_full_name = sqlalchemy.Column(
        name="investigator_full_name",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<investigator_title>` element.
    investigator_title = sqlalchemy.Column(
        name="investigator_title",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="responsible_party",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class PatientData(Base, OrmFightForBase):
    """ Table of `<patient_data>` element records."""

    # Set table name.
    __tablename__ = "patient_datas"

    # Autoincrementing primary key ID.
    patient_data_id = sqlalchemy.Column(
        name="patient_data_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<sharing_ipd>` element.
    sharing_ipd = sqlalchemy.Column(
        name="sharing_ipd",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the value of the `<ipd_description>` element.
    ipd_description = sqlalchemy.Column(
        name="ipd_description",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `PatientDataIpdInfoType` records.
    ipd_info_types = sqlalchemy.orm.relationship(
        argument="PatientDataIpdInfoType",
        back_populates="patient_data",
        uselist=True,
    )

    # Referring to the value of the `<ipd_time_frame>` element.
    ipd_time_frame = sqlalchemy.Column(
        name="ipd_time_frame",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<ipd_access_criteria>` element.
    ipd_access_criteria = sqlalchemy.Column(
        name="ipd_access_criteria",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<ipd_url>` element.
    ipd_url = sqlalchemy.Column(
        name="ipd_url",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="patient_data",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class PatientDataIpdInfoType(Base, OrmFightForBase):
    """ Table for `<ipd_info_type>` records."""

    # Set table name.
    __tablename__ = "patient_data_ipd_info_types"

    # Autoincrementing primary key ID.
    patient_data_ipd_info_type_id = sqlalchemy.Column(
        name="patient_data_ipd_info_type_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the patient-data ID.
    patient_data_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.patient_datas.patient_data_id"),
        name="patient_data_id",
        nullable=False,
    )

    # Referring to the value of the `<ipd_info_type>` element.
    ipd_info_type = sqlalchemy.Column(
        name="ipd_info_type",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Relationship to a `PatientData` record.
    patient_data = sqlalchemy.orm.relationship(
        argument="PatientData",
        back_populates="ipd_info_types",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class StudyDoc(Base, OrmFightForBase):
    """ Table of `<study_doc>` element records."""

    # Set table name.
    __tablename__ = "study_docs"

    # Autoincrementing primary key ID.
    study_doc_id = sqlalchemy.Column(
        name="study_doc_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<doc_id>` element.
    doc_id = sqlalchemy.Column(
        name="doc_id",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<doc_type>` element.
    doc_type = sqlalchemy.Column(
        name="doc_type",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<doc_url>` element.
    doc_url = sqlalchemy.Column(
        name="doc_url",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<doc_comment>` element.
    doc_comment = sqlalchemy.Column(
        name="doc_comment",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `StudyStudyDoc` records.
    study_study_docs = sqlalchemy.orm.relationship(
        argument="StudyStudyDoc",
        back_populates="study_doc",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_study_docs",
        back_populates="study_docs",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class StudyDates(Base, OrmFightForBase):
    """ Table of secondary dates pertaining to a `<clinical_study>` element
        record.
    """

    # Set table name.
    __tablename__ = "study_dates"

    # Autoincrementing primary key ID.
    study_dates_id = sqlalchemy.Column(
        name="study_dates_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<study_first_submitted>` element.
    study_first_submitted = sqlalchemy.Column(
        name="study_first_submitted",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<study_first_submitted_qc>` element.
    study_first_submitted_qc = sqlalchemy.Column(
        name="study_first_submitted_qc",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<study_first_posted>` element.
    study_first_posted = sqlalchemy.Column(
        name="study_first_posted",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<results_first_submitted>` element.
    results_first_submitted = sqlalchemy.Column(
        name="results_first_submitted",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<results_first_submitted_qc>` element.
    results_first_submitted_qc = sqlalchemy.Column(
        name="results_first_submitted_qc",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<results_first_posted>` element.
    results_first_posted = sqlalchemy.Column(
        name="results_first_posted",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<disposition_first_submitted>` element.
    disposition_first_submitted = sqlalchemy.Column(
        name="disposition_first_submitted",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<disposition_first_submitted_qc>` element.
    disposition_first_submitted_qc = sqlalchemy.Column(
        name="disposition_first_submitted_qc",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<disposition_first_posted>` element.
    disposition_first_posted = sqlalchemy.Column(
        name="disposition_first_posted",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<last_update_submitted>` element.
    last_update_submitted = sqlalchemy.Column(
        name="last_update_submitted",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<last_update_submitted_qc>` element.
    last_update_submitted_qc = sqlalchemy.Column(
        name="last_update_submitted_qc",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<last_update_posted>` element.
    last_update_posted = sqlalchemy.Column(
        name="last_update_posted",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_dates",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class Study(Base, OrmFightForBase):
    """ Table of `<clinical_study>` element records."""

    # Set table name.
    __tablename__ = "studies"

    # Autoincrementing primary key ID.
    study_id = sqlalchemy.Column(
        name="study_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Referring to the value of the `<org_study_id>` element.
    org_study_id = sqlalchemy.Column(
        name="org_study_id",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `StudySecondaryId` records.
    secondary_ids = sqlalchemy.orm.relationship(
        argument="StudySecondaryId",
        back_populates="study",
        uselist=True,
    )

    # Referring to the value of the `<nct_id>` element.
    nct_id = sqlalchemy.Column(
        name="nct_id",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
        unique=True,
    )

    # Relationship to a list of `StudyAlias` records.
    study_aliases = sqlalchemy.orm.relationship(
        argument="StudyAlias",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Alias` records.
    aliases = sqlalchemy.orm.relationship(
        argument="Alias",
        secondary="clinicaltrials.study_aliases",
        back_populates="studies",
        uselist=True,
    )

    # Referring to the value of the `<brief_title>` element.
    brief_title = sqlalchemy.Column(
        name="brief_title",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Referring to the value of the `<acronym>` element.
    acronym = sqlalchemy.Column(
        name="acronym",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<official_title>` element.
    official_title = sqlalchemy.Column(
        name="official_title",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `StudySponsor` records.
    study_sponsors = sqlalchemy.orm.relationship(
        argument="StudySponsor",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Sponsor` records.
    sponsors = sqlalchemy.orm.relationship(
        argument="Sponsor",
        secondary="clinicaltrials.study_sponsors",
        back_populates="studies",
        uselist=True,
    )

    # Referring to the value of the `<source>` element.
    source = sqlalchemy.Column(
        name="source",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Foreign key to the oversight-info ID.
    oversight_info_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "clinicaltrials.oversight_infos.oversight_info_id"
        ),
        name="oversight_info_id",
        nullable=True,
    )

    # Relationship to a `OversightInfo` record.
    oversight_info = sqlalchemy.orm.relationship(
        argument="OversightInfo",
        back_populates="study",
        uselist=False,
    )

    # Referring to the value of the `<brief_summary>` element.
    brief_summary = sqlalchemy.Column(
        name="brief_summary",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the value of the `<detailed_description>` element.
    detailed_description = sqlalchemy.Column(
        name="detailed_description",
        type_=sqlalchemy.types.UnicodeText(),
        nullable=True,
    )

    # Referring to the value of the `<overall_status>` element.
    overall_status = sqlalchemy.Column(
        name="overall_status",
        type_=sqlalchemy.types.Enum(OverallStatusType),
        nullable=False,
        index=True,
    )

    # Referring to the value of the `<last_known_status>` element.
    last_known_status = sqlalchemy.Column(
        name="last_known_status",
        type_=sqlalchemy.types.Enum(OverallStatusType),
        nullable=True,
        index=True,
    )

    # Referring to the value of the `<why_stopped>` element.
    why_stopped = sqlalchemy.Column(
        name="why_stopped",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Referring to the value of the `<start_date>` element.
    start_date = sqlalchemy.Column(
        name="start_date",
        type_=sqlalchemy.types.Date(),
        nullable=True,
        index=True,
    )

    # Referring to the value of the `<completion_date>` element.
    completion_date = sqlalchemy.Column(
        name="completion_date",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<primary_completion_date>` element.
    primary_completion_date = sqlalchemy.Column(
        name="primary_completion_date",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<verification_date>` element.
    verification_date = sqlalchemy.Column(
        name="verification_date",
        type_=sqlalchemy.types.Date(),
        nullable=True,
    )

    # Referring to the value of the `<phase>` element.
    phase = sqlalchemy.Column(
        name="phase",
        type_=sqlalchemy.types.Enum(PhaseType),
        nullable=True,
        index=True,
    )

    # Referring to the value of the `<study_type>` element.
    study_type = sqlalchemy.Column(
        name="study_type",
        type_=sqlalchemy.types.Enum(StudyType),
        nullable=False,
        index=True,
    )

    # Foreign key to the expanded-access-info ID.
    expanded_access_info_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "clinicaltrials.expanded_access_infos.expanded_access_info_id"
        ),
        name="expanded_access_info_id",
        nullable=True,
    )

    # Relationship to a `ExpandedAccessInfo` record.
    expanded_access_info = sqlalchemy.orm.relationship(
        argument="ExpandedAccessInfo",
        back_populates="study",
        uselist=False,
    )

    # Foreign key to the study-design-info ID.
    study_design_info_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "clinicaltrials.study_design_infos.study_design_info_id"
        ),
        name="study_design_info_id",
        nullable=True,
    )

    # Relationship to a `StudyDesignInfo` record.
    study_design_info = sqlalchemy.orm.relationship(
        argument="StudyDesignInfo",
        back_populates="study",
        uselist=False,
    )

    # Referring to the value of the `<target_duration>` element.
    target_duration = sqlalchemy.Column(
        name="target_duration",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Relationship to a list of `StudyOutcome` records.
    study_outcomes = sqlalchemy.orm.relationship(
        argument="StudyOutcome",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `ProtocolOutcome` records.
    outcomes = sqlalchemy.orm.relationship(
        argument="ProtocolOutcome",
        secondary="clinicaltrials.study_outcomes",
        back_populates="studies",
        uselist=True,
    )

    # Foreign key to the enrollment ID.
    enrollment_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.enrollments.enrollment_id"),
        name="enrollment_id",
        nullable=True,
    )

    # Relationship to a `Enrollment` record.
    enrollment = sqlalchemy.orm.relationship(
        argument="Enrollment",
        back_populates="study",
        uselist=False,
    )

    # Relationship to a list of `StudyCondition` records.
    study_conditions = sqlalchemy.orm.relationship(
        argument="StudyCondition",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Condition` records.
    conditions = sqlalchemy.orm.relationship(
        argument="Condition",
        secondary="clinicaltrials.study_conditions",
        back_populates="studies",
        uselist=True,
    )

    # Relationship to a list of `StudyArmGroup` records.
    study_arm_groups = sqlalchemy.orm.relationship(
        argument="StudyArmGroup",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `ArmGroup` records.
    arm_groups = sqlalchemy.orm.relationship(
        argument="ArmGroup",
        secondary="clinicaltrials.study_arm_groups",
        back_populates="studies",
        uselist=True,
    )

    # Relationship to a list of `StudyIntervention` records.
    study_interventions = sqlalchemy.orm.relationship(
        argument="StudyIntervention",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Intervention` records.
    interventions = sqlalchemy.orm.relationship(
        argument="Intervention",
        secondary="clinicaltrials.study_interventions",
        back_populates="studies",
        uselist=True,
    )

    # Referring to the value of the `<biospec_retention>` element.
    biospec_retention = sqlalchemy.Column(
        name="biospec_retention",
        type_=sqlalchemy.types.Enum(BiospecRetentionType),
        nullable=True,
        index=True,
    )

    # Referring to the value of the `<biospec_desc>` element.
    biospec_description = sqlalchemy.Column(
        name="biospec_description",
        type_=sqlalchemy.types.Unicode(),
        nullable=True,
    )

    # Foreign key to the elligibility ID.
    eligibility_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.eligibilities.eligibility_id"),
        name="eligibility_id",
        nullable=True,
    )

    # Relationship to an `Elligibility` record.
    eligibility = sqlalchemy.orm.relationship(
        argument="Eligibility",
        back_populates="study",
        uselist=False,
    )

    # Relationship to a list of `StudyInvestigator` records.
    study_investigators = sqlalchemy.orm.relationship(
        argument="StudyInvestigator",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Investigator` records.
    investigators = sqlalchemy.orm.relationship(
        argument="Investigator",
        secondary="clinicaltrials.study_investigators",
        back_populates="studies",
        uselist=True,
    )

    # Foreign key to a contact ID of 'primary' type.
    contact_primary_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.contacts.contact_id"),
        name="contact_primary_id",
        nullable=True,
    )

    # Relationship to a `Contact` record of 'primary' type.
    contact_primary = sqlalchemy.orm.relationship(
        argument="Contact",
        foreign_keys=contact_primary_id,
        uselist=False,
    )

    # Foreign key to a contact ID of 'backup' type.
    contact_backup_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.contacts.contact_id"),
        name="contact_backup_id",
        nullable=True,
    )

    # Relationship to a `Contact` record of 'backup' type.
    contact_backup = sqlalchemy.orm.relationship(
        argument="Contact",
        foreign_keys=contact_backup_id,
        uselist=False,
    )

    # Relationship to a list of `StudyLocation` records.
    study_locations = sqlalchemy.orm.relationship(
        argument="StudyLocation",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Location` records.
    locations = sqlalchemy.orm.relationship(
        argument="Location",
        secondary="clinicaltrials.study_locations",
        back_populates="studies",
        uselist=True,
    )

    # Relationship to a list of `StudyFacility` records.
    study_facilities = sqlalchemy.orm.relationship(
        argument="StudyFacility",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Facility` records.
    facilities = sqlalchemy.orm.relationship(
        argument="Facility",
        secondary="clinicaltrials.study_facilities",
        back_populates="studies",
        uselist=True,
    )

    # Relationship to a list of `FacilityCanonical` records.
    facilities_canonical = sqlalchemy.orm.relationship(
        argument="FacilityCanonical",
        secondary="clinicaltrials.study_facilities",
        back_populates="studies",
        uselist=True,
    )

    # Relationship to a list of `StudyReference` records.
    study_references = sqlalchemy.orm.relationship(
        argument="StudyReference",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Reference` records.
    references = sqlalchemy.orm.relationship(
        argument="Reference",
        secondary="clinicaltrials.study_references",
        back_populates="studies",
        uselist=True,
    )

    # Foreign key to the study-dates ID.
    study_dates_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.study_dates.study_dates_id"),
        name="study_dates_id",
        nullable=False,
    )

    # Relationship to a list of `StudyDates` records.
    study_dates = sqlalchemy.orm.relationship(
        argument="StudyDates",
        back_populates="study",
        uselist=False,
    )

    # Foreign key to a responsible-party ID.
    responsible_party_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "clinicaltrials.responsible_parties.responsible_party_id"
        ),
        name="responsible_party_id",
        nullable=True,
    )

    # Relationship to a `ResponsibleParty` record.
    responsible_party = sqlalchemy.orm.relationship(
        argument="ResponsibleParty",
        back_populates="study",
        uselist=False,
    )

    # Relationship to a list of `StudyKeyword` records.
    study_keywords = sqlalchemy.orm.relationship(
        argument="StudyKeyword",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Keyword` records.
    keywords = sqlalchemy.orm.relationship(
        argument="Keyword",
        secondary="clinicaltrials.study_keywords",
        back_populates="studies",
        uselist=True,
    )

    # Relationship to a list of `StudyDescriptor` records.
    study_descriptors = sqlalchemy.orm.relationship(
        argument="StudyDescriptor",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `Descriptor` records.
    descriptors = sqlalchemy.orm.relationship(
        argument="Descriptor",
        secondary="clinicaltrials.study_descriptors",
        back_populates="studies",
        uselist=True,
    )

    # Foreign key to a patient-data ID.
    patient_data_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.patient_datas.patient_data_id"),
        name="patient_data_id",
        nullable=True,
    )

    # Relationship to a `PatientData` record.
    patient_data = sqlalchemy.orm.relationship(
        argument="PatientData",
        back_populates="study",
        uselist=False,
    )

    # Relationship to a list of `StudyStudyDoc` records.
    study_study_docs = sqlalchemy.orm.relationship(
        argument="StudyStudyDoc",
        back_populates="study",
        uselist=True,
    )

    # Relationship to a list of `StudyDoc` records.
    study_docs = sqlalchemy.orm.relationship(
        argument="StudyDoc",
        secondary="clinicaltrials.study_study_docs",
        back_populates="studies",
        uselist=True,
    )

    # TODO: pending_results
    # TODO: clinical_results

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class StudySecondaryId(Base, OrmFightForBase):
    """ Table for `<secondary_id>` records."""

    # Set table name.
    __tablename__ = "study_secondary_ids"

    # Autoincrementing primary key ID.
    study_secondary_id_id = sqlalchemy.Column(
        name="study_secondary_id_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Referring to the value of the `<secondary_id>` element.
    secondary_id = sqlalchemy.Column(
        name="secondary_id",
        type_=sqlalchemy.types.Unicode(),
        nullable=False,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="secondary_ids",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class StudyAlias(Base, OrmFightForBase):
    """ Associative table between `Study` and `Alias` records."""

    # Set table name.
    __tablename__ = "study_aliases"

    # Autoincrementing primary key ID.
    study_alias_id = sqlalchemy.Column(
        name="study_alias_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the alias ID.
    alias_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.aliases.alias_id"),
        name="alias_id",
        nullable=False,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_aliases",
        uselist=False,
    )

    # Relationship to a `Alias` record.
    alias = sqlalchemy.orm.relationship(
        argument="Alias",
        back_populates="study_aliases",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'alias_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudySponsor(Base, OrmFightForBase):
    """ Associative table between `Study` and `Sponsor` records."""

    # Set table name.
    __tablename__ = "study_sponsors"

    # Autoincrementing primary key ID.
    study_sponsor_id = sqlalchemy.Column(
        name="study_sponsor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the sponsor ID.
    sponsor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.sponsors.sponsor_id"),
        name="sponsor_id",
        nullable=False,
    )

    # Sponsor type (defined by the name of the element of `<sponsor>` type.
    sponsor_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Enum(SponsorType),
        nullable=False,
        index=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_sponsors",
        uselist=False,
    )

    # Relationship to a `Sponsor` record.
    sponsor = sqlalchemy.orm.relationship(
        argument="Sponsor",
        back_populates="study_sponsors",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'sponsor_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyOutcome(Base, OrmFightForBase):
    """ Associative table between `Study` and `ProtocolOutcome` records."""

    # Set table name.
    __tablename__ = "study_outcomes"

    # Autoincrementing primary key ID.
    study_outcome_id = sqlalchemy.Column(
        name="study_outcome_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the protocol-outcome ID.
    protocol_outcome_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "clinicaltrials.protocol_outcomes.protocol_outcome_id"
        ),
        name="protocol_outcome_id",
        nullable=False,
    )

    # Referring to the type of outcome.
    outcome_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Enum(OutcomeType),
        nullable=False,
        index=True
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_outcomes",
        uselist=False,
    )

    # Relationship to a `ProtocolOutcome` record.
    protocol_outcome = sqlalchemy.orm.relationship(
        argument="ProtocolOutcome",
        back_populates="study_outcomes",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'protocol_outcome_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyCondition(Base, OrmFightForBase):
    """ Associative table between `Study` and `Condition` records."""

    # Set table name.
    __tablename__ = "study_conditions"

    # Autoincrementing primary key ID.
    study_condition_id = sqlalchemy.Column(
        name="study_condition_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the condition ID.
    condition_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.conditions.condition_id"),
        name="condition_id",
        nullable=False,
        index=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_conditions",
        uselist=False,
    )

    # Relationship to a `Condition` record.
    condition = sqlalchemy.orm.relationship(
        argument="Condition",
        back_populates="study_conditions",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'condition_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyArmGroup(Base, OrmFightForBase):
    """ Associative table between `Study` and `ArmGroup` records."""

    # Set table name.
    __tablename__ = "study_arm_groups"

    # Autoincrementing primary key ID.
    study_arm_group_id = sqlalchemy.Column(
        name="study_arm_group_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the arm-group ID.
    arm_group_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.arm_groups.arm_group_id"),
        name="arm_group_id",
        nullable=False,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_arm_groups",
        uselist=False,
    )

    # Relationship to a `ArmGroup` record.
    arm_group = sqlalchemy.orm.relationship(
        argument="ArmGroup",
        back_populates="study_arm_groups",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'arm_group_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyIntervention(Base, OrmFightForBase):
    """ Associative table between `Study` and `Intervention` records."""

    # Set table name.
    __tablename__ = "study_interventions"

    # Autoincrementing primary key ID.
    study_intervention_id = sqlalchemy.Column(
        name="study_intervention_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the intervention ID.
    intervention_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.interventions.intervention_id"),
        name="intervention_id",
        nullable=False,
        index=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_interventions",
        uselist=False,
    )

    # Relationship to a `ArmGroup` record.
    intervention = sqlalchemy.orm.relationship(
        argument="Intervention",
        back_populates="study_interventions",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'intervention_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyInvestigator(Base, OrmFightForBase):
    """ Associative table between `Study` and `Investigator` records."""

    # Set table name.
    __tablename__ = "study_investigators"

    # Autoincrementing primary key ID.
    study_investigator_id = sqlalchemy.Column(
        name="study_investigator_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the investigator ID.
    investigator_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.investigators.investigator_id"),
        name="investigator_id",
        nullable=False,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_investigators",
        uselist=False,
    )

    # Relationship to a `Investigator` record.
    investigator = sqlalchemy.orm.relationship(
        argument="Investigator",
        back_populates="study_investigators",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'investigator_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyLocation(Base, OrmFightForBase):
    """ Associative table between `Study` and `Location` records."""

    # Set table name.
    __tablename__ = "study_locations"

    # Autoincrementing primary key ID.
    study_location_id = sqlalchemy.Column(
        name="study_location_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the location ID.
    location_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.locations.location_id"),
        name="location_id",
        nullable=False,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_locations",
        uselist=False,
    )

    # Relationship to a `Location` record.
    location = sqlalchemy.orm.relationship(
        argument="Location",
        back_populates="study_locations",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'location_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyReference(Base, OrmFightForBase):
    """ Associative table between `Study` and `Reference` records."""

    # Set table name.
    __tablename__ = "study_references"

    # Autoincrementing primary key ID.
    study_reference_id = sqlalchemy.Column(
        name="study_reference_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the reference ID.
    reference_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.references.reference_id"),
        name="reference_id",
        nullable=False,
    )

    # Referring to the type of reference.
    reference_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Enum(ReferenceType),
        nullable=False,
        index=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_references",
        uselist=False,
    )

    # Relationship to a `Reference` record.
    reference = sqlalchemy.orm.relationship(
        argument="Reference",
        back_populates="study_references",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'reference_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyKeyword(Base, OrmFightForBase):
    """ Associative table between `Study` and `Keyword` records."""

    # Set table name.
    __tablename__ = "study_keywords"

    # Autoincrementing primary key ID.
    study_keyword_id = sqlalchemy.Column(
        name="study_keyword_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the keyword ID.
    keyword_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.keywords.keyword_id"),
        name="keyword_id",
        nullable=False,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_keywords",
        uselist=False,
    )

    # Relationship to a `Keyword` record.
    keyword = sqlalchemy.orm.relationship(
        argument="Keyword",
        back_populates="study_keywords",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'keyword_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyDescriptor(Base, OrmFightForBase):
    """ Associative table between `Study` and `Descriptor` records."""

    # Set table name.
    __tablename__ = "study_descriptors"

    # Autoincrementing primary key ID.
    study_descriptor_id = sqlalchemy.Column(
        name="study_descriptor_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the MeSH dewscriptor ID.
    descriptor_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("mesh.descriptors.descriptor_id"),
        name="descriptor_id",
        nullable=False,
        index=True,
    )

    # Referring to the type of MeSH descriptor.
    study_descriptor_type = sqlalchemy.Column(
        name="type",
        type_=sqlalchemy.types.Enum(MeshTermType),
        nullable=False,
        index=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_descriptors",
        uselist=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_descriptors",
        uselist=False,
    )

    # Relationship to a `Descriptor` record.
    descriptor = sqlalchemy.orm.relationship(
        argument="Descriptor",
        back_populates="study_descriptors",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'descriptor_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class StudyStudyDoc(Base, OrmFightForBase):
    """ Associative table between `Study` and `StudyDoc` records."""

    # Set table name.
    __tablename__ = "study_study_docs"

    # Autoincrementing primary key ID.
    study_study_doc_id = sqlalchemy.Column(
        name="study_study_doc_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
    )

    # Foreign key to the study-doc ID.
    study_doc_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.study_docs.study_doc_id"),
        name="study_doc_id",
        nullable=False,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_study_docs",
        uselist=False,
    )

    # Relationship to a `StudyDoc` record.
    study_doc = sqlalchemy.orm.relationship(
        argument="StudyDoc",
        back_populates="study_study_docs",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'study_doc_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )


class FacilityCanonical(Base, OrmFightForBase):
    """ Table storing canonicalized version of study facilities with data
        retrieved from the Google Maps API.
    """

    # Set table name.
    __tablename__ = "facilities_canonical"

    # Autoincrementing primary key ID.
    facility_canonical_id = sqlalchemy.Column(
        name="facility_canonical_id",
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

    # Relationship to a `Facility` record.
    facility = sqlalchemy.orm.relationship(
        argument="Facility",
        back_populates="facility_canonical",
        uselist=False,
    )

    # Relationship to a list of `StudyFacility` records.
    study_facilities = sqlalchemy.orm.relationship(
        argument="StudyFacility",
        back_populates="facility_canonical",
        uselist=True,
    )

    # Relationship to a list of `Study` records.
    studies = sqlalchemy.orm.relationship(
        argument="Study",
        secondary="clinicaltrials.study_facilities",
        back_populates="facilities_canonical",
        uselist=True,
    )

    # Set table arguments.
    __table_args__ = {
        # Set table schema.
        "schema": "clinicaltrials",
    }


class StudyFacility(Base, OrmFightForBase):
    """ Associative table between `Study`, `Facility` and `FacilityCanonical`
        records.
    """

    # Set table name.
    __tablename__ = "study_facilities"

    # Autoincrementing primary key ID.
    study_facility_id = sqlalchemy.Column(
        name="study_facility_id",
        type_=sqlalchemy.types.BigInteger(),
        primary_key=True,
        autoincrement="auto",
    )

    # Foreign key to the study ID.
    study_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.studies.study_id"),
        name="study_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the facility ID.
    facility_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey("clinicaltrials.facilities.facility_id"),
        name="facility_id",
        nullable=False,
        index=True,
    )

    # Foreign key to the canonical facility ID.
    facility_canonical_id = sqlalchemy.Column(
        sqlalchemy.ForeignKey(
            "clinicaltrials.facilities_canonical.facility_canonical_id",
        ),
        name="facility_canonical_id",
        nullable=True,
        index=True,
    )

    # Relationship to a `Study` record.
    study = sqlalchemy.orm.relationship(
        argument="Study",
        back_populates="study_facilities",
        uselist=False,
    )

    # Relationship to a `Facility` record.
    facility = sqlalchemy.orm.relationship(
        argument="Facility",
        back_populates="study_facilities",
        uselist=False,
    )

    # Relationship to a `FacilityCanonical` record.
    facility_canonical = sqlalchemy.orm.relationship(
        argument="FacilityCanonical",
        back_populates="study_facilities",
        uselist=False,
    )

    # Set table arguments.
    __table_args__ = (
        # Set unique constraint.
        sqlalchemy.UniqueConstraint('study_id', 'facility_id'),
        # Set table schema.
        {"schema": "clinicaltrials"},
    )
