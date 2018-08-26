# coding=utf-8

import datetime
from typing import List, Union

from sqlalchemy.dialects.postgresql import insert

from fform.dal_base import DalFightForBase
from fform.dal_base import with_session_scope
from fform.orm_pubmed import Chemical
from fform.orm_pubmed import Author
from fform.orm_pubmed import Affiliation
from fform.orm_pubmed import PmKeyword
from fform.orm_pubmed import PmDescriptor
from fform.orm_pubmed import PmQualifier
from fform.orm_pubmed import PublicationType
from fform.orm_pubmed import Journal
from fform.orm_pubmed import JournalIssnType
from fform.orm_pubmed import JournalInfo
from fform.orm_pubmed import Grant
from fform.orm_pubmed import Databank
from fform.orm_pubmed import AccessionNumber
from fform.orm_pubmed import ArticleAbstractText
from fform.orm_pubmed import ArticleAuthorAffiliation
from fform.orm_pubmed import ArticleDatabankAccessionNumber
from fform.orm_pubmed import ArticleGrant
from fform.orm_pubmed import CitationChemical
from fform.orm_pubmed import CitationDescriptorQualifier
from fform.orm_pubmed import CitationIdentifier
from fform.orm_pubmed import CitationKeyword
from fform.orm_pubmed import ArticleIdentifierType
from fform.orm_pubmed import ArticlePublicationType
from fform.orm_pubmed import AbstractText
from fform.orm_pubmed import AbstractTextCategory
from fform.orm_pubmed import ArticlePubModel
from fform.orm_pubmed import Article
from fform.orm_pubmed import Citation
from fform.utils import lists_equal_length


