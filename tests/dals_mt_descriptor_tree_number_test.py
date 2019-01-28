# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `DescriptorTreeNumber` class as well as
the `iodi_descriptor_tree_number` method of the `DalMesh` class.
"""

from fform.orm_mt import DescriptorTreeNumber

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_tree_number
from tests.assets.items_mt import create_descriptor


class DalMtTermDescriptorTreeNumberTest(DalMtTestBase):
    """ Defines unit-tests for the `DescriptorTreeNumber` class as well as
        the `iodi_descriptor_tree_number` method of the `DalMesh` class.
    """

    def test_iodi_get_descriptor_tree_number(self):
        """ Tests the IODI insertion of a `DescriptorTreeNumber` record via the
            `iodi_descriptor_tree_number` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        tree_number_id, _ = create_tree_number(dal=self.dal)

        # IODI a new `DescriptorTreeNumber` record.
        obj_id = self.dal.iodi_descriptor_tree_number(
            descriptor_id=descriptor_id,
            tree_number_id=tree_number_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            DescriptorTreeNumber,
            obj_id,
        )  # type: DescriptorTreeNumber

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_tree_number_id, 1)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.tree_number_id, tree_number_id)

    def test_iodi_descriptor_tree_number_duplicate(self):
        """ Tests the IODI insertion of duplicate `DescriptorTreeNumber`
            records to ensure deduplication functions as intended.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        tree_number_id, _ = create_tree_number(dal=self.dal)
        tree_number_02_id, _ = create_tree_number(
            dal=self.dal,
            tree_number="B13.869.106",
        )

        # IODI a new `DescriptorTreeNumber` record.
        obj_id = self.dal.iodi_descriptor_tree_number(
            descriptor_id=descriptor_id,
            tree_number_id=tree_number_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `DescriptorTreeNumber` record.
        obj_id = self.dal.iodi_descriptor_tree_number(
            descriptor_id=descriptor_id,
            tree_number_id=tree_number_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `DescriptorTreeNumber` record.
        obj_id = self.dal.iodi_descriptor_tree_number(
            descriptor_id=descriptor_id,
            tree_number_id=tree_number_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_descriptor_tree_number(self):
        """ Tests the deletion of a `DescriptorTreeNumber` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        tree_number_id, _ = create_tree_number(dal=self.dal)

        # IODI a new `DescriptorTreeNumber` record.
        obj_id = self.dal.iodi_descriptor_tree_number(
            descriptor_id=descriptor_id,
            tree_number_id=tree_number_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(DescriptorTreeNumber, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            DescriptorTreeNumber,
            obj_id,
        )  # type: DescriptorTreeNumber

        self.assertIsNone(obj)
