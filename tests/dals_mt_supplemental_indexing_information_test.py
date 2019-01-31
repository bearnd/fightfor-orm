# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `SupplementalIndexingInformation` class
as well as the `iodi_supplemental_indexing_information` method of the `DalMesh`
class.
"""

from fform.orm_mt import SupplementalIndexingInformation

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_descriptor
from tests.assets.items_mt import create_qualifier
from tests.assets.items_mt import create_entry_combination
from tests.assets.items_mt import create_supplemental


class DalMtTermSupplementalIndexingInformationTest(DalMtTestBase):
    """ Defines unit-tests for the `SupplementalIndexingInformation` class as
        well as the `iodi_supplemental_indexing_information` method of the
        `DalMesh` class.
    """

    def test_iodi_get_supplemental_indexing_information(self):
        """ Tests the IODI insertion of a `SupplementalIndexingInformation`
            record via the `iodi_supplemental_indexing_information` method of
            the `DalMesh` class and its retrieval via the `get` method.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        qualifier_id, _ = create_qualifier(dal=self.dal)
        entry_combination_id, _ = create_entry_combination(
            dal=self.dal,
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
        )
        supplemental_id, _ = create_supplemental(dal=self.dal)

        # IODI a new `SupplementalIndexingInformation` record.
        obj_id = self.dal.iodi_supplemental_indexing_information(
            supplemental_id=supplemental_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            SupplementalIndexingInformation,
            obj_id,
        )  # type: SupplementalIndexingInformation

        # Assert that the different fields of the record match.
        self.assertEqual(obj.supplemental_indexing_information_id, 1)
        self.assertEqual(obj.supplemental_id, supplemental_id)
        self.assertEqual(obj.entry_combination_id, entry_combination_id)

    def test_iodi_supplemental_indexing_information_duplicate(self):
        """ Tests the IODI insertion of duplicate
            `SupplementalIndexingInformation` records to ensure deduplication
            functions as intended.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        qualifier_id, _ = create_qualifier(dal=self.dal)
        entry_combination_id, _ = create_entry_combination(
            dal=self.dal,
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
        )
        supplemental_id, _ = create_supplemental(dal=self.dal)
        supplemental_02_id, _ = create_supplemental(
            dal=self.dal,
            ui="UI2",
            name="Name2"
        )

        # IODI a new `SupplementalIndexingInformation` record.
        obj_id = self.dal.iodi_supplemental_indexing_information(
            supplemental_id=supplemental_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `SupplementalIndexingInformation` record.
        obj_id = self.dal.iodi_supplemental_indexing_information(
            supplemental_id=supplemental_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `SupplementalIndexingInformation` record.
        obj_id = self.dal.iodi_supplemental_indexing_information(
            supplemental_id=supplemental_02_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_supplemental_indexing_information(self):
        """ Tests the deletion of a `SupplementalIndexingInformation` record via
            the `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        qualifier_id, _ = create_qualifier(dal=self.dal)
        entry_combination_id, _ = create_entry_combination(
            dal=self.dal,
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
        )
        supplemental_id, _ = create_supplemental(dal=self.dal)

        # IODI a new `SupplementalIndexingInformation` record.
        obj_id = self.dal.iodi_supplemental_indexing_information(
            supplemental_id=supplemental_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(SupplementalIndexingInformation, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            SupplementalIndexingInformation,
            obj_id,
        )  # type: SupplementalIndexingInformation

        self.assertIsNone(obj)
