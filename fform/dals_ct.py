# coding: utf-8

from typing import Union, Optional
import datetime

import sqlalchemy.orm
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.dialects.postgresql import Insert
from sqlalchemy.engine.result import ResultProxy

from fform.dal_base import DalFightForBase
from fform.dal_base import with_session_scope
from fform.orm_ct import Sponsor
from fform.orm_ct import Keyword
from fform.orm_ct import Condition
from fform.orm_ct import Facility
from fform.orm_ct import Person
from fform.orm_ct import Contact
from fform.orm_ct import Investigator
from fform.orm_ct import Location
from fform.orm_ct import LocationInvestigator
from fform.orm_ct import OversightInfo
from fform.orm_ct import ExpandedAccessInfo
from fform.orm_ct import StudyDesignInfo
from fform.orm_ct import ProtocolOutcome
from fform.orm_ct import Enrollment
from fform.orm_ct import ActualType
from fform.orm_ct import ArmGroup
from fform.orm_ct import Intervention
from fform.orm_ct import Alias
from fform.orm_ct import InterventionAlias
from fform.orm_ct import InterventionArmGroup
from fform.orm_ct import Eligibility
from fform.orm_ct import Reference
from fform.orm_ct import ResponsibleParty
from fform.orm_ct import MeshTerm
from fform.orm_ct import PatientData
from fform.orm_ct import StudyDoc
from fform.orm_ct import Study
from fform.orm_ct import StudyAlias
from fform.orm_ct import StudySponsor
from fform.orm_ct import StudyOutcome
from fform.orm_ct import StudyCondition
from fform.orm_ct import StudyArmGroup
from fform.orm_ct import StudyIntervention
from fform.orm_ct import StudyInvestigator
from fform.orm_ct import StudyLocation
from fform.orm_ct import StudyReference
from fform.orm_ct import StudyKeyword
from fform.orm_ct import StudyMeshTerm
from fform.orm_ct import StudyStudyDoc
from fform.orm_ct import StudyDates
from fform.orm_ct import AgencyClassType
from fform.orm_ct import SponsorType
from fform.orm_ct import RoleType
from fform.orm_ct import RecruitmentStatusType
from fform.orm_ct import OutcomeType
from fform.orm_ct import InterventionType
from fform.orm_ct import SamplingMethodType
from fform.orm_ct import GenderType
from fform.orm_ct import ResponsiblePartyType
from fform.orm_ct import OverallStatusType
from fform.orm_ct import PhaseType
from fform.orm_ct import StudyType
from fform.orm_ct import BiospecRetentionType
from fform.orm_ct import MeshTermType
from fform.orm_ct import ReferenceType
from fform.orm_ct import FacilityCanonical
from fform.orm_ct import StudyFacility
from fform.utils import return_first_item


