# coding=utf-8

import datetime
from typing import Optional, Tuple, Dict

from fform.orm_pubmed import Journal
from fform.orm_pubmed import Article
from fform.orm_pubmed import ArticlePubModel
from fform.orm_pubmed import JournalIssnType
from fform.dals_pubmed import DalPubmed


def create_journal(dal: DalPubmed, **kwargs) -> Tuple[int, Dict]:
    """ Inserts a new `journals` record.

    Args:
        dal (DalPubmed): The DAL used to interact with the DB.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    refr = {
        "issn": "0007-0947",
        "issn_type": JournalIssnType.PRINT,
        "title": "The British journal of clinical practice",
        "abbreviation": "Br J Clin Pract",
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Journal()
    for k, v in refr.items():
        setattr(obj, k, v)

    refr["md5"] = obj.md5

    obj_id = dal.iodi_journal(**refr)

    return obj_id, refr


def create_article(
    dal: DalPubmed,
    journal_id: Optional[int] = None,
    **kwargs
) -> Tuple[int, Dict]:
    """ Inserts a new `journals` record.

    Args:
        dal (DalPubmed): The DAL used to interact with the DB.
        journal_id (Optional[int] = None): The ID of the `journals` record
            against which the new record will be associated.

    Returns:
        Tuple(int, Dict):
            - The PK ID of the new record.
            - The inserted record reference.
    """

    if journal_id is None:
        journal_id, _ = create_journal(dal=dal)

    refr = {
        "publication_year": 1975,
        "publication_month": 12,
        "publication_day": 26,
        "date_published": datetime.date(1975, 12, 26),
        "publication_model": ArticlePubModel.PRINT,
        "journal_id": journal_id,
        "journal_volume": "40",
        "journal_issue": "26",
        "title": ("Different reactivities of 5-bromo-2'-deoxyuridine and "
                  "5-bromouracil in the bisulfite-mediated debromination."),
        "pagination": "3862-5",
        "language": "eng",
        "title_vernacular": None,
    }

    # Override any reference pairs with values under `kwargs`.
    for k, v in kwargs.items():
        refr[k] = v

    obj = Article()
    for k, v in refr.items():
        setattr(obj, k, v)

    refr["md5"] = obj.md5

    obj_id = dal.iodi_article(**refr)

    return obj_id, refr
