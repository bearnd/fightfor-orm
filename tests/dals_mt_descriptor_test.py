# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Descriptor` class as well as the
`iodu_descriptor` method of the `DalMesh` class.
"""

from fform.orm_mt import Descriptor

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_descriptor


class DalMtDescriptorTest(DalMtTestBase):

    def test_iodu_get_descriptor(self):
        """ Tests the IODU insertion of a `Descriptor` record via the
            `iodu_descriptor` method of the `DalMesh` class and its retrieval
            via the `get` method.
        """

        # Create a new `Descriptor` record.
        obj_id, refr = create_descriptor(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Descriptor, obj_id)  # type: Descriptor

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_id, obj_id)
        self.assertEqual(obj.ui, refr["ui"])
        self.assertEqual(obj.name, refr["name"])
        self.assertEqual(obj.created, refr["created"])
        self.assertEqual(obj.revised, refr["revised"])
        self.assertEqual(obj.established, refr["established"])
        self.assertEqual(obj.annotation, refr["annotation"])
        self.assertEqual(obj.history_note, refr["history_note"])
        self.assertEqual(
            obj.nlm_classification_number,
            refr["nlm_classification_number"],
        )
        self.assertEqual(obj.online_note, refr["online_note"])
        self.assertEqual(obj.public_mesh_note, refr["public_mesh_note"])
        self.assertEqual(obj.consider_also, refr["consider_also"])

    def test_iodu_descriptor_duplicate(self):
        """ Tests the IODU insertion of duplicate `Descriptor` records to ensure
            deduplication functions as intended.
        """

        # Create a new `Descriptor` record.
        obj_id, refr = create_descriptor(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Descriptor` record.
        obj_id, refr = create_descriptor(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Descriptor` record with a changed `history_note` field
        # which should trigger an update on the existing record.
        obj_id, refr = create_descriptor(
            dal=self.dal,
            history_note="different history note"
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Descriptor, obj_id)  # type: Descriptor

        self.assertEqual(obj.history_note, "different history note")

        # IODU a new `Descriptor` record.
        obj_id, refr = create_descriptor(
            dal=self.dal,
            ui="D000057",
            name="NewDescriptor"
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Descriptor` record as before.
        obj_id, refr = create_descriptor(
            dal=self.dal,
            ui="D000057",
            name="NewDescriptor"
        )

        self.assertEqual(obj_id, 4)

    def test_delete_descriptor(self):
        """ Tests the deletion of a `Descriptor` record via the `delete` method
            of the `DalMesh` class.
        """

        # Create a new `Descriptor` record.
        obj_id, refr = create_descriptor(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Descriptor, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Descriptor, obj_id)  # type: Descriptor

        self.assertIsNone(obj)

    def test_update_descriptor(self):
        """ Tests the update of a `Descriptor` record via the `update` method of
            the `DalMesh` class.
        """

        # Create a new `Descriptor` record.
        obj_id, refr = create_descriptor(dal=self.dal)

        # Retrieve the new record.
        obj_original = self.dal.get(Descriptor, obj_id)  # type: Descriptor

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.descriptor_id, obj_id)
        self.assertEqual(obj_original.ui, refr["ui"])
        self.assertEqual(obj_original.name, refr["name"])
        self.assertEqual(obj_original.created, refr["created"])
        self.assertEqual(obj_original.revised, refr["revised"])
        self.assertEqual(obj_original.established, refr["established"])
        self.assertEqual(obj_original.annotation, refr["annotation"])
        self.assertEqual(obj_original.history_note, refr["history_note"])
        self.assertEqual(
            obj_original.nlm_classification_number,
            refr["nlm_classification_number"],
        )
        self.assertEqual(obj_original.online_note, refr["online_note"])
        self.assertEqual(obj_original.public_mesh_note, refr["public_mesh_note"])
        self.assertEqual(obj_original.consider_also, refr["consider_also"])

        # Update the record.
        self.dal.update_attr_value(
            Descriptor,
            obj_id,
            "history_note",
            "different history note",
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(Descriptor, obj_id)  # type: Descriptor

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.qualifier_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.history_note, "different history note")
