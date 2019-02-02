# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the
`DescriptorPharmacologicalActionDescriptor` class as well as the
`iodi_descriptor_pharmacological_action_descriptor` method of the `DalMesh`
class.
"""

from fform.orm_mt import DescriptorPharmacologicalActionDescriptor

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_descriptor


class DalMtTermDescriptorPharmacologicalActionDescriptorTest(DalMtTestBase):
    """ Defines unit-tests for the `DescriptorPharmacologicalActionDescriptor`
        class as well as the
        `iodi_descriptor_pharmacological_action_descriptor` method of the
        `DalMesh` class.
    """

    def test_iodi_get_descriptor_pharmacological_action_descriptor(self):
        """ Tests the IODI insertion of a
            `DescriptorPharmacologicalActionDescriptor` record via the
            `iodi_descriptor_pharmacological_action_descriptor` method of the
            `DalMesh` class and its retrieval via the `get` method.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="NewDescriptor"
        )

        # IODI a new `DescriptorPharmacologicalActionDescriptor` record.
        obj_id = self.dal.iodi_descriptor_pharmacological_action_descriptor(
            descriptor_id=descriptor_id,
            pharmacological_action_descriptor_id=descriptor_02_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            DescriptorPharmacologicalActionDescriptor,
            obj_id,
        )  # type: DescriptorPharmacologicalActionDescriptor

        # Assert that the different fields of the record match.
        self.assertEqual(
            obj.descriptor_pharmacological_action_descriptor_id,
            1,
        )
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(
            obj.pharmacological_action_descriptor_id,
            descriptor_02_id,
        )

    def test_iodi_descriptor_pharmacological_action_descriptor_duplicate(
        self
    ):
        """ Tests the IODI insertion of duplicate
            `DescriptorPharmacologicalActionDescriptor` records to ensure
            deduplication functions as intended.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="NewDescriptor"
        )
        descriptor_03_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI3",
            name="NewerDescriptor"
        )

        # IODI a new `DescriptorPharmacologicalActionDescriptor` record.
        obj_id = self.dal.iodi_descriptor_pharmacological_action_descriptor(
            descriptor_id=descriptor_id,
            pharmacological_action_descriptor_id=descriptor_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `DescriptorPharmacologicalActionDescriptor`
        # record.
        obj_id = self.dal.iodi_descriptor_pharmacological_action_descriptor(
            descriptor_id=descriptor_id,
            pharmacological_action_descriptor_id=descriptor_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `DescriptorPharmacologicalActionDescriptor` record.
        obj_id = self.dal.iodi_descriptor_pharmacological_action_descriptor(
            descriptor_id=descriptor_id,
            pharmacological_action_descriptor_id=descriptor_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_descriptor_pharmacological_action_descriptor(self):
        """ Tests the deletion of a
            `DescriptorPharmacologicalActionDescriptor` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="NewDescriptor"
        )

        # IODI a new `DescriptorPharmacologicalActionDescriptor` record.
        obj_id = self.dal.iodi_descriptor_pharmacological_action_descriptor(
            descriptor_id=descriptor_id,
            pharmacological_action_descriptor_id=descriptor_02_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(DescriptorPharmacologicalActionDescriptor, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            DescriptorPharmacologicalActionDescriptor,
            obj_id,
        )  # type: DescriptorPharmacologicalActionDescriptor

        self.assertIsNone(obj)
