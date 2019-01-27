# -*- coding: utf-8 -*-

import datetime
from typing import Tuple, Dict

from fform.orm_mt import Term
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
