# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `DescriptorSynonym` class as well as the
`biodi_descriptor_synonyms` method of the `DalMesh` class.
"""

import hashlib
from typing import List

from fform.orm_mt import DescriptorSynonym

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_descriptor


class DalMtDescriptorSynonymTest(DalMtTestBase):

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

    def _get_all_descriptor_synonyms(self) -> List[DescriptorSynonym]:
        """ Returns all `DescriptorSynonym` records.

        Returns:
            List[DescriptorSynonym]: A list of all `DescriptorSynonym` records.
        """

        with self.dal.session_scope() as session:
            query = session.query(DescriptorSynonym)
            objs = query.all()

        return objs

    def test_biodi_get_descriptor_synonym(self):
        """ Tests the BIODI insertion of a single `DescriptorSynonym` record via
            the `biodi_descriptor_synonyms` method of the `DalMesh` class and
            its retrieval via the `get` method.
        """

        # Create a new `Descriptor` record.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        synonyms = ["synonym"]

        # Create a new `DescriptorSynonym` record.
        self.dal.biodi_descriptor_synonyms(
            descriptor_id=descriptor_id,
            synonyms=synonyms,
            md5s=self._get_md5s(values=synonyms),
        )

        # Retrieve all `DescriptorSynonym` records for the new `Descriptor`.
        objs = self.dal.bget_by_attr(
            orm_class=DescriptorSynonym,
            attr_name="descriptor_id",
            attr_values=[descriptor_id],
            do_sort=True,
        )  # type: List[DescriptorSynonym]

        self.assertEqual(len(objs), 1)

        obj = objs[0]

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_synonym_id, 1)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.synonym, synonyms[0])
        self.assertEqual(obj.md5, self._get_md5s(values=synonyms)[0])

    def test_biodi_get_descriptor_synonyms(self):
        """ Tests the BIODI insertion of multiple `DescriptorSynonym` records
            via the `biodi_descriptor_synonyms` method of the `DalMesh` class
            and its retrieval via the `get` method.
        """

        # Create a new `Descriptor` record.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        synonyms = ["synonym01", "synonym02", "synonym03", "synonym04"]

        # Create a new `DescriptorSynonym` record.
        self.dal.biodi_descriptor_synonyms(
            descriptor_id=descriptor_id,
            synonyms=synonyms,
            md5s=self._get_md5s(values=synonyms),
        )

        # Retrieve all `DescriptorSynonym` records for the new `Descriptor`.
        objs = self.dal.bget_by_attr(
            orm_class=DescriptorSynonym,
            attr_name="descriptor_id",
            attr_values=[descriptor_id],
            do_sort=True,
        )  # type: List[DescriptorSynonym]

        self.assertEqual(len(objs), len(synonyms))

        synonyms_eval = [obj.synonym for obj in objs]

        self.assertListEqual(synonyms_eval, synonyms)

    def test_biodi_descriptor_synonym_duplicate(self):
        """ Tests the BIODI insertion of duplicate `DescriptorSynonym` records
            to ensure deduplication functions as intended.
        """

        # Create a new `Descriptor` record.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        # Create a new `DescriptorSynonym` record.
        self.dal.biodi_descriptor_synonyms(
            descriptor_id=descriptor_id,
            synonyms=["synonym01"],
            md5s=self._get_md5s(values=["synonym01"]),
        )

        self.assertEqual(len(self._get_all_descriptor_synonyms()), 1)

        # BIODI the same `DescriptorSynonym` record.
        self.dal.biodi_descriptor_synonyms(
            descriptor_id=descriptor_id,
            synonyms=["synonym01"],
            md5s=self._get_md5s(values=["synonym01"]),
        )

        self.assertEqual(len(self._get_all_descriptor_synonyms()), 1)

        # BIODI the same `DescriptorSynonym` record.
        self.dal.biodi_descriptor_synonyms(
            descriptor_id=descriptor_id,
            synonyms=["synonym02"],
            md5s=self._get_md5s(values=["synonym02"]),
        )

        self.assertEqual(len(self._get_all_descriptor_synonyms()), 2)

        # BIODI the same `DescriptorSynonym` record as before.
        self.dal.biodi_descriptor_synonyms(
            descriptor_id=descriptor_id,
            synonyms=["synonym02"],
            md5s=self._get_md5s(values=["synonym02"]),
        )

        self.assertEqual(len(self._get_all_descriptor_synonyms()), 2)

    def test_delete_descriptor_synonym(self):
        """ Tests the deletion of a `DescriptorSynonym` record via the `delete`
            method of the `DalMesh` class.
        """

        # Create a new `Descriptor` record.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        synonyms = ["synonym"]

        # Create a new `DescriptorSynonym` record.
        self.dal.biodi_descriptor_synonyms(
            descriptor_id=descriptor_id,
            synonyms=synonyms,
            md5s=self._get_md5s(values=synonyms),
        )

        # Retrieve all `DescriptorSynonym` records for the new `Descriptor`.
        objs = self.dal.bget_by_attr(
            orm_class=DescriptorSynonym,
            attr_name="descriptor_id",
            attr_values=[descriptor_id],
            do_sort=True,
        )  # type: List[DescriptorSynonym]

        self.assertEqual(len(objs), 1)

        obj_id = objs[0].descriptor_synonym_id

        # Delete the new record.
        self.dal.delete(DescriptorSynonym, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(DescriptorSynonym, obj_id)  # type: DescriptorSynonym

        self.assertIsNone(obj)
