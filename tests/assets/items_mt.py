# -*- coding: utf-8 -*-

import datetime
from typing import Tuple, Dict, Optional

from fform.orm_mt import Term
from fform.orm_mt import DescriptorClassType
from fform.orm_mt import EntryCombinationType as Ect
from fform.orm_mt import SupplementalClassType
from fform.dals_mt import DalMesh


def create_term(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `terms` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "ui": "T000048",
        "name": "Abortifacients",
        "created": datetime.date(1991, 10, 9),
        "abbreviation": "abbreviation",
        "sort_version": "sort_version",
        "entry_version": "entry_version",
        "note": "note",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodu_term(**refr)

    return obj_id, refr


def create_thesaurus_id(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `thesaurus_ids` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "thesaurus_id": "POPLINE (1978)",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodi_thesaurus_id(**refr)

    return obj_id, refr


def create_concept(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `concepts` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "ui": "M0000033",
        "name": "Abortion, Incomplete",
        "casn1_name": "casn1_name",
        "registry_number": "registry_number",
        "scope_note": "scope_note",
        "translators_english_scope_note": "translators_english_scope_note",
        "translators_scope_note": "translators_scope_note",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodu_concept(**refr)

    return obj_id, refr


def create_qualifier(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `qualifiers` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "ui": "Q000000981",
        "name": "diagnostic imaging",
        "created": datetime.date(2016, 6, 29),
        "revised": datetime.date(2016, 6, 8),
        "established": datetime.date(2017, 1, 1),
        "annotation": ("subheading only; coordinate with specific  imaging "
                       "technique if pertinent"),
        "history_note": "2017(1967)",
        "online_note": "online_note",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodu_qualifier(**refr)

    return obj_id, refr


def create_tree_number(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `tree_numbers` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "tree_number": "A13.869.106",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodi_tree_number(**refr)

    return obj_id, refr


def create_descriptor(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `descriptors` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "descriptor_class": DescriptorClassType.ONE,
        "ui": "D000056",
        "name": "Accident Prevention",
        "created": datetime.date(1999, 1, 1),
        "revised": datetime.date(2008, 7, 8),
        "established": datetime.date(1966, 1, 1),
        "annotation": "general or unspecified; prefer specifics",
        "history_note": "70(69)",
        "nlm_classification_number": "WA 275",
        "online_note": "use CALCIMYCIN to search A 23187 1975-90",
        "public_mesh_note": ("96; was ABATE 1972-95 (see under INSECTICIDES,"
                             " ORGANOTHIOPHOSPHATE 1972-90)"),
        "consider_also": "consider_also",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodu_descriptor(**refr)

    return obj_id, refr


def create_entry_combination(
    dal: DalMesh,
    descriptor_id: int,
    qualifier_id: int,
    combination_type: Optional[Ect] = Ect.ECIN,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `entry_combinations` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.
        descriptor_id (int): The PK ID of the `descriptors` record.
        qualifier_id (int): The PK ID of the `qualifiers` record.
        combination_type (Optional[Ect] = Ect.ECIN): The combination type.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "descriptor_id": descriptor_id,
        "qualifier_id": qualifier_id,
        "combination_type": combination_type,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodu_entry_combination(**refr)

    return obj_id, refr


def create_previous_indexing(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `previous_indexings` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "previous_indexing": "Amoeba (1966-1987)",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodi_previous_indexing(**refr)

    return obj_id, refr


def create_supplemental(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `supplementals` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "supplemental_class": SupplementalClassType.ONE,
        "ui": "C000002",
        "name": "bevonium",
        "created": datetime.date(1971, 1, 1),
        "revised": datetime.date(2018, 9, 24),
        "note": "structure given in first source",
        "frequency": "1",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodu_supplemental(**refr)

    return obj_id, refr


def create_source(dal: DalMesh, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `sources` record.

    Args:
        dal (DalMesh): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "source": "Tetrahedron 26:4307",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Term()
    for k, v in refr.items():
        setattr(obj, k, v)

    obj_id = dal.iodi_source(**refr)

    return obj_id, refr