class DalClinicalTrials(DalFightForBase):
    def __init__(
        self,
        sql_username,
        sql_password,
        sql_host,
        sql_port,
        sql_db,
        *args,
        **kwargs
    ):

        super(DalClinicalTrials, self).__init__(
            sql_username=sql_username,
            sql_password=sql_password,
            sql_host=sql_host,
            sql_port=sql_port,
            sql_db=sql_db,
            *args,
            **kwargs
        )

    @return_first_item
    @with_session_scope()
    def iodi_sponsor(
        self,
        agency: str,
        agency_class: AgencyClassType,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Sponsor` record in an IODI manner.

        Args:
            agency (str): The sponsor agency.
            agency_class (AgencyClassType): An enumeration member denoting the
                sponsor agency class.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Sponsor` record.
        """

        # Create and populate a `Sponsor` object so that we can retrieve the
        # MD5 hash.
        obj = Sponsor()
        obj.agency = agency
        obj.agency_class = agency_class

        # Upsert the `Sponsor` record.
        statement = insert(
            Sponsor,
            values={
                "agency": obj.agency,
                "class": obj.agency_class,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Sponsor,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Sponsor
            return obj.sponsor_id

    @return_first_item
    @with_session_scope()
    def iodi_keyword(
        self,
        keyword: str,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Keyword` record in an IODI manner.

        Args:
            keyword (str): The keyword.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Keyword` record.
        """

        # Create and populate a `Person` object so that we can retrieve the
        # MD5 hash.
        obj = Keyword()
        obj.keyword = keyword

        # Upsert the `Keyword` record.
        statement = insert(
            Keyword,
            values={
                "keyword": obj.keyword,
                "md5": obj.md5
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Keyword,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Keyword
            return obj.keyword_id

    @return_first_item
    @with_session_scope()
    def iodi_condition(
        self,
        condition: str,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Condition` record in an IODI manner.

        Args:
            condition (str): The condition.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Condition` record.
        """

        # Create and populate a `Condition` object so that we can retrieve the
        # MD5 hash.
        obj = Condition()
        obj.condition = condition

        statement = insert(
            Condition,
            values={
                "condition": obj.condition,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Condition,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Condition
            return obj.condition_id

    @return_first_item
    @with_session_scope()
    def iodi_facility(
        self,
        name: Union[str, None],
        city: Union[str, None],
        state: Union[str, None],
        zip_code: Union[str, None],
        country: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Facility` record in an IODI manner.

        Args:
            name (str): The facility name.
            city (str): The facility city.
            state (str): The facility state.
            zip_code (str): The facility zip-code.
            country (str): The facility country.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Condition` record.
        """

        # Create and populate a `Facility` object so that we can retrieve the
        # MD5 hash.
        obj = Facility()
        obj.name = name
        obj.city = city
        obj.state = state
        obj.zip_code = zip_code
        obj.country = country

        statement = insert(
            Facility,
            values={
                "name": obj.name,
                "city": obj.city,
                "state": obj.state,
                "zip_code": obj.zip_code,
                "country": obj.country,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Facility,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Facility
            return obj.facility_id

    @return_first_item
    @with_session_scope()
    def iodu_facility_canonical(
        self,
        google_place_id: str,
        name: Union[str, None],
        google_url: Union[str, None],
        url: Union[str, None],
        address: Union[str, None],
        phone_number: Union[str, None],
        coordinate_longitude: Union[float, None],
        coordinate_latitude: Union[float, None],
        country: Union[str, None],
        administrative_area_level_1: Union[str, None],
        administrative_area_level_2: Union[str, None],
        administrative_area_level_3: Union[str, None],
        administrative_area_level_4: Union[str, None],
        administrative_area_level_5: Union[str, None],
        locality: Union[str, None],
        sublocality: Union[str, None],
        sublocality_level_1: Union[str, None],
        sublocality_level_2: Union[str, None],
        sublocality_level_3: Union[str, None],
        sublocality_level_4: Union[str, None],
        sublocality_level_5: Union[str, None],
        colloquial_area: Union[str, None],
        floor: Union[str, None],
        room: Union[str, None],
        intersection: Union[str, None],
        neighborhood: Union[str, None],
        post_box: Union[str, None],
        postal_code: Union[str, None],
        postal_code_prefix: Union[str, None],
        postal_code_suffix: Union[str, None],
        postal_town: Union[str, None],
        premise: Union[str, None],
        subpremise: Union[str, None],
        route: Union[str, None],
        street_address: Union[str, None],
        street_number: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `FacilityCanonical` record in an IODU manner.

        Args:
            google_place_id (str): Google Place ID.
            name (str): Facility name.
            google_url (str): Google Maps place URL.
            url (Union[str, None]): Facility URL.
            address (Union[str, None]): Facility formatted address.
            phone_number (Union[str, None]): Facility phone-number.
            coordinate_longitude (float): Facility longitude.
            coordinate_latitude (float): Facility latitude.
            country (str): Country.
            administrative_area_level_1 (Union[str, None]): First-order civil
                entity below the country level.
            administrative_area_level_2 (Union[str, None]): Second-order civil
                entity below the country level.
            administrative_area_level_3 (Union[str, None]): Third-order civil
                entity below the country level.
            administrative_area_level_4 (Union[str, None]): Fourth-order civil
                entity below the country level.
            administrative_area_level_5 (Union[str, None]): Fifth-order civil
                entity below the country level.
            locality (Union[str, None]): Incorporated city or town political
                entity.
            sublocality (Union[str, None]): First-order civil entity below a
                locality.
            sublocality_level_1 (Union[str, None]): First-order sublocality.
            sublocality_level_2 (Union[str, None]): Second-order sublocality.
            sublocality_level_3 (Union[str, None]): Third-order sublocality.
            sublocality_level_4 (Union[str, None]): Fourth-order sublocality.
            sublocality_level_5 (Union[str, None]): Fifth-order sublocality.
            colloquial_area (Union[str, None]): Commonly-used alternative name
                for the entity.
            floor (Union[str, None]): Floor of a building address.
            room (Union[str, None]): Room of a building address.
            intersection (Union[str, None]): Major intersection, usually of two
                major roads.
            neighborhood (Union[str, None]): Named neighborhood.
            post_box (Union[str, None]): Postal box.
            postal_code (Union[str, None]): Postal code as used to address
                postal mail within the country.
            postal_code_prefix (Union[str, None]): Postal code prefix.
            postal_code_suffix (Union[str, None]): Postal code suffix.
            postal_town (Union[str, None]): Grouping of geographic areas, such
                as `locality` and `sublocality`, used for mailing addresses in
                some countries.
            premise (Union[str, None]): Named location, usually a building or
                collection of buildings with a common name.
            subpremise (Union[str, None]): First-order entity below a named
                location, usually a singular building within a collection of
                buildings with a common name.
            route (Union[str, None]): Named route.
            street_address (Union[str, None]): Precise street address.
            street_number (Union[str, None]): Precise street number.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Location` record.
        """
        
        # Assemble a PostGIS coordinates point if coordinates have been defined.
        coordinates = None
        if coordinate_latitude and coordinate_longitude:
            coordinates = "SRID=4326;POINT({} {})".format(
                coordinate_longitude,
                coordinate_latitude,
            )

        obj = FacilityCanonical()
        obj.google_place_id = google_place_id
        obj.name = name
        obj.google_url = google_url
        obj.url = url
        obj.address = address
        obj.phone_number = phone_number
        obj.coordinates = coordinates,
        obj.coordinate_latitude = coordinate_latitude
        obj.country = country
        obj.administrative_area_level_1 = administrative_area_level_1
        obj.administrative_area_level_2 = administrative_area_level_2
        obj.administrative_area_level_3 = administrative_area_level_3
        obj.administrative_area_level_4 = administrative_area_level_4
        obj.administrative_area_level_5 = administrative_area_level_5
        obj.locality = locality
        obj.sublocality = sublocality
        obj.sublocality_level_1 = sublocality_level_1
        obj.sublocality_level_2 = sublocality_level_2
        obj.sublocality_level_3 = sublocality_level_3
        obj.sublocality_level_4 = sublocality_level_4
        obj.sublocality_level_5 = sublocality_level_5
        obj.colloquial_area = colloquial_area
        obj.floor = floor
        obj.room = room
        obj.intersection = intersection
        obj.neighborhood = neighborhood
        obj.post_box = post_box
        obj.postal_code = postal_code
        obj.postal_code_prefix = postal_code_prefix
        obj.postal_code_suffix = postal_code_suffix
        obj.postal_town = postal_town
        obj.premise = premise
        obj.subpremise = subpremise
        obj.route = route
        obj.street_address = street_address
        obj.street_number = street_number

        statement = insert(
            FacilityCanonical,
            values={
                "google_place_id": obj.google_place_id,
                "name": obj.name,
                "google_url": obj.google_url,
                "url": obj.url,
                "address": obj.address,
                "phone_number": obj.phone_number,
                "coordinates": obj.coordinates,
                "country": obj.country,
                "administrative_area_level_1": obj.administrative_area_level_1,
                "administrative_area_level_2": obj.administrative_area_level_2,
                "administrative_area_level_3": obj.administrative_area_level_3,
                "administrative_area_level_4": obj.administrative_area_level_4,
                "administrative_area_level_5": obj.administrative_area_level_5,
                "locality": obj.locality,
                "sublocality": obj.sublocality,
                "sublocality_level_1": obj.sublocality_level_1,
                "sublocality_level_2": obj.sublocality_level_2,
                "sublocality_level_3": obj.sublocality_level_3,
                "sublocality_level_4": obj.sublocality_level_4,
                "sublocality_level_5": obj.sublocality_level_5,
                "colloquial_area": obj.colloquial_area,
                "floor": obj.floor,
                "room": obj.room,
                "intersection": obj.intersection,
                "neighborhood": obj.neighborhood,
                "post_box": obj.post_box,
                "postal_code": obj.postal_code,
                "postal_code_prefix": obj.postal_code_prefix,
                "postal_code_suffix": obj.postal_code_suffix,
                "postal_town": obj.postal_town,
                "premise": obj.premise,
                "subpremise": obj.subpremise,
                "route": obj.route,
                "street_address": obj.street_address,
                "street_number": obj.street_number,
            }
        ).on_conflict_do_update(
            index_elements=["google_place_id"],
            set_={
                "name": obj.name,
                "google_url": obj.google_url,
                "url": obj.url,
                "address": obj.address,
                "phone_number": obj.phone_number,
                "coordinates": obj.coordinates,
                "country": obj.country,
                "administrative_area_level_1": obj.administrative_area_level_1,
                "administrative_area_level_2": obj.administrative_area_level_2,
                "administrative_area_level_3": obj.administrative_area_level_3,
                "administrative_area_level_4": obj.administrative_area_level_4,
                "administrative_area_level_5": obj.administrative_area_level_5,
                "locality": obj.locality,
                "sublocality": obj.sublocality,
                "sublocality_level_1": obj.sublocality_level_1,
                "sublocality_level_2": obj.sublocality_level_2,
                "sublocality_level_3": obj.sublocality_level_3,
                "sublocality_level_4": obj.sublocality_level_4,
                "sublocality_level_5": obj.sublocality_level_5,
                "colloquial_area": obj.colloquial_area,
                "floor": obj.floor,
                "room": obj.room,
                "intersection": obj.intersection,
                "neighborhood": obj.neighborhood,
                "post_box": obj.post_box,
                "postal_code": obj.postal_code,
                "postal_code_prefix": obj.postal_code_prefix,
                "postal_code_suffix": obj.postal_code_suffix,
                "postal_town": obj.postal_town,
                "premise": obj.premise,
                "subpremise": obj.subpremise,
                "route": obj.route,
                "street_address": obj.street_address,
                "street_number": obj.street_number,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=FacilityCanonical,
                attr_name="google_place_id",
                attr_value=obj.google_place_id,
                session=session,
            )  # type: FacilityCanonical
            return obj.facility_canonical_id

    @return_first_item
    @with_session_scope()
    def iodi_person(
        self,
        name_first: Union[str, None],
        name_middle: Union[str, None],
        name_last: Union[str, None],
        degrees: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Person` record in an IODI manner.

        Args:
            name_first (str): The person first name.
            name_middle (str): The person middle name.
            name_last (str): The person last name.
            degrees (str): The person degrees.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Person` record.
        """

        # Create and populate a `Person` object so that we can retrieve the
        # MD5 hash.
        obj = Person()
        obj.name_first = name_first
        obj.name_middle = name_middle
        obj.name_last = name_last
        obj.degrees = degrees

        statement = insert(
            Person,
            values={
                "name_first": obj.name_first,
                "name_middle": obj.name_middle,
                "name_last": obj.name_last,
                "degrees": obj.degrees,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Person,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Person
            return obj.person_id

    @return_first_item
    @with_session_scope()
    def iodi_contact(
        self,
        person_id: int,
        phone: Union[str, None],
        phone_ext: Union[str, None],
        email: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Contact` record in an IODI manner.

        Args:
            person_id (int): The linked `Person` record primary-key ID.
            phone (str): The contact phone.
            phone_ext (str): The contact phone extension.
            email (str): The contact email.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Contact` record.
        """

        # Create and populate a `Contact` object so that we can retrieve the
        # MD5 hash.
        obj = Contact()
        obj.person_id = person_id
        obj.phone = phone
        obj.phone_ext = phone_ext
        obj.email = email

        statement = insert(
            Contact,
            values={
                "person_id": obj.person_id,
                "phone": obj.phone,
                "phone_ext": obj.phone_ext,
                "email": obj.email,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Contact,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Contact
            return obj.contact_id

    @return_first_item
    @with_session_scope()
    def iodi_investigator(
        self,
        person_id: int,
        role: Union[RoleType, None],
        affiliation: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Contact` record in an IODI manner.

        Args:
            person_id (int): The linked `Person` record primary-key ID.
            role (RoleType): The investigator role-type.
            affiliation (str): The investigator affiliation.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Investigator` record.
        """

        # Create and populate a `Investigator` object so that we can retrieve
        # the MD5 hash.
        obj = Investigator()
        obj.person_id = person_id
        obj.role = role
        obj.affiliation = affiliation

        statement = insert(
            Investigator,
            values={
                "person_id": obj.person_id,
                "role": obj.role,
                "affiliation": obj.affiliation,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Investigator,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Investigator
            return obj.investigator_id

    @return_first_item
    @with_session_scope()
    def iodu_location(
        self,
        facility_id: Union[int, None],
        status: Union[RecruitmentStatusType, None],
        contact_primary_id: Union[int, None],
        contact_backup_id: Union[int, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Location` record in an IODU manner.

        Args:
            facility_id (int): The linked `Facility` record primary-key ID.
            status (RoleType): The location recruitment-status-type.
            contact_primary_id (str): The linked primary `Contact` record.
            contact_backup_id (str): The linked backup `Contact` record.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Location` record.
        """

        obj = Location()
        obj.facility_id = facility_id
        obj.status = status
        obj.contact_primary_id = contact_primary_id
        obj.contact_backup_id = contact_backup_id

        statement = insert(
            Location,
            values={
                "facility_id": obj.facility_id,
                "status": obj.status,
                "contact_primary_id": obj.contact_primary_id,
                "contact_backup_id": obj.contact_backup_id,
                "md5": obj.md5,
            }
        ).on_conflict_do_update(
            index_elements=["md5"],
            set_={
                "status": obj.status,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Location,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Location
            return obj.location_id

    @return_first_item
    @with_session_scope()
    def iodi_location_investigator(
        self,
        location_id: int,
        investigator_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `LocationInvestigator` record in an IODI manner.

        Args:
            location_id (int): The linked `Location` record primary-key ID.
            investigator_id (int): The linked `Investigator` record primary-key
                ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `LocationInvestigator` record.
        """

        obj = LocationInvestigator()
        obj.location_id = location_id
        obj.investigator_id = investigator_id

        statement = insert(
            LocationInvestigator,
            values={
                "location_id": obj.location_id,
                "investigator_id": obj.investigator_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=LocationInvestigator,
                attrs_names_values={
                    "location_id": obj.location_id,
                    "investigator_id": obj.investigator_id,
                },
                session=session,
            )  # type: LocationInvestigator
            return obj.location_investigator_id

    @return_first_item
    @with_session_scope()
    def iodi_oversight_info(
        self,
        has_dmc: Union[bool, None],
        is_fda_regulated_drug: Union[bool, None],
        is_fda_regulated_device: Union[bool, None],
        is_unapproved_device: Union[bool, None],
        is_ppsd: Union[bool, None],
        is_us_export: Union[bool, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `OversightInfo` record in an IODI manner.

        Args:
            has_dmc (bool): Whether the study has DMC.
            is_fda_regulated_drug (bool): Whether the study involves an FDA
                regulated drug.
            is_fda_regulated_device (bool): Whether the study involves an FDA
                regulated device.
            is_unapproved_device (bool): Whether the study involves an
                unapproved device.
            is_ppsd (bool): Whether the study is PPSD.
            is_us_export (bool): Whether the study involves a US export.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `OversightInfo` record.
        """

        obj = OversightInfo()
        obj.has_dmc = has_dmc
        obj.is_fda_regulated_drug = is_fda_regulated_drug
        obj.is_fda_regulated_device = is_fda_regulated_device
        obj.is_unapproved_device = is_unapproved_device
        obj.is_ppsd = is_ppsd
        obj.is_us_export = is_us_export

        statement = insert(
            OversightInfo,
            values={
                "has_dmc": obj.has_dmc,
                "is_fda_regulated_drug": obj.is_fda_regulated_drug,
                "is_fda_regulated_device": obj.is_fda_regulated_device,
                "is_unapproved_device": obj.is_unapproved_device,
                "is_ppsd": obj.is_ppsd,
                "is_us_export": obj.is_us_export,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_expanded_access_info(
        self,
        expanded_access_type_individual: Union[bool, None],
        expanded_access_type_intermediate: Union[bool, None],
        expanded_access_type_treatment: Union[bool, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `ExpandedAccessInfo` record in an IODI manner.

        Args:
            expanded_access_type_individual (bool): Whether the study has
                individual expanded access.
            expanded_access_type_intermediate (bool): Whether the study has
                intermediate expanded access.
            expanded_access_type_treatment (bool): Whether the study has
                treatment expanded access.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `ExpandedAccessInfo` record.
        """

        obj = ExpandedAccessInfo
        obj.expanded_access_type_individual = expanded_access_type_individual
        obj.expanded_access_type_intermediate = (
            expanded_access_type_intermediate
        )
        obj.expanded_access_type_treatment = expanded_access_type_treatment

        statement = insert(
            ExpandedAccessInfo,
            values={
                "individual": obj.expanded_access_type_individual,
                "intermediate": obj.expanded_access_type_intermediate,
                "treatment": obj.expanded_access_type_treatment,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_study_design_info(
        self,
        allocation: Union[str, None],
        intervention_model: Union[str, None],
        intervention_model_description: Union[str, None],
        primary_purpose: Union[str, None],
        observational_model: Union[str, None],
        time_perspective: Union[str, None],
        masking: Union[str, None],
        masking_description: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyDesignInfo` record in an IODI manner.

        Args:
            allocation (str): Study allocation.
            intervention_model (str): Study intervention model.
            intervention_model_description (str): Study intervention model
                description.
            primary_purpose (str): Study primary purpose.
            observational_model (str): Study observational model.
            time_perspective (str): Study time perspective.
            masking (str): Study masking.
            masking_description (str): Study masking description.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyDesignInfo` record.
        """

        obj = StudyDesignInfo
        obj.allocation = allocation
        obj.intervention_model = intervention_model
        obj.intervention_model_description = intervention_model_description
        obj.primary_purpose = primary_purpose
        obj.observational_model = observational_model
        obj.time_perspective = time_perspective
        obj.masking = masking
        obj.masking_description = masking_description

        statement = insert(
            StudyDesignInfo,
            values={
                "allocation": obj.allocation,
                "intervention_model": obj.intervention_model,
                "intervention_model_description": (
                    obj.intervention_model_description
                ),
                "primary_purpose": obj.primary_purpose,
                "observational_model": obj.observational_model,
                "time_perspective": obj.time_perspective,
                "masking": obj.masking,
                "masking_description": obj.masking_description,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_protocol_outcome(
        self,
        measure: str,
        time_frame: Union[str, None],
        description: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `ProtocolOutcome` record in an IODI manner.

        Args:
            measure (str): Protocol outcome measure.
            time_frame (str): Protocol outcome time-frame.
            description (str): Protocol description.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `ProtocolOutcome` record.
        """

        obj = ProtocolOutcome()
        obj.measure = measure
        obj.time_frame = time_frame
        obj.description = description

        statement = insert(
            ProtocolOutcome,
            values={
                "measure": obj.measure,
                "time_frame": obj.time_frame,
                "description": obj.description,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_enrollment(
        self,
        value: str,
        enrollment_type: Union[ActualType, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Enrollment` record in an IODI manner.

        Args:
            value (str): The enrollment value.
            enrollment_type (ActualType): The enrollment type.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Enrollment` record.
        """

        obj = Enrollment()
        obj.value = value
        obj.enrollment_type = enrollment_type

        statement = insert(
            Enrollment,
            values={
                "value": obj.value,
                "type": obj.enrollment_type,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_arm_group(
        self,
        label: str,
        arm_group_type: Union[str, None],
        description: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `ArmGroup` record in an IODI manner.

        Args:
            label (str): The arm-group label.
            arm_group_type (str): The arm-group type.
            description (str): The arm-group description.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `ArmGroup` record.
        """

        obj = ArmGroup()
        obj.label = label
        obj.arm_group_type = arm_group_type
        obj.description = description

        statement = insert(
            ArmGroup,
            values={
                "label": label,
                "type": arm_group_type,
                "description": description,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_intervention(
        self,
        intervention_type: InterventionType,
        name: str,
        description: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Intervention` record in an IODI manner.

        Args:
            intervention_type (InterventionType): The intervention type.
            name (str): The intervention name.
            description (str): The intervention description.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Intervention` record.
        """

        obj = Intervention()
        obj.intervention_type = intervention_type
        obj.name = name
        obj.description = description

        statement = insert(
            Intervention,
            values={
                "type": obj.intervention_type,
                "name": obj.name,
                "description": obj.description,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Intervention,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Intervention
            return obj.intervention_id

    @return_first_item
    @with_session_scope()
    def iodi_alias(
        self,
        alias: str,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Alias` record in an IODI manner.

        Args:
            alias (str): The alias.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Alias` record.
        """

        # Create and populate a `Alias` object so that we can retrieve
        # the MD5 hash.
        obj = Alias()
        obj.alias = alias

        statement = insert(
            Alias,
            values={
                "alias": obj.alias,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Alias,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: Alias
            return obj.alias_id

    @return_first_item
    @with_session_scope()
    def iodi_intervention_alias(
        self,
        intervention_id: int,
        alias_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `InterventionAlias` record in an IODI manner.

        Args:
            intervention_id (int): The linked `Intervention` record
                primary-key ID.
            alias_id (int): The linked `Alias` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `InterventionAlias` record.
        """

        obj = InterventionAlias()
        obj.intervention_id = intervention_id
        obj.alias_id = alias_id

        statement = insert(
            InterventionAlias,
            values={
                "intervention_id": obj.intervention_id,
                "alias_id": obj.alias_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=InterventionAlias,
                attrs_names_values={
                    "intervention_id": obj.intervention_id,
                    "alias_id": obj.alias_id,
                },
                session=session,
            )  # type: InterventionAlias
            return obj.intervention_alias_id

    @return_first_item
    @with_session_scope()
    def iodi_intervention_arm_group(
        self,
        intervention_id: int,
        arm_group_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `InterventionArmGroup` record in an IODI manner.

        Args:
            intervention_id (int): The linked `Intervention` record
                primary-key ID.
            arm_group_id (int): The linked `ArmGroup` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `InterventionArmGroup` record.
        """

        obj = InterventionArmGroup()
        obj.intervention_id = intervention_id
        obj.arm_group_id = arm_group_id

        statement = insert(
            InterventionArmGroup,
            values={
                "intervention_id": obj.intervention_id,
                "arm_group_id": obj.arm_group_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=InterventionArmGroup,
                attrs_names_values={
                    "intervention_id": obj.intervention_id,
                    "arm_group_id": obj.arm_group_id,
                },
                session=session,
            )  # type: InterventionArmGroup
            return obj.intervention_arm_group_id

    @return_first_item
    @with_session_scope()
    def iodi_eligibility(
        self,
        study_pop: Union[str, None],
        sampling_method: Union[SamplingMethodType, None],
        criteria: Union[str, None],
        gender: Union[GenderType, None],
        gender_based: Union[bool, None],
        gender_description: Union[str, None],
        minimum_age: Union[str, None],
        maximum_age: Union[str, None],
        healthy_volunteers: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Eligibility` record in an IODI manner.

        Args:
            study_pop (str): The eligibility study population.
            sampling_method (SamplingMethodType): The eligibility sampling
                method type.
            criteria (str): The eligibility study population.
            gender (GenderType): The eligibility gender-type.
            gender_based (bool): Whether the study is gender-based.
            gender_description (str): The eligibility gender description.
            minimum_age (str): The eligibility minimum-age.
            maximum_age (str): The eligibility maximum-age.
            healthy_volunteers (str): The description of healthy volunteers in
                the study.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Eligibility` record.
        """

        obj = Eligibility()
        obj.study_pop = study_pop
        obj.sampling_method = sampling_method
        obj.criteria = criteria
        obj.gender = gender
        obj.gender_based = gender_based
        obj.gender_description = gender_description
        obj.minimum_age = minimum_age
        obj.maximum_age = maximum_age
        obj.healthy_volunteers = healthy_volunteers

        statement = insert(
            Eligibility,
            values={
                "study_pop": obj.study_pop,
                "sampling_method": obj.sampling_method,
                "criteria": obj.criteria,
                "gender": obj.gender,
                "gender_based": obj.gender_based,
                "gender_description": obj.gender_description,
                "minimum_age": obj.minimum_age,
                "maximum_age": obj.maximum_age,
                "healthy_volunteers": obj.healthy_volunteers,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodu_reference(
        self,
        citation: Union[str, None],
        pmid: Union[int, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Reference` record in an IODU manner.

        Args:
            citation (str): The citation.
            pmid (int): The reference PMID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Reference` record.
        """

        obj = Reference()
        obj.citation = citation
        obj.pmid = pmid

        statement = insert(
            Reference,
            values={
                "citation": obj.citation,
                "pmid": obj.pmid,
            }
        ).on_conflict_do_update(
            index_elements=["pmid"],
            set_={
                "citation": obj.citation,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=Reference,
                attrs_names_values={
                    "pmid": obj.pmid,
                },
                session=session,
            )  # type: Reference
            return obj.reference_id

    @return_first_item
    @with_session_scope()
    def iodi_responsible_party(
        self,
        name_title: Union[str, None],
        organization: Union[str, None],
        responsible_party_type: Union[ResponsiblePartyType, None],
        investigator_affiliation: Union[str, None],
        investigator_full_name: Union[str, None],
        investigator_title: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `ResponsibleParty` record in an IODI manner.

        Args:
            name_title (str): The name/title of the responsible party.
            organization (str): The organization of the responsible party.
            responsible_party_type (ResponsiblePartyType): The type of the
                responsible party.
            investigator_affiliation (str): The investigator affiliation of the
                responsible party.
            investigator_full_name (str): The investigator full name of the
                responsible party.
            investigator_title (str): The investigator title of the
                responsible party.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `ResponsibleParty` record.
        """

        obj = ResponsibleParty()
        obj.name_title = name_title
        obj.organization = organization
        obj.responsible_party_type = responsible_party_type
        obj.investigator_affiliation = investigator_affiliation
        obj.investigator_full_name = investigator_full_name
        obj.investigator_title = investigator_title

        statement = insert(
            ResponsibleParty,
            values={
                "name_title": obj.name_title,
                "organization": obj.organization,
                "type": obj.responsible_party_type,
                "investigator_affiliation": obj.investigator_affiliation,
                "investigator_full_name": obj.investigator_full_name,
                "investigator_title": obj.investigator_title,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_mesh_term(
        self,
        term: str,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `MeshTerm` record in an IODI manner.

        Args:
            term (str): The MeSH term.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `MeshTerm` record.
        """

        # Create and populate a `MeshTerm` object so that we can retrieve the
        # MD5 hash.
        obj = MeshTerm()
        obj.term = term

        statement = insert(
            MeshTerm,
            values={
                "term": obj.term,
                "md5": obj.md5,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=MeshTerm,
                attr_name="md5",
                attr_value=obj.md5,
                session=session,
            )  # type: MeshTerm
            return obj.mesh_term_id

    @return_first_item
    @with_session_scope()
    def iodi_patient_data(
        self,
        sharing_ipd: str,
        ipd_description: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `PatientData` record in an IODI manner.

        Args:
            sharing_ipd (str): The sharing IPD.
            ipd_description (str): The IPD description.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `PatientData` record.
        """

        obj = PatientData()
        obj.sharing_ipd = sharing_ipd
        obj.ipd_description = ipd_description

        statement = insert(
            PatientData,
            values={
                "sharing_ipd": obj.sharing_ipd,
                "ipd_description": obj.ipd_description,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_study_doc(
        self,
        doc_id: Union[str, None],
        doc_type: Union[str, None],
        doc_url: Union[str, None],
        doc_comment: Union[str, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyDoc` record in an IODI manner.

        Args:
            doc_id (str): The study-doc ID.
            doc_type (str): The study-doc type.
            doc_url (str): The study-doc URL.
            doc_comment (str): The study-doc comment.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyDoc` record.
        """

        obj = StudyDoc()
        obj.doc_id = doc_id
        obj.doc_type = doc_type
        obj.doc_url = doc_url
        obj.doc_comment = doc_comment

        statement = insert(
            StudyDoc,
            values={
                "doc_id": obj.doc_id,
                "doc_type": obj.doc_type,
                "doc_url": obj.doc_url,
                "doc_comment": obj.doc_comment,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodi_study_dates(
        self,
        study_first_submitted: Union[datetime.date, None],
        study_first_submitted_qc: Union[datetime.date, None],
        study_first_posted: Union[datetime.date, None],
        results_first_submitted: Union[datetime.date, None],
        results_first_submitted_qc: Union[datetime.date, None],
        results_first_posted: Union[datetime.date, None],
        disposition_first_submitted: Union[datetime.date, None],
        disposition_first_submitted_qc: Union[datetime.date, None],
        disposition_first_posted: Union[datetime.date, None],
        last_update_submitted: Union[datetime.date, None],
        last_update_submitted_qc: Union[datetime.date, None],
        last_update_posted: Union[datetime.date, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyDates` record in an IODI manner.

        Args:
            study_first_submitted (datetime.date): The date the study was
                submitted.
            study_first_submitted_qc (datetime.date): The date the study was
                submitted for quality-control.
            study_first_posted (datetime.date): The date the study was
                first-posted.
            results_first_submitted (datetime.date): The date the results were
                first-submitted.
            results_first_submitted_qc (datetime.date): The date the results
                were submitted for quality-control.
            results_first_posted (datetime.date): The date the results were
                first-posted.
            disposition_first_submitted (datetime.date): The date the
                disposition was first-submitted.
            disposition_first_submitted_qc (datetime.date): The date the
                disposition was first-submitted for quality-control.
            disposition_first_posted (datetime.date): The date the
                disposition was first-posted.
            last_update_submitted (datetime.date): The date the latest update
                was submitted.
            last_update_submitted_qc (datetime.date): The date the latest update
                was submitted for quality-control.
            last_update_posted (datetime.date): The date the latest update
                was posted.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyDates` record.
        """

        obj = StudyDates()
        obj.study_first_submitted = study_first_submitted
        obj.study_first_submitted_qc = study_first_submitted_qc
        obj.study_first_posted = study_first_posted
        obj.results_first_submitted = results_first_submitted
        obj.results_first_submitted_qc = results_first_submitted_qc
        obj.results_first_posted = results_first_posted
        obj.disposition_first_posted = disposition_first_posted
        obj.disposition_first_submitted = disposition_first_submitted
        obj.disposition_first_submitted_qc = disposition_first_submitted_qc
        obj.disposition_first_posted = disposition_first_posted
        obj.last_update_submitted = last_update_submitted
        obj.last_update_submitted_qc = last_update_submitted_qc
        obj.last_update_posted = last_update_posted

        statement = insert(
            StudyDates,
            values={
                "study_first_submitted": obj.study_first_submitted,
                "study_first_submitted_qc": obj.study_first_submitted_qc,
                "study_first_posted": obj.study_first_posted,
                "results_first_submitted": obj.results_first_submitted,
                "results_first_submitted_qc": obj.results_first_submitted_qc,
                "results_first_posted": obj.results_first_posted,
                "disposition_first_submitted": obj.disposition_first_submitted,
                "disposition_first_submitted_qc": (
                    obj.disposition_first_submitted_qc
                ),
                "disposition_first_posted": obj.disposition_first_posted,
                "last_update_submitted": obj.last_update_submitted,
                "last_update_submitted_qc": obj.last_update_submitted_qc,
                "last_update_posted": obj.last_update_posted,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        return result.inserted_primary_key

    @return_first_item
    @with_session_scope()
    def iodu_study(
        self,
        org_study_id: Union[str, None],
        secondary_id: Union[str, None],
        nct_id: str,
        brief_title: str,
        acronym: Union[str, None],
        official_title: Union[str, None],
        source: str,
        oversight_info_id: Union[int, None],
        brief_summary: Union[str, None],
        detailed_description: Union[str, None],
        overall_status:  OverallStatusType,
        last_known_status: Union[OverallStatusType, None],
        why_stopped: Union[str, None],
        start_date: Union[datetime.date, None],
        completion_date: Union[datetime.date, None],
        primary_completion_date: Union[datetime.date, None],
        verification_date: Union[datetime.date, None],
        phase: PhaseType,
        study_type: StudyType,
        expanded_access_info_id: Union[int, None],
        study_design_info_id: Union[int, None],
        target_duration: Union[str, None],
        enrollment_id: Union[int, None],
        biospec_retention: Union[BiospecRetentionType, None],
        biospec_description: Union[str, None],
        eligibility_id: Union[int, None],
        contact_primary_id: Union[int, None],
        contact_backup_id: Union[int, None],
        study_dates_id: int,
        responsible_party_id: Union[int, None],
        patient_data_id: Union[int, None],
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `Study` record in an IODU manner.

        Args:
            org_study_id (str): The organizational study ID.
            secondary_id (str): A secondary study ID.
            nct_id (str): The NCT study ID.
            brief_title (str): A brief study title.
            acronym (str): The study acronym.
            official_title (str): The official study title.
            source (str): The study source.
            oversight_info_id (int): The linked `OversightInfo` record
                primary-key ID.
            brief_summary (str): The brief study summary.
            detailed_description (str): The detailed summary description.
            overall_status: (OverallStatusType): The study overall status.
            last_known_status (OverallStatusType): THe study last-known status.
            why_stopped (str): Why the study was stopped (if applicable).
            start_date: (datetime.date): The date the study will start.
            completion_date: (datetime.date): The date the study will be
                completed.
            primary_completion_date: (datetime.date): The date of the study
                primary-completion.
            verification_date: (datetime.date): The date the study will be
                verified.
            phase (PhaseType): The study phase.
            study_type (StudyType): The study type.
            expanded_access_info_id (int): The linked `ExpandedAccessInfo`
                record primary-key ID.
            study_design_info_id (int): The linked `StudyDesignInfo` record
                primary-key ID.
            target_duration (str): The study target duration.
            enrollment_id (int): The linked `Enrollment` record primary-key ID.
            biospec_retention (BiospecRetentionType): The study
                biospec-retention type.
            biospec_description (str): The study biospec description.
            eligibility_id (int): The linked `Eligibility` record
                primary-key ID.
            contact_primary_id (int): The linked `Contact` record
                primary-key ID for the study's primary contact.
            contact_backup_id (int): The linked `Contact` record
                primary-key ID for the study's backup contact.
            study_dates_id (int): The linked `StudyDates` record
                primary-key ID.
            responsible_party_id (int): The linked `ResponsibleParty` record
                primary-key ID.
            patient_data_id (int): The linked `Patientdata` record
                primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `Study` record.
        """

        obj = Study()
        obj.org_study_id = org_study_id
        obj.secondary_id = secondary_id
        obj.nct_id = nct_id
        obj.brief_title = brief_title
        obj.acronym = acronym
        obj.official_title = official_title
        obj.source = source
        obj.oversight_info_id = oversight_info_id
        obj.brief_summary = brief_summary
        obj.detailed_description = detailed_description
        obj.overall_status = overall_status
        obj.last_known_status = last_known_status
        obj.why_stopped = why_stopped
        obj.start_date = start_date
        obj.completion_date = completion_date
        obj.primary_completion_date = primary_completion_date
        obj.verification_date = verification_date
        obj.phase = phase
        obj.study_type = study_type
        obj.expanded_access_info_id = expanded_access_info_id
        obj.study_design_info_id = study_design_info_id
        obj.target_duration = target_duration
        obj.enrollment_id = enrollment_id
        obj.biospec_retention = biospec_retention
        obj.biospec_description = biospec_description
        obj.eligibility_id = eligibility_id
        obj.contact_primary_id = contact_primary_id
        obj.contact_backup_id = contact_backup_id
        obj.study_dates_id = study_dates_id
        obj.responsible_party_id = responsible_party_id
        obj.patient_data_id = patient_data_id

        statement = insert(
            Study,
            values={
                "org_study_id": obj.org_study_id,
                "secondary_id": obj.secondary_id,
                "nct_id": obj.nct_id,
                "brief_title": obj.brief_title,
                "acronym": obj.acronym,
                "official_title": obj.official_title,
                "source": obj.source,
                "oversight_info_id": obj.oversight_info_id,
                "brief_summary": obj.brief_summary,
                "detailed_description": obj.detailed_description,
                "overall_status": obj.overall_status,
                "last_known_status": obj.last_known_status,
                "why_stopped": obj.why_stopped,
                "start_date": obj.start_date,
                "completion_date": obj.completion_date,
                "primary_completion_date": obj.primary_completion_date,
                "verification_date": obj.verification_date,
                "phase": obj.phase,
                "study_type": obj.study_type,
                "expanded_access_info_id": obj.expanded_access_info_id,
                "study_design_info_id": obj.study_design_info_id,
                "target_duration": obj.target_duration,
                "enrollment_id": obj.enrollment_id,
                "biospec_retention": obj.biospec_retention,
                "biospec_description": obj.biospec_description,
                "eligibility_id": obj.eligibility_id,
                "contact_primary_id": obj.contact_primary_id,
                "contact_backup_id": obj.contact_backup_id,
                "study_dates_id": obj.study_dates_id,
                "responsible_party_id": obj.responsible_party_id,
                "patient_data_id": obj.patient_data_id,
            }
        ).on_conflict_do_update(
            index_elements=["nct_id"],
            set_={
                "org_study_id": obj.org_study_id,
                "secondary_id": obj.secondary_id,
                "brief_title": obj.brief_title,
                "acronym": obj.acronym,
                "official_title": obj.official_title,
                "source": obj.source,
                "oversight_info_id": obj.oversight_info_id,
                "brief_summary": obj.brief_summary,
                "detailed_description": obj.detailed_description,
                "overall_status": obj.overall_status,
                "last_known_status": obj.last_known_status,
                "why_stopped": obj.why_stopped,
                "start_date": obj.start_date,
                "completion_date": obj.completion_date,
                "primary_completion_date": obj.primary_completion_date,
                "verification_date": obj.verification_date,
                "phase": obj.phase,
                "study_type": obj.study_type,
                "expanded_access_info_id": obj.expanded_access_info_id,
                "study_design_info_id": obj.study_design_info_id,
                "target_duration": obj.target_duration,
                "enrollment_id": obj.enrollment_id,
                "biospec_retention": obj.biospec_retention,
                "biospec_description": obj.biospec_description,
                "eligibility_id": obj.eligibility_id,
                "contact_primary_id": obj.contact_primary_id,
                "contact_backup_id": obj.contact_backup_id,
                "study_dates_id": obj.study_dates_id,
                "responsible_party_id": obj.responsible_party_id,
                "patient_data_id": obj.patient_data_id,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attr(
                orm_class=Study,
                attr_name="nct_id",
                attr_value=obj.nct_id,
                session=session,
            )  # type: Study
            return obj.study_id

    @return_first_item
    @with_session_scope()
    def iodi_study_alias(
        self,
        study_id: int,
        alias_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyAlias` record in an IODI manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            alias_id (int): The linked `Alias` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyAlias` record.
        """

        obj = StudyAlias()
        obj.study_id = study_id
        obj.alias_id = alias_id

        statement = insert(
            StudyAlias,
            values={
                "study_id": obj.study_id,
                "alias_id": obj.alias_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyAlias,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "alias_id": obj.alias_id,
                },
                session=session,
            )  # type: StudyAlias
            return obj.study_alias_id

    @return_first_item
    @with_session_scope()
    def iodu_study_sponsor(
        self,
        study_id: int,
        sponsor_id: int,
        sponsor_type: SponsorType,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudySponsor` record in an IODU manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            sponsor_id (int): The linked `Sponsor` record primary-key ID.
            sponsor_type (SponsorType): An enumeration member denoting the
                sponsor type.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudySponsor` record.
        """

        obj = StudySponsor()
        obj.study_id = study_id
        obj.sponsor_id = sponsor_id
        obj.sponsor_type = sponsor_type

        statement = insert(
            StudySponsor,
            values={
                "study_id": obj.study_id,
                "sponsor_id": obj.sponsor_id,
                "type": obj.sponsor_type,
            }
        ).on_conflict_do_update(
            index_elements=["study_id", "sponsor_id"],
            set_={
                "type": obj.sponsor_type,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudySponsor,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "sponsor_id": obj.sponsor_id,
                },
                session=session,
            )  # type: StudySponsor
            return obj.study_sponsor_id

    @return_first_item
    @with_session_scope()
    def iodu_study_outcome(
        self,
        study_id: int,
        protocol_outcome_id: int,
        outcome_type: OutcomeType,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyOutcome` record in an IODU manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            protocol_outcome_id (int): The linked `Outcome` record primary-key
                ID.
            outcome_type (OutcomeType): The linked `Outcome` type.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyOutcome` record.
        """

        obj = StudyOutcome()
        obj.study_id = study_id
        obj.protocol_outcome_id = protocol_outcome_id
        obj.outcome_type = outcome_type

        statement = insert(
            StudyOutcome,
            values={
                "study_id": obj.study_id,
                "protocol_outcome_id": obj.protocol_outcome_id,
                "type": obj.outcome_type,
            }
        ).on_conflict_do_update(
            index_elements=["study_id", "protocol_outcome_id"],
            set_={
                "type": obj.outcome_type,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyOutcome,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "protocol_outcome_id": obj.protocol_outcome_id,
                },
                session=session,
            )  # type: StudyOutcome
            return obj.study_primary_outcome_id

    @return_first_item
    @with_session_scope()
    def iodi_study_condition(
        self,
        study_id: int,
        condition_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyCondition` record in an IODI manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            condition_id (int): The linked `Condition` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyCondition` record.
        """

        obj = StudyCondition()
        obj.study_id = study_id
        obj.condition_id = condition_id

        statement = insert(
            StudyCondition,
            values={
                "study_id": obj.study_id,
                "condition_id": obj.condition_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyCondition,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "condition_id": obj.condition_id,
                },
                session=session,
            )  # type: StudyCondition
            return obj.study_condition_id

    @return_first_item
    @with_session_scope()
    def iodi_study_arm_group(
        self,
        study_id: int,
        arm_group_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyArmGroup` record in an IODI manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            arm_group_id (int): The linked `ArmGroup` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyArmGroup` record.
        """

        obj = StudyArmGroup()
        obj.study_id = study_id
        obj.arm_group_id = arm_group_id

        statement = insert(
            StudyArmGroup,
            values={
                "study_id": obj.study_id,
                "arm_group_id": obj.arm_group_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyArmGroup,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "arm_group_id": obj.arm_group_id,
                },
                session=session,
            )  # type: StudyArmGroup
            return obj.study_arm_group_id

    @return_first_item
    @with_session_scope()
    def iodi_study_intervention(
        self,
        study_id: int,
        intervention_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyIntervention` record in an IODI manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            intervention_id (int): The linked `Intervention` record primary-key
                ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyIntervention` record.
        """

        obj = StudyIntervention()
        obj.study_id = study_id
        obj.intervention_id = intervention_id

        statement = insert(
            StudyIntervention,
            values={
                "study_id": obj.study_id,
                "intervention_id": obj.intervention_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyIntervention,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "intervention_id": obj.intervention_id,
                },
                session=session,
            )  # type: StudyIntervention
            return obj.study_intervention_id

    @return_first_item
    @with_session_scope()
    def iodi_study_investigator(
        self,
        study_id: int,
        investigator_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyInvestigator` record in an IODI manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            investigator_id (int): The linked `Investigator` record primary-key
                ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyInvestigator` record.
        """

        obj = StudyInvestigator()
        obj.study_id = study_id
        obj.investigator_id = investigator_id

        statement = insert(
            StudyInvestigator,
            values={
                "study_id": obj.study_id,
                "investigator_id": obj.investigator_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyInvestigator,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "investigator_id": obj.investigator_id,
                },
                session=session,
            )  # type: StudyInvestigator
            return obj.study_investigator_id

    @return_first_item
    @with_session_scope()
    def iodi_study_location(
        self,
        study_id: int,
        location_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyLocation` record in an IODI manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            location_id (int): The linked `Location` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyLocation` record.
        """

        obj = StudyLocation()
        obj.study_id = study_id
        obj.location_id = location_id

        statement = insert(
            StudyLocation,
            values={
                "study_id": obj.study_id,
                "location_id": obj.location_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyLocation,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "location_id": obj.location_id,
                },
                session=session,
            )  # type: StudyLocation
            return obj.study_location_id

    @return_first_item
    @with_session_scope()
    def iodu_study_reference(
        self,
        study_id: int,
        reference_id: int,
        reference_type: ReferenceType,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyReference` record in an IODU manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            reference_id (int): The linked `Reference` record primary-key ID.
            reference_type (ReferenceType): The reference type.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyReference` record.
        """

        obj = StudyReference()
        obj.study_id = study_id
        obj.reference_id = reference_id
        obj.reference_type = reference_type

        statement = insert(
            StudyReference,
            values={
                "study_id": obj.study_id,
                "reference_id": obj.reference_id,
                "type": obj.reference_type,
            }
        ).on_conflict_do_update(
            index_elements=["study_id", "reference_id"],
            set_={
                "type": obj.reference_type,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyReference,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "reference_id": obj.reference_id,
                },
                session=session,
            )  # type: StudyReference
            return obj.study_reference_id

    @return_first_item
    @with_session_scope()
    def iodi_study_keyword(
        self,
        study_id: int,
        keyword_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyKeyword` record in an IODI manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            keyword_id (int): The linked `Keyword` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyKeyword` record.
        """

        obj = StudyKeyword()
        obj.study_id = study_id
        obj.keyword_id = keyword_id

        statement = insert(
            StudyKeyword,
            values={
                "study_id": obj.study_id,
                "keyword_id": obj.keyword_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyKeyword,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "keyword_id": obj.keyword_id,
                },
                session=session,
            )  # type: StudyKeyword
            return obj.study_keyword_id

    @return_first_item
    @with_session_scope()
    def iodu_study_mesh_term(
        self,
        study_id: int,
        mesh_term_id: int,
        mesh_term_type: MeshTermType,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyMeshTerm` record in an IODU manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            mesh_term_id (int): The linked `MeshTerm` record primary-key ID.
            mesh_term_type (MeshTermType): The mesh-term type.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyMeshTerm` record.
        """

        obj = StudyMeshTerm()
        obj.study_id = study_id
        obj.mesh_term_id = mesh_term_id
        obj.mesh_term_type = mesh_term_type

        statement = insert(
            StudyMeshTerm,
            values={
                "study_id": obj.study_id,
                "mesh_term_id": obj.mesh_term_id,
                "type": obj.mesh_term_type,
            }
        ).on_conflict_do_update(
            index_elements=["study_id", "mesh_term_id"],
            set_={
                "type": obj.mesh_term_type,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyMeshTerm,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "mesh_term_id": obj.mesh_term_id,
                },
                session=session,
            )  # type: StudyMeshTerm
            return obj.study_mesh_term_id

    @return_first_item
    @with_session_scope()
    def iodi_study_study_doc(
        self,
        study_id: int,
        study_doc_id: int,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyStudyDoc` record in an IODI manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            study_doc_id (int): The linked `StudyDoc` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyStudyDoc` record.
        """

        obj = StudyStudyDoc()
        obj.study_id = study_id
        obj.study_doc_id = study_doc_id

        statement = insert(
            StudyStudyDoc,
            values={
                "study_id": obj.study_id,
                "study_doc_id": obj.study_doc_id,
            }
        ).on_conflict_do_nothing()  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyStudyDoc,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "study_doc_id": obj.study_doc_id,
                },
                session=session,
            )  # type: StudyStudyDoc
            return obj.study_study_doc_id

    @return_first_item
    @with_session_scope()
    def iodu_study_facility(
        self,
        study_id: int,
        facility_id: int,
        facility_canonical_id: Optional[int] = None,
        session: Optional[sqlalchemy.orm.Session] = None,
    ) -> int:
        """Creates a new `StudyFacility` record in an IODU manner.

        Args:
            study_id (int): The linked `Study` record primary-key ID.
            facility_id (int): The linked `Facility` record primary-key ID.
            facility_canonical_id (Optional[int]): The linked
                `FacilityCanonical` record primary-key ID.
            session (sqlalchemy.orm.Session, optional): An SQLAlchemy session
                through which the record will be added. Defaults to `None` in
                which case a new session is automatically created and terminated
                upon completion.

        Returns:
            int: The primary key ID of the `StudyFacility` record.
        """

        obj = StudyFacility()
        obj.study_id = study_id
        obj.facility_id = facility_id
        obj.facility_canonical_id = facility_canonical_id

        statement = insert(
            StudyMeshTerm,
            values={
                "study_id": obj.study_id,
                "facility_id": obj.facility_id,
                "facility_canonical_id": obj.facility_canonical_id,
            }
        ).on_conflict_do_update(
            index_elements=["study_id", "facility_id"],
            set_={
                "facility_canonical_id": obj.facility_canonical_id,
            }
        )  # type: Insert

        result = session.execute(statement)  # type: ResultProxy

        if result.inserted_primary_key:
            return result.inserted_primary_key
        else:
            obj = self.get_by_attrs(
                orm_class=StudyFacility,
                attrs_names_values={
                    "study_id": obj.study_id,
                    "facility_id": obj.facility_id,
                },
                session=session,
            )  # type: StudyFacility
            return obj.study_facility_id
