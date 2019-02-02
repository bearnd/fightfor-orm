# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the
`SupplementalPharmacologicalActionDescriptor` class as well as the
`iodi_supplemental_pharmacological_action_descriptor` method of the `DalMesh`
class.
"""

from fform.orm_mt import SupplementalPharmacologicalActionDescriptor

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_supplemental
from tests.assets.items_mt import create_descriptor


class DalMtTermSupplementalPharmacologicalActionDescriptorTest(DalMtTestBase):
    """ Defines unit-tests for the `SupplementalPharmacologicalActionDescriptor`
        class as well as the
        `iodi_supplemental_pharmacological_action_descriptor` method of the
        `DalMesh` class.
    """

    def test_iodi_get_supplemental_pharmacological_action_descriptor(self):
        """ Tests the IODI insertion of a
            `SupplementalPharmacologicalActionDescriptor` record via the
            `iodi_supplemental_pharmacological_action_descriptor` method of the
            `DalMesh` class and its retrieval via the `get` method.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal)

        # IODI a new `SupplementalPharmacologicalActionDescriptor` record.
        obj_id = self.dal.iodi_supplemental_pharmacological_action_descriptor(
            supplemental_id=supplemental_id,
            pharmacological_action_descriptor_id=descriptor_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            SupplementalPharmacologicalActionDescriptor,
            obj_id,
        )  # type: SupplementalPharmacologicalActionDescriptor

        # Assert that the different fields of the record match.
        self.assertEqual(
            obj.supplemental_pharmacological_action_descriptor_id,
            1,
        )
        self.assertEqual(obj.supplemental_id, supplemental_id)
        self.assertEqual(
            obj.pharmacological_action_descriptor_id,
            descriptor_id,
        )

    def test_iodi_supplemental_pharmacological_action_descriptor_duplicate(
        self
    ):
        """ Tests the IODI insertion of duplicate
            `SupplementalPharmacologicalActionDescriptor` records to ensure
            deduplication functions as intended.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal)
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="NewDescriptor"
        )

        # IODI a new `SupplementalPharmacologicalActionDescriptor` record.
        obj_id = self.dal.iodi_supplemental_pharmacological_action_descriptor(
            supplemental_id=supplemental_id,
            pharmacological_action_descriptor_id=descriptor_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `SupplementalPharmacologicalActionDescriptor`
        # record.
        obj_id = self.dal.iodi_supplemental_pharmacological_action_descriptor(
            supplemental_id=supplemental_id,
            pharmacological_action_descriptor_id=descriptor_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `SupplementalPharmacologicalActionDescriptor` record.
        obj_id = self.dal.iodi_supplemental_pharmacological_action_descriptor(
            supplemental_id=supplemental_id,
            pharmacological_action_descriptor_id=descriptor_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_supplemental_pharmacological_action_descriptor(self):
        """ Tests the deletion of a
            `SupplementalPharmacologicalActionDescriptor` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal)

        # IODI a new `SupplementalPharmacologicalActionDescriptor` record.
        obj_id = self.dal.iodi_supplemental_pharmacological_action_descriptor(
            supplemental_id=supplemental_id,
            pharmacological_action_descriptor_id=descriptor_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(SupplementalPharmacologicalActionDescriptor, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            SupplementalPharmacologicalActionDescriptor,
            obj_id,
        )  # type: SupplementalPharmacologicalActionDescriptor

        self.assertIsNone(obj)
