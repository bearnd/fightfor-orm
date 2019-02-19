# -*- coding: utf-8 -*-

"""
This module defines functions to create fixture records of different types under
the `clinicaltrials` schema.
"""

from typing import Tuple, Dict

from fform.dals_ct import RecruitmentStatusType
from fform.dals_ct import RoleType
from fform.dals_ct import InterventionType
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
    facility_id: int,
    contact_primary_id: int,
    contact_backup_id: int,
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
    person_id: int,
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
