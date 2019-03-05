# -*- coding: utf-8 -*-

"""
This module defines functions to create fixture records of different types under
the `clinicaltrials` schema.
"""

import datetime
from typing import Tuple, Dict, Optional

from fform.dals_ct import RecruitmentStatusType
from fform.dals_ct import RoleType
from fform.dals_ct import InterventionType
from fform.dals_ct import ActualType
from fform.dals_ct import SamplingMethodType
from fform.dals_ct import GenderType
from fform.dals_ct import ResponsiblePartyType
from fform.dals_ct import OverallStatusType
from fform.dals_ct import PhaseType
from fform.dals_ct import StudyType
from fform.dals_ct import BiospecRetentionType
from fform.dals_ct import AgencyClassType
from fform.dals_ct import DalClinicalTrials


def create_facility(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `facilities` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "name": "The Alfred",
        "city": "Melbourne",
        "state": "Victoria",
        "zip_code": "3000",
        "country": "Australia",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_facility(**refr)

    return obj_id, refr


def create_location(
    dal: DalClinicalTrials,
    facility_id: Optional[int] = None,
    contact_primary_id: Optional[int] = None,
    contact_backup_id: Optional[int] = None,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `locations` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.
        facility_id (int): The PK ID of the `facilities` record.
        contact_primary_id (int): The PK ID of the primary `contacts` record.
        contact_backup_id (int): The PK ID of the backup `contacts` record.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    if not facility_id:
        facility_id, _ = create_facility(dal=dal)

    if not contact_primary_id:
        person_01_id, _ = create_person(dal=dal, name_first="A")
        contact_primary_id, _ = create_contact(dal=dal, person_id=person_01_id)

    if not contact_backup_id:
        person_02_id, _ = create_person(dal=dal, name_first="B")
        contact_backup_id, _ = create_contact(dal=dal, person_id=person_02_id)

    refr = {
        "facility_id": facility_id,
        "status": RecruitmentStatusType.ACTIVE_NOT,
        "contact_primary_id": contact_primary_id,
        "contact_backup_id": contact_backup_id,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodu_location(**refr)

    return obj_id, refr


def create_person(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `persons` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "name_first": "John",
        "name_middle": "Malcolm",
        "name_last": "Doe",
        "degrees": "PhD",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_person(**refr)

    return obj_id, refr


def create_contact(
    dal: DalClinicalTrials,
    person_id: int,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `contacts` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.
        person_id (int): The PK ID of the `persons` record.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    if not person_id:
        person_id, _ = create_person(dal=dal)

    refr = {
        "person_id": person_id,
        "phone": "phone",
        "phone_ext": "phone_ext",
        "email": "email",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_contact(**refr)

    return obj_id, refr


def create_investigator(
    dal: DalClinicalTrials,
    person_id: Optional[int] = None,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `investigators` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.
        person_id (int): The PK ID of the `persons` record.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    if not person_id:
        person_id, _ = create_person(dal=dal)

    refr = {
        "person_id": person_id,
        "role": RoleType.DIRECTOR,
        "affiliation": "affiliation",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_investigator(**refr)

    return obj_id, refr


def create_intervention(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `interventions` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "intervention_type": InterventionType.BEHAVIORAL,
        "name": "name",
        "description": "description",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_intervention(**refr)

    return obj_id, refr


def create_alias(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `aliases` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "alias": "alias",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_alias(**refr)

    return obj_id, refr


def create_arm_group(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `arm_groups` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "label": "label",
        "arm_group_type": "arm_group_type",
        "description": "description",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_arm_group(**refr)

    return obj_id, refr


def create_patient_data(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `patient_data` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "sharing_ipd": "sharing_ipd",
        "ipd_description": "ipd_description",
        "ipd_time_frame": "ipd_time_frame",
        "ipd_access_criteria": "ipd_access_criteria",
        "ipd_url": "ipd_url",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_patient_data(**refr)

    return obj_id, refr


def create_enrollment(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `enrollments` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "value": 1,
        "enrollment_type": ActualType.ACTUAL,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_enrollment(**refr)

    return obj_id, refr


def create_study_design_info(
    dal: DalClinicalTrials,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `study_design_infos` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "allocation": "allocation",
        "intervention_model": "intervention_model",
        "intervention_model_description": "intervention_model_description",
        "primary_purpose": "primary_purpose",
        "observational_model": "observational_model",
        "time_perspective": "time_perspective",
        "masking": "masking",
        "masking_description": "masking_description",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_study_design_info(**refr)

    return obj_id, refr


def create_eligibility(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `eligibilities` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "study_pop": "study_pop",
        "sampling_method": SamplingMethodType.PROBABILITY,
        "criteria": "criteria",
        "gender": GenderType.ALL,
        "gender_based": False,
        "gender_description": "gender_description",
        "minimum_age": "1 year",
        "maximum_age": "10 years",
        "healthy_volunteers": "healthy_volunteers",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_eligibility(**refr)

    return obj_id, refr


def create_study_dates(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `study_dates` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "study_first_submitted": datetime.date(2019, 1, 1),
        "study_first_submitted_qc": datetime.date(2019, 1, 2),
        "study_first_posted": datetime.date(2019, 1, 3),
        "results_first_submitted": datetime.date(2019, 1, 4),
        "results_first_submitted_qc": datetime.date(2019, 1, 5),
        "results_first_posted": datetime.date(2019, 1, 6),
        "disposition_first_submitted": datetime.date(2019, 1, 7),
        "disposition_first_submitted_qc": datetime.date(2019, 1, 8),
        "disposition_first_posted": datetime.date(2019, 1, 9),
        "last_update_submitted": datetime.date(2019, 1, 10),
        "last_update_submitted_qc": datetime.date(2019, 1, 11),
        "last_update_posted": datetime.date(2019, 1, 12),
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_study_dates(**refr)

    return obj_id, refr


def create_responsible_party(
    dal: DalClinicalTrials,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `responsible_parties` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "name_title": "name_title",
        "organization": "organization",
        "responsible_party_type": ResponsiblePartyType.PRINCIPAL,
        "investigator_affiliation": "investigator_affiliation",
        "investigator_full_name": "investigator_full_name",
        "investigator_title": "investigator_title",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_responsible_party(**refr)

    return obj_id, refr


def create_expanded_access_info(
    dal: DalClinicalTrials,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `expanded_access_infos` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "expanded_access_type_individual": True,
        "expanded_access_type_intermediate": True,
        "expanded_access_type_treatment": True,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_expanded_access_info(**refr)

    return obj_id, refr


def create_oversight_info(
    dal: DalClinicalTrials,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `oversight_infos` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "has_dmc": True,
        "is_fda_regulated_drug": True,
        "is_fda_regulated_device": True,
        "is_unapproved_device": True,
        "is_ppsd": True,
        "is_us_export": True,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_oversight_info(**refr)

    return obj_id, refr


def create_study(
    dal: DalClinicalTrials,
    oversight_info_id: Optional[int] = None,
    expanded_access_info_id: Optional[int] = None,
    study_design_info_id: Optional[int] = None,
    enrollment_id: Optional[int] = None,
    eligibility_id: Optional[int] = None,
    contact_primary_id: Optional[int] = None,
    contact_backup_id: Optional[int] = None,
    study_dates_id: Optional[int] = None,
    responsible_party_id: Optional[int] = None,
    patient_data_id: Optional[int] = None,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `oversight_infos` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.
        oversight_info_id (int): The PK ID of the `oversight_infos` record.
        expanded_access_info_id (int): The PK ID of the `expanded_access_infos`
            record.
        study_design_info_id (int): The PK ID of the `study_design_infos`
            record.
        enrollment_id (int): The PK ID of the `enrollments` record.
        eligibility_id (int): The PK ID of the `eligibilities` record.
        contact_primary_id (int): The PK ID of the `contacts` record pertaining
            to the primary contact.
        contact_backup_id (int): The PK ID of the `contacts` record pertaining
            to the backup contact
        study_dates_id (int): The PK ID of the `study_dates` record.
        responsible_party_id (int): The PK ID of the `responsible_parties`
            record.
        patient_data_id (int): The PK ID of the `patient_datas` record.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    if not oversight_info_id:
        oversight_info_id, _ = create_oversight_info(dal=dal)

    if not expanded_access_info_id:
        expanded_access_info_id, _ = create_expanded_access_info(dal=dal)

    if not study_design_info_id:
        study_design_info_id, _ = create_study_design_info(dal=dal)

    if not enrollment_id:
        enrollment_id, _ = create_enrollment(dal=dal)

    if not eligibility_id:
        eligibility_id, _ = create_eligibility(dal=dal)

    if not contact_primary_id:
        person_01_id, _ = create_person(dal=dal, name_first="A")
        contact_primary_id, _ = create_contact(dal=dal, person_id=person_01_id)

    if not contact_backup_id:
        person_02_id, _ = create_person(dal=dal, name_first="B")
        contact_backup_id, _ = create_contact(dal=dal, person_id=person_02_id)

    if not study_dates_id:
        study_dates_id, _ = create_study_dates(dal=dal)

    if not responsible_party_id:
        responsible_party_id, _ = create_responsible_party(dal=dal)

    if not patient_data_id:
        patient_data_id, _ = create_patient_data(dal=dal)

    refr = {
        "org_study_id": "org_study_id",
        "nct_id": "nct_id",
        "brief_title": "brief_title",
        "acronym": "acronym",
        "official_title": "official_title",
        "source": "source",
        "oversight_info_id": oversight_info_id,
        "brief_summary": "brief_summary",
        "detailed_description": "detailed_description",
        "overall_status": OverallStatusType.ACTIVE_NOT,
        "last_known_status": OverallStatusType.APPROVED,
        "why_stopped": "why_stopped",
        "start_date": datetime.date(2019, 1, 1),
        "completion_date": datetime.date(2019, 1, 1),
        "primary_completion_date": datetime.date(2019, 1, 1),
        "verification_date": datetime.date(2019, 1, 1),
        "phase": PhaseType.PHASE_1,
        "study_type": StudyType.EXPANDED,
        "expanded_access_info_id": expanded_access_info_id,
        "study_design_info_id": study_design_info_id,
        "target_duration": "target_duration",
        "enrollment_id": enrollment_id,
        "biospec_retention": BiospecRetentionType.SAMPLES_W_DNA,
        "biospec_description": "biospec_description",
        "eligibility_id": eligibility_id,
        "contact_primary_id": contact_primary_id,
        "contact_backup_id": contact_backup_id,
        "study_dates_id": study_dates_id,
        "responsible_party_id": responsible_party_id,
        "patient_data_id": patient_data_id,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodu_study(**refr)

    return obj_id, refr


def create_sponsor(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `sponsors` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "agency": "agency",
        "agency_class": AgencyClassType.INDUSTRY,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_sponsor(**refr)

    return obj_id, refr


def create_protocol_outcome(
    dal: DalClinicalTrials,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `protocol_outcomes` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "measure": "measure",
        "time_frame": "time_frame",
        "description": "description",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_protocol_outcome(**refr)

    return obj_id, refr


def create_condition(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `conditions` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "condition": "condition",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_condition(**refr)

    return obj_id, refr


def create_reference(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `references` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "citation": "citation",
        "pmid": 1,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodu_reference(**refr)

    return obj_id, refr


def create_keyword(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `keywords` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "keyword": "keyword",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.iodi_keyword(**refr)

    return obj_id, refr


def create_study_doc(dal: DalClinicalTrials, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `study_docs` record.

    Args:
        dal (DalClinicalTrials): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "doc_id": "doc_id",
        "doc_type": "doc_type",
        "doc_url": "doc_url",
        "doc_comment": "doc_comment",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj_id = dal.insert_study_doc(**refr)

    return obj_id, refr
