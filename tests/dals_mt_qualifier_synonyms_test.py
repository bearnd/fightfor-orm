# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `QualifierSynonym` class as well as the
`biodi_qualifier_synonyms` method of the `DalMesh` class.
"""

import hashlib
from typing import List

from fform.orm_mt import QualifierSynonym

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_qualifier


class DalMtQualifierSynonymTest(DalMtTestBase):

    @staticmethod
    def _get_md5s(values: List[str]) -> List[bytes]:
        """ Returns the binary digests of the MD5 hashes of a list of strings.

        Args:
            values (List[str]): The list of strings to be hashed.

        Returns:
            List[bytes]: The list of binary digests of the MD5 hashes.
        """

        md5s = [
            hashlib.md5(value.encode("utf-8")).digest()
            for value in values
        ]

        return md5s

    def _get_all_qualifier_synonyms(self) -> List[QualifierSynonym]:
        """ Returns all `QualifierSynonym` records.

        Returns:
            List[QualifierSynonym]: A list of all `QualifierSynonym` records.
        """

        with self.dal.session_scope() as session:
            query = session.query(QualifierSynonym)
            objs = query.all()

        return objs

    def test_biodi_get_qualifier_synonym(self):
        """ Tests the BIODI insertion of a single `QualifierSynonym` record via
            the `biodi_qualifier_synonyms` method of the `DalMesh` class and
            its retrieval via the `get` method.
        """

        # Create a new `Qualifier` record.
        qualifier_id, _ = create_qualifier(dal=self.dal)

        synonyms = ["synonym"]

        # Create a new `QualifierSynonym` record.
        self.dal.biodi_qualifier_synonyms(
            qualifier_id=qualifier_id,
            synonyms=synonyms,
            md5s=self._get_md5s(values=synonyms),
        )

        # Retrieve all `QualifierSynonym` records for the new `Qualifier`.
        objs = self.dal.bget_by_attr(
            orm_class=QualifierSynonym,
            attr_name="qualifier_id",
            attr_values=[qualifier_id],
            do_sort=True,
        )  # type: List[QualifierSynonym]

        self.assertEqual(len(objs), 1)

        obj = objs[0]

        # Assert that the different fields of the record match.
        self.assertEqual(obj.qualifier_synonym_id, 1)
        self.assertEqual(obj.qualifier_id, qualifier_id)
        self.assertEqual(obj.synonym, synonyms[0])
        self.assertEqual(obj.md5, self._get_md5s(values=synonyms)[0])

    def test_biodi_get_qualifier_synonyms(self):
        """ Tests the BIODI insertion of multiple `QualifierSynonym` records
            via the `biodi_qualifier_synonyms` method of the `DalMesh` class
            and its retrieval via the `get` method.
        """

        # Create a new `Qualifier` record.
        qualifier_id, _ = create_qualifier(dal=self.dal)

        synonyms = ["synonym01", "synonym02", "synonym03", "synonym04"]

        # Create a new `QualifierSynonym` record.
        self.dal.biodi_qualifier_synonyms(
            qualifier_id=qualifier_id,
            synonyms=synonyms,
            md5s=self._get_md5s(values=synonyms),
        )

        # Retrieve all `QualifierSynonym` records for the new `Qualifier`.
        objs = self.dal.bget_by_attr(
            orm_class=QualifierSynonym,
            attr_name="qualifier_id",
            attr_values=[qualifier_id],
            do_sort=True,
        )  # type: List[QualifierSynonym]

        self.assertEqual(len(objs), len(synonyms))

        synonyms_eval = [obj.synonym for obj in objs]

        self.assertListEqual(synonyms_eval, synonyms)

    def test_biodi_qualifier_synonym_duplicate(self):
        """ Tests the BIODI insertion of duplicate `QualifierSynonym` records
            to ensure deduplication functions as intended.
        """

        # Create a new `Qualifier` record.
        qualifier_id, _ = create_qualifier(dal=self.dal)

        # Create a new `QualifierSynonym` record.
        self.dal.biodi_qualifier_synonyms(
            qualifier_id=qualifier_id,
            synonyms=["synonym01"],
            md5s=self._get_md5s(values=["synonym01"]),
        )

        self.assertEqual(len(self._get_all_qualifier_synonyms()), 1)

        # BIODI the same `QualifierSynonym` record.
        self.dal.biodi_qualifier_synonyms(
            qualifier_id=qualifier_id,
            synonyms=["synonym01"],
            md5s=self._get_md5s(values=["synonym01"]),
        )

        self.assertEqual(len(self._get_all_qualifier_synonyms()), 1)

        # BIODI the same `QualifierSynonym` record.
        self.dal.biodi_qualifier_synonyms(
            qualifier_id=qualifier_id,
            synonyms=["synonym02"],
            md5s=self._get_md5s(values=["synonym02"]),
        )

        self.assertEqual(len(self._get_all_qualifier_synonyms()), 2)

        # BIODI the same `QualifierSynonym` record as before.
        self.dal.biodi_qualifier_synonyms(
            qualifier_id=qualifier_id,
            synonyms=["synonym02"],
            md5s=self._get_md5s(values=["synonym02"]),
        )

        self.assertEqual(len(self._get_all_qualifier_synonyms()), 2)

    def test_delete_qualifier_synonym(self):
        """ Tests the deletion of a `QualifierSynonym` record via the `delete`
            method of the `DalMesh` class.
        """

        # Create a new `Qualifier` record.
        qualifier_id, _ = create_qualifier(dal=self.dal)

        synonyms = ["synonym"]

        # Create a new `QualifierSynonym` record.
        self.dal.biodi_qualifier_synonyms(
            qualifier_id=qualifier_id,
            synonyms=synonyms,
            md5s=self._get_md5s(values=synonyms),
        )

        # Retrieve all `QualifierSynonym` records for the new `Qualifier`.
        objs = self.dal.bget_by_attr(
            orm_class=QualifierSynonym,
            attr_name="qualifier_id",
            attr_values=[qualifier_id],
            do_sort=True,
        )  # type: List[QualifierSynonym]

        self.assertEqual(len(objs), 1)

        obj_id = objs[0].qualifier_synonym_id

        # Delete the new record.
        self.dal.delete(QualifierSynonym, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(QualifierSynonym, obj_id)  # type: QualifierSynonym

        self.assertIsNone(obj)
