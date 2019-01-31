# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `DescriptorEntryCombination` class as
well as the `iodi_descriptor_entry_combination` method of the `DalMesh` class.
"""

from fform.orm_mt import DescriptorEntryCombination

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_qualifier
from tests.assets.items_mt import create_descriptor
from tests.assets.items_mt import create_entry_combination


class DalMtDescriptorEntryCombinationTest(DalMtTestBase):
    """ Defines unit-tests for the `DescriptorEntryCombination` class as well as
        the `iodi_descriptor_entry_combination` method of the `DalMesh` class.
    """

    def test_iodi_get_descriptor_entry_combination(self):
        """ Tests the IODI insertion of a `DescriptorEntryCombination` record
            via the `iodi_descriptor_entry_combination` method of the `DalMesh`
            class and its retrieval via the `get` method.
        """

        # Create fixture records.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal)
        entry_combination_id, _ = create_entry_combination(
            dal=self.dal,
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
        )

        # IODI a new `DescriptorEntryCombination` record.
        obj_id = self.dal.iodi_descriptor_entry_combination(
            descriptor_id=descriptor_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            DescriptorEntryCombination,
            obj_id,
        )  # type: DescriptorEntryCombination

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_entry_combination_id, 1)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.entry_combination_id, entry_combination_id)

    def test_iodi_descriptor_entry_combination_duplicate(self):
        """ Tests the IODI insertion of duplicate `DescriptorEntryCombination`
            records to ensure deduplication functions as intended.
        """

        # Create fixture records.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal)
        entry_combination_id, _ = create_entry_combination(
            dal=self.dal,
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
        )
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="Name2",
        )

        # IODI a new `DescriptorEntryCombination` record.
        obj_id = self.dal.iodi_descriptor_entry_combination(
            descriptor_id=descriptor_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `DescriptorEntryCombination` record.
        obj_id = self.dal.iodi_descriptor_entry_combination(
            descriptor_id=descriptor_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `DescriptorEntryCombination` record.
        obj_id = self.dal.iodi_descriptor_entry_combination(
            descriptor_id=descriptor_02_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_descriptor_entry_combination(self):
        """ Tests the deletion of a `DescriptorEntryCombination` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal)
        entry_combination_id, _ = create_entry_combination(
            dal=self.dal,
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
        )

        # IODI a new `DescriptorEntryCombination` record.
        obj_id = self.dal.iodi_descriptor_entry_combination(
            descriptor_id=descriptor_id,
            entry_combination_id=entry_combination_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(DescriptorEntryCombination, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            DescriptorEntryCombination,
            obj_id,
        )  # type: DescriptorEntryCombination

        self.assertIsNone(obj)
