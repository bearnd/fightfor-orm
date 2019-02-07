# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `DescriptorRelatedDescriptor` class as
well as the `iodi_descriptor_related_descriptor` method of the `DalMesh` class.
"""

from fform.orm_mt import DescriptorRelatedDescriptor

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_descriptor


class DalMtTermDescriptorRelatedDescriptorTest(DalMtTestBase):
    """ Defines unit-tests for the `DescriptorRelatedDescriptor` class as well
        as the `iodi_descriptor_related_descriptor` method of the `DalMesh`
        class.
    """

    def test_iodi_get_descriptor_related_descriptor(self):
        """ Tests the IODI insertion of a `DescriptorRelatedDescriptor` record
            via the `iodi_descriptor_related_descriptor` method of the `DalMesh`
            class and its retrieval via the `get` method.
        """

        # Create fixture records.
        descriptor_01_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI1",
            name="Name1",
        )
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="Name2",
        )

        # IODI a new `DescriptorRelatedDescriptor` record.
        obj_id = self.dal.iodi_descriptor_related_descriptor(
            descriptor_id=descriptor_01_id,
            related_descriptor_id=descriptor_02_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            DescriptorRelatedDescriptor,
            obj_id,
        )  # type: DescriptorRelatedDescriptor

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_related_descriptor_id, 1)
        self.assertEqual(obj.descriptor_id, descriptor_01_id)
        self.assertEqual(obj.related_descriptor_id, descriptor_02_id)

    def test_iodi_descriptor_related_descriptor_duplicate(self):
        """ Tests the IODI insertion of duplicate `DescriptorRelatedDescriptor`
            records to ensure deduplication functions as intended.
        """

        # Create fixture records.
        descriptor_01_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI1",
            name="Name1",
        )
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="Name2",
        )
        descriptor_03_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI3",
            name="Name3",
        )

        # IODI a new `DescriptorRelatedDescriptor` record.
        obj_id = self.dal.iodi_descriptor_related_descriptor(
            descriptor_id=descriptor_01_id,
            related_descriptor_id=descriptor_02_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `DescriptorRelatedDescriptor` record.
        obj_id = self.dal.iodi_descriptor_related_descriptor(
            descriptor_id=descriptor_01_id,
            related_descriptor_id=descriptor_02_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `DescriptorRelatedDescriptor` record.
        obj_id = self.dal.iodi_descriptor_related_descriptor(
            descriptor_id=descriptor_01_id,
            related_descriptor_id=descriptor_03_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_descriptor_related_descriptor(self):
        """ Tests the deletion of a `DescriptorRelatedDescriptor` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        descriptor_01_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI1",
            name="Name1",
        )
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="Name2",
        )

        # IODI a new `DescriptorRelatedDescriptor` record.
        obj_id = self.dal.iodi_descriptor_related_descriptor(
            descriptor_id=descriptor_01_id,
            related_descriptor_id=descriptor_02_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(DescriptorRelatedDescriptor, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            DescriptorRelatedDescriptor,
            obj_id,
        )  # type: DescriptorRelatedDescriptor

        self.assertIsNone(obj)
