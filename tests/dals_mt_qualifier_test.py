# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Qualifier` class as well as the
`iodu_qualifier` method of the `DalMesh` class.
"""

from fform.orm_mt import Qualifier

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_qualifier


class DalMtQualifierTest(DalMtTestBase):

    def test_iodu_get_qualifier(self):
        """ Tests the IODU insertion of a `Qualifier` record via the
            `iodu_qualifier` method of the `DalMesh` class and its retrieval
            via the `get` method.
        """

        # Create a new `Qualifier` record.
        obj_id, refr = create_qualifier(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Qualifier, obj_id)  # type: Qualifier

        # Assert that the different fields of the record match.
        self.assertEqual(obj.qualifier_id, obj_id)
        self.assertEqual(obj.ui, refr["ui"])
        self.assertEqual(obj.name, refr["name"])
        self.assertEqual(obj.created, refr["created"])
        self.assertEqual(obj.revised, refr["revised"])
        self.assertEqual(obj.established, refr["established"])
        self.assertEqual(obj.annotation, refr["annotation"])
        self.assertEqual(obj.history_note, refr["history_note"])
        self.assertEqual(obj.online_note, refr["online_note"])

    def test_iodu_qualifier_duplicate(self):
        """ Tests the IODU insertion of duplicate `Qualifier` records to ensure
            deduplication functions as intended.
        """

        # Create a new `Qualifier` record.
        obj_id, refr = create_qualifier(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Qualifier` record.
        obj_id, refr = create_qualifier(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Qualifier` record with a changed `history_note` field
        # which should trigger an update on the existing record.
        obj_id, refr = create_qualifier(
            dal=self.dal,
            history_note="different history note"
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Qualifier, obj_id)  # type: Qualifier

        self.assertEqual(obj.history_note, "different history note")

        # IODU a new `Qualifier` record.
        obj_id, refr = create_qualifier(
            dal=self.dal,
            ui="Q000000982",
            name="NewQualifier"
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Qualifier` record as before.
        obj_id, refr = create_qualifier(
            dal=self.dal,
            ui="Q000000982",
            name="NewQualifier"
        )

        self.assertEqual(obj_id, 4)

    def test_delete_qualifier(self):
        """ Tests the deletion of a `Qualifier` record via the `delete` method
            of the `DalMesh` class.
        """

        # Create a new `Qualifier` record.
        obj_id, refr = create_qualifier(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Qualifier, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Qualifier, obj_id)  # type: Qualifier

        self.assertIsNone(obj)

    def test_update_qualifier(self):
        """ Tests the update of a `Qualifier` record via the `update` method of
            the `DalMesh` class.
        """

        # Create a new `Qualifier` record.
        obj_id, refr = create_qualifier(dal=self.dal)

        # Retrieve the new record.
        obj_original = self.dal.get(Qualifier, obj_id)  # type: Qualifier

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.qualifier_id, obj_id)
        self.assertEqual(obj_original.ui, refr["ui"])
        self.assertEqual(obj_original.name, refr["name"])
        self.assertEqual(obj_original.created, refr["created"])
        self.assertEqual(obj_original.revised, refr["revised"])
        self.assertEqual(obj_original.established, refr["established"])
        self.assertEqual(obj_original.annotation, refr["annotation"])
        self.assertEqual(obj_original.history_note, refr["history_note"])
        self.assertEqual(obj_original.online_note, refr["online_note"])

        # Update the record.
        self.dal.update_attr_value(
            Qualifier,
            obj_id,
            "history_note",
            "different history note",
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(Qualifier, obj_id)  # type: Qualifier

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.qualifier_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.history_note, "different history note")
