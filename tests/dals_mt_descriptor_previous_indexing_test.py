# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `DescriptorPreviousIndexing` class as
well as the `iodi_descriptor_previous_indexing` method of the `DalMesh` class.
"""

from fform.orm_mt import DescriptorPreviousIndexing

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_descriptor
from tests.assets.items_mt import create_previous_indexing


class DalMtTermDescriptorPreviousIndexingTest(DalMtTestBase):
    """ Defines unit-tests for the `DescriptorPreviousIndexing` class as well as
        the `iodi_descriptor_previous_indexing` method of the `DalMesh` class.
    """

    def test_iodi_get_descriptor_previous_indexing(self):
        """ Tests the IODI insertion of a `DescriptorPreviousIndexing` record
            via the `iodi_descriptor_previous_indexing` method of the `DalMesh`
            class and its retrieval via the `get` method.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        previous_indexing_id, _ = create_previous_indexing(dal=self.dal)

        # IODI a new `DescriptorPreviousIndexing` record.
        obj_id = self.dal.iodi_descriptor_previous_indexing(
            descriptor_id=descriptor_id,
            previous_indexing_id=previous_indexing_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            DescriptorPreviousIndexing,
            obj_id,
        )  # type: DescriptorPreviousIndexing

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_previous_indexing_id, 1)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.previous_indexing_id, previous_indexing_id)

    def test_iodi_descriptor_previous_indexing_duplicate(self):
        """ Tests the IODI insertion of duplicate `DescriptorPreviousIndexing`
            records to ensure deduplication functions as intended.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        previous_indexing_id, _ = create_previous_indexing(dal=self.dal)
        previous_indexing_02_id, _ = create_previous_indexing(
            dal=self.dal,
            previous_indexing="NewPreviousIndexing"
        )

        # IODI a new `DescriptorPreviousIndexing` record.
        obj_id = self.dal.iodi_descriptor_previous_indexing(
            descriptor_id=descriptor_id,
            previous_indexing_id=previous_indexing_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `DescriptorPreviousIndexing` record.
        obj_id = self.dal.iodi_descriptor_previous_indexing(
            descriptor_id=descriptor_id,
            previous_indexing_id=previous_indexing_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `DescriptorPreviousIndexing` record.
        obj_id = self.dal.iodi_descriptor_previous_indexing(
            descriptor_id=descriptor_id,
            previous_indexing_id=previous_indexing_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_descriptor_previous_indexing(self):
        """ Tests the deletion of a `DescriptorPreviousIndexing` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        previous_indexing_id, _ = create_previous_indexing(dal=self.dal)

        # IODI a new `DescriptorPreviousIndexing` record.
        obj_id = self.dal.iodi_descriptor_previous_indexing(
            descriptor_id=descriptor_id,
            previous_indexing_id=previous_indexing_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(DescriptorPreviousIndexing, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            DescriptorPreviousIndexing,
            obj_id,
        )  # type: DescriptorPreviousIndexing

        self.assertIsNone(obj)