class DalPubmed(DalFightForBase):
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

        super(DalPubmed, self).__init__(
            sql_username=sql_username,
            sql_password=sql_password,
            sql_host=sql_host,
            sql_port=sql_port,
            sql_db=sql_db,
            *args,
            **kwargs
        )

    @lists_equal_length
    @with_session_scope()
    def biodi_chemicals(
        self,
        nums_registries: List[str],
        uids: List[str],
        chemicals: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            Chemical,
            values=list(
                {
                    "num_registry": num_registry,
                    "uid": uid,
                    "chemical": chemical,
                } for num_registry, uid, chemical in zip(
                    nums_registries,
                    uids,
                    chemicals
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=Chemical,
            attr_name="uid",
            attr_values=uids,
            do_sort=True,
            session=session,
        )  # type: List[Chemical]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_descriptors(
        self,
        uids: List[str],
        descriptors: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            PmDescriptor,
            values=list(
                {
                    "uid": uid,
                    "descriptor": descriptor,
                } for uid, descriptor in zip(
                    uids,
                    descriptors
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=PmDescriptor,
            attr_name="uid",
            attr_values=uids,
            do_sort=True,
            session=session,
        )  # type: List[PmDescriptor]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_qualifiers(
        self,
        uids: List[str],
        qualifiers: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            PmQualifier,
            values=list(
                {
                    "uid": uid,
                    "qualifier": qualifier,
                } for uid, qualifier in zip(
                    uids,
                    qualifiers
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=PmQualifier,
            attr_name="uid",
            attr_values=uids,
            do_sort=True,
            session=session,
        )  # type: List[PmQualifier]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_keywords(
        self,
        keywords: List[str],
        md5s: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            PmKeyword,
            values=list(
                {
                    "keyword": keyword,
                    "md5": md5,
                } for keyword, md5 in zip(
                    keywords,
                    md5s
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=PmKeyword,
            attr_name="md5",
            attr_values=md5s,
            do_sort=True,
            session=session,
        )  # type: List[PmKeyword]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_publication_types(
        self,
        uids: List[str],
        publication_types: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            PublicationType,
            values=list(
                {
                    "uid": uid,
                    "publication_type": publication_type,
                } for uid, publication_type in zip(
                    uids,
                    publication_types
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=PublicationType,
            attr_name="uid",
            attr_values=uids,
            do_sort=True,
            session=session,
        )  # type: List[PublicationType]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_authors(
        self,
        author_identifiers: List[str],
        author_identifier_sources: List[str],
        names_first: List[str],
        names_last: List[str],
        names_initials: List[str],
        names_suffix: List[str],
        emails: List[str],
        md5s: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            Author,
            values=list(
                {
                    "author_identifier": author_identifier,
                    "author_identifier_source": author_identifier_source,
                    "name_first": name_first,
                    "name_last": name_last,
                    "name_initials": name_initials,
                    "name_suffix": name_suffix,
                    "email": email,
                    "md5": md5,
                } for (
                    author_identifier,
                    author_identifier_source,
                    name_first,
                    name_last,
                    name_initials,
                    name_suffix,
                    email,
                    md5,
                ) in zip(
                    author_identifiers,
                    author_identifier_sources,
                    names_first,
                    names_last,
                    names_initials,
                    names_suffix,
                    emails,
                    md5s,
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=Author,
            attr_name="md5",
            attr_values=md5s,
            do_sort=True,
            session=session,
        )  # type: List[Author]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_affiliations(
        self,
        affiliation_identifiers: List[str],
        affiliation_identifier_sources: List[str],
        affiliations: List[str],
        md5s: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            Affiliation,
            values=list(
                {
                    "affiliation_identifier": affiliation_identifier,
                    "affiliation_identifier_source":
                        affiliation_identifier_source,
                    "affiliation": affiliation,
                    "md5": md5,
                } for (
                    affiliation_identifier,
                    affiliation_identifier_source,
                    affiliation,
                    md5,
                ) in zip(
                    affiliation_identifiers,
                    affiliation_identifier_sources,
                    affiliations,
                    md5s,
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=Affiliation,
            attr_name="md5",
            attr_values=md5s,
            do_sort=True,
            session=session,
        )  # type: List[Affiliation]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_grants(
        self,
        uids: List[str],
        acronyms: List[str],
        agencies: List[str],
        countries: List[str],
        md5s: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            Grant,
            values=list(
                {
                    "uid": uid,
                    "acronym": acronym,
                    "agency": agency,
                    "country": country,
                    "md5": md5,
                } for (
                    uid,
                    acronym,
                    agency,
                    country,
                    md5,
                ) in zip(
                    uids,
                    acronyms,
                    agencies,
                    countries,
                    md5s,
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=Grant,
            attr_name="md5",
            attr_values=md5s,
            do_sort=True,
            session=session,
        )  # type: List[Grant]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_databanks(
        self,
        databanks: List[str],
        md5s: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            Databank,
            values=list(
                {
                    "databank": databank,
                    "md5": md5,
                } for databank, md5 in zip(
                    databanks,
                    md5s
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=Databank,
            attr_name="md5",
            attr_values=md5s,
            do_sort=True,
            session=session,
        )  # type: List[Databank]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_accession_numbers(
        self,
        accession_numbers: List[str],
        md5s: List[str],
        session=None
    ) -> List[int]:

        statement = insert(
            AccessionNumber,
            values=list(
                {
                    "accession_number": accession_number,
                    "md5": md5,
                } for accession_number, md5 in zip(
                    accession_numbers,
                    md5s
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=AccessionNumber,
            attr_name="md5",
            attr_values=md5s,
            do_sort=True,
            session=session,
        )  # type: List[AccessionNumber]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @lists_equal_length
    @with_session_scope()
    def biodi_article_abstract_texts(
        self,
        article_id: int,
        abstract_text_ids: List[int],
        ordinances: List[int],
        session=None
    ) -> None:

        statement = insert(
            ArticleAbstractText,
            values=list(
                {
                    "article_id": article_id,
                    "abstract_text_id": abstract_text_id,
                    "ordinance": ordinance,
                } for (
                    abstract_text_id,
                    ordinance,
                ) in zip(abstract_text_ids, ordinances)
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_article_author_affiliations(
        self,
        article_id: int,
        author_ids: List[int],
        affiliation_ids: Union[List[int], List[None]],
        ordinances: List[int],
        session=None,
    ) -> None:

        statement = insert(
            ArticleAuthorAffiliation,
            values=list(
                {
                    "article_id": article_id,
                    "author_id": author_id,
                    "affiliation_id": affiliation_id,
                    "ordinance": ordinance,
                } for author_id, affiliation_id, ordinance in zip(
                    author_ids,
                    affiliation_ids,
                    ordinances
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_article_databank_accession_numbers(
        self,
        article_id: int,
        databank_id: int,
        accession_number_ids: List[int],
        session=None,
    ) -> None:

        statement = insert(
            ArticleDatabankAccessionNumber,
            values=list(
                {
                    "article_id": article_id,
                    "databank_id": databank_id,
                    "accession_number_id": accession_number_id,
                } for accession_number_id in zip(
                    accession_number_ids
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_article_grants(
        self,
        article_id: int,
        grant_ids: List[int],
        session=None,
    ) -> None:

        statement = insert(
            ArticleGrant,
            values=list(
                {
                    "article_id": article_id,
                    "grant_id": grant_id,
                } for grant_id in zip(
                    grant_ids
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_citation_chemicals(
        self,
        citation_id: int,
        chemical_ids: List[int],
        session=None,
    ) -> None:

        statement = insert(
            CitationChemical,
            values=list(
                {
                    "citation_id": citation_id,
                    "chemical_id": chemical_id,
                } for chemical_id in zip(
                    chemical_ids
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_citation_descriptors_qualifiers(
        self,
        citation_id: int,
        descriptor_ids: List[int],
        are_descriptors_major: List[bool],
        qualifier_ids: List[int],
        are_qualifiers_major: List[bool],
        session=None,
    ) -> None:

        statement = insert(
            CitationDescriptorQualifier,
            values=list(
                {
                    "citation_id": citation_id,
                    "descriptor_id": descriptor_id,
                    "is_descriptor_major": is_descriptor_major,
                    "qualifier_id": qualifier_id,
                    "is_qualifier_major": is_qualifier_major,
                } for (
                    descriptor_id,
                    is_descriptor_major,
                    qualifier_id,
                    is_qualifier_major,
                ) in zip(
                    descriptor_ids,
                    are_descriptors_major,
                    qualifier_ids,
                    are_qualifiers_major,
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_citation_identifiers(
        self,
        citation_id: int,
        identifier_types: List[ArticleIdentifierType],
        identifiers: List[str],
        session=None,
    ) -> None:

        statement = insert(
            CitationIdentifier,
            values=list(
                {
                    "citation_id": citation_id,
                    "identifier_type": identifier_type,
                    "identifier": identifier,
                } for (
                    identifier_type,
                    identifier
                ) in zip(
                    identifier_types,
                    identifiers
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_citation_keywords(
        self,
        citation_id: int,
        keyword_ids: List[int],
        session=None,
    ) -> None:

        statement = insert(
            CitationKeyword,
            values=list(
                {
                    "citation_id": citation_id,
                    "keyword_id": keyword_id,
                } for keyword_id in zip(
                    keyword_ids
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_article_publication_types(
        self,
        article_id: int,
        publication_type_ids: List[int],
        session=None,
    ) -> None:

        statement = insert(
            ArticlePublicationType,
            values=list(
                {
                    "article_id": article_id,
                    "publication_type_id": publication_type_id,
                } for publication_type_id in zip(
                    publication_type_ids
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

    @lists_equal_length
    @with_session_scope()
    def biodi_abstract_texts(
        self,
        labels: str,
        categories: List[AbstractTextCategory],
        texts: List[str],
        md5s: List[str],
        session=None,
    ) -> List[int]:

        statement = insert(
            AbstractText,
            values=list(
                {
                    "label": label,
                    "category": category,
                    "text": text,
                    "md5": md5,
                } for label, category, text, md5 in zip(
                    labels,
                    categories,
                    texts,
                    md5s,
                )
            )
        ).on_conflict_do_nothing()

        session.execute(statement)

        objs = self.bget_by_attr(
            orm_class=AbstractText,
            attr_name="md5",
            attr_values=md5s,
            do_sort=True,
            session=session,
        )  # type: List[AbstractText]

        obj_ids = [getattr(obj, obj.pk_name) for obj in objs]

        return obj_ids

    @with_session_scope()
    def iodi_journal_info(
        self,
        nlmid: str,
        issn: str,
        country: str,
        abbreviation: str,
        session=None
    ) -> int:

        statement = insert(
            JournalInfo,
            values={
                "nlmid": nlmid,
                "issn": issn,
                "country": country,
                "abbreviation": abbreviation,
            }
        ).on_conflict_do_nothing()

        session.execute(statement)

        obj = self.get_by_attr(
            orm_class=JournalInfo,
            attr_name="nlmid",
            attr_value=nlmid,
            session=session,
        )  # type: JournalInfo

        obj_id = getattr(obj, obj.pk_name)

        return obj_id

    @with_session_scope()
    def iodi_journal(
        self,
        issn: str,
        issn_type: JournalIssnType,
        title: str,
        abbreviation: str,
        md5: str,
        session=None
    ) -> int:

        statement = insert(
            Journal,
            values={
                "issn": issn,
                "issn_type": issn_type,
                "title": title,
                "abbreviation": abbreviation,
                "md5": md5,
            }
        ).on_conflict_do_nothing()

        session.execute(statement)

        obj = self.get_by_attr(
            orm_class=Journal,
            attr_name="md5",
            attr_value=md5,
            session=session,
        )  # type: Journal

        obj_id = getattr(obj, obj.pk_name)

        return obj_id

    @with_session_scope()
    def iodi_article(
        self,
        publication_year: int,
        publication_month: int,
        publication_day: int,
        date_published: datetime.date,
        publication_model: ArticlePubModel,
        journal_id: int,
        journal_volume: str,
        journal_issue: str,
        title: str,
        pagination: str,
        language: str,
        title_vernacular: str,
        md5: str,
        session=None,
    ) -> int:

        statement = insert(
            Article,
            values={
                "publication_year": publication_year,
                "publication_month": publication_month,
                "publication_day": publication_day,
                "date_published": date_published,
                "publication_model": publication_model,
                "journal_id": journal_id,
                "journal_volume": journal_volume,
                "journal_issue": journal_issue,
                "title": title,
                "pagination": pagination,
                "language": language,
                "title_vernacular": title_vernacular,
                "md5": md5,
            }
        ).on_conflict_do_nothing()

        session.execute(statement)

        obj = self.get_by_attr(
            orm_class=Article,
            attr_name="md5",
            attr_value=md5,
            session=session,
        )  # type: Article

        obj_id = getattr(obj, obj.pk_name)

        return obj_id

    @with_session_scope()
    def iodi_citation(
        self,
        pmid: int,
        date_created: datetime.date,
        date_completion: datetime.date,
        date_revision: datetime.date,
        article_id: int,
        journal_info_id: int,
        num_references: int,
        session=None,
    ) -> int:

        statement = insert(
            Citation,
            values={
                "pmid": pmid,
                "date_created": date_created,
                "date_completion": date_completion,
                "date_revision": date_revision,
                "article_id": article_id,
                "journal_info_id": journal_info_id,
                "num_references": num_references,
            }
        ).on_conflict_do_nothing()

        session.execute(statement)

        obj = self.get_by_attr(
            orm_class=Citation,
            attr_name="pmid",
            attr_value=pmid,
            session=session,
        )  # type: Citation

        obj_id = getattr(obj, obj.pk_name)

        return obj_id
