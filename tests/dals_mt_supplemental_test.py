# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Supplemental` class as well as the
`iodu_supplemental` method of the `DalMesh` class.
"""

from fform.orm_mt import Supplemental

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_supplemental


class DalMtSupplementalTest(DalMtTestBase):

    def test_iodu_get_supplemental(self):
        """ Tests the IODU insertion of a `Supplemental` record via the
            `iodu_supplemental` method of the `DalMesh` class and its retrieval
            via the `get` method.
        """

        # Create a new `Supplemental` record.
        obj_id, refr = create_supplemental(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Supplemental, obj_id)  # type: Supplemental

        # Assert that the different fields of the record match.
        self.assertEqual(obj.supplemental_id, obj_id)
        self.assertEqual(obj.ui, refr["ui"])
        self.assertEqual(obj.name, refr["name"])
        self.assertEqual(obj.created, refr["created"])
        self.assertEqual(obj.revised, refr["revised"])
        self.assertEqual(obj.note, refr["note"])
        self.assertEqual(obj.frequency, refr["frequency"])

    def test_iodu_supplemental_duplicate(self):
        """ Tests the IODU insertion of duplicate `Supplemental` records to
            ensure deduplication functions as intended.
        """

        # Create a new `Supplemental` record.
        obj_id, refr = create_supplemental(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Supplemental` record.
        obj_id, refr = create_supplemental(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Supplemental` record with a changed `note` field which
        # should trigger an update on the existing record.
        obj_id, refr = create_supplemental(
            dal=self.dal,
            note="different note"
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Supplemental, obj_id)  # type: Supplemental

        self.assertEqual(obj.note, "different note")

        # IODU a new `Supplemental` record.
        obj_id, refr = create_supplemental(
            dal=self.dal,
            ui="C000003",
            name="NewSupplemental"
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Supplemental` record as before.
        obj_id, refr = create_supplemental(
            dal=self.dal,
            ui="C000003",
            name="NewSupplemental"
        )

        self.assertEqual(obj_id, 4)

    def test_delete_supplemental(self):
        """ Tests the deletion of a `Supplemental` record via the `delete`
            method of the `DalMesh` class.
        """

        # Create a new `Supplemental` record.
        obj_id, refr = create_supplemental(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Supplemental, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Supplemental, obj_id)  # type: Supplemental

        self.assertIsNone(obj)

    def test_update_supplemental(self):
        """ Tests the update of a `Supplemental` record via the `update` method
            of the `DalMesh` class.
        """

        # Create a new `Supplemental` record.
        obj_id, refr = create_supplemental(dal=self.dal)

        # Retrieve the new record.
        obj_original = self.dal.get(Supplemental, obj_id)  # type: Supplemental

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.supplemental_id, obj_id)
        self.assertEqual(obj_original.ui, refr["ui"])
        self.assertEqual(obj_original.name, refr["name"])
        self.assertEqual(obj_original.created, refr["created"])
        self.assertEqual(obj_original.revised, refr["revised"])
        self.assertEqual(obj_original.note, refr["note"])
        self.assertEqual(obj_original.frequency, refr["frequency"])

        # Update the record.
        self.dal.update_attr_value(
            Supplemental,
            obj_id,
            "note",
            "different note",
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(Supplemental, obj_id)  # type: Supplemental

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.supplemental_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.note, "different note")
