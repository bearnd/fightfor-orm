# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Concept` class as well as the
`iodu_concept` method of the `DalMesh` class.
"""

from fform.orm_mt import Concept

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_concept


class DalMtConceptTest(DalMtTestBase):

    def test_iodu_get_concept(self):
        """ Tests the IODU insertion of a `Concept` record via the
            `iodu_concept` method of the `DalMesh` class and its retrieval via
            the `get` method.
        """

        # Create a new `Concept` record.
        obj_id, refr = create_concept(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Concept, obj_id)  # type: Concept

        # Assert that the different fields of the record match.
        self.assertEqual(obj.concept_id, obj_id)
        self.assertEqual(obj.ui, refr["ui"])
        self.assertEqual(obj.name, refr["name"])
        self.assertEqual(obj.casn1_name, refr["casn1_name"])
        self.assertEqual(obj.registry_number, refr["registry_number"])
        self.assertEqual(obj.scope_note, refr["scope_note"])
        self.assertEqual(
            obj.translators_english_scope_note,
            refr["translators_english_scope_note"],
        )
        self.assertEqual(
            obj.translators_scope_note,
            refr["translators_scope_note"],
        )

    def test_iodu_concept_duplicate(self):
        """ Tests the IODU insertion of duplicate `Concept` records to ensure
            deduplication functions as intended.
        """

        # Create a new `Concept` record.
        obj_id, refr = create_concept(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Term` record.
        obj_id, refr = create_concept(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Term` record with a changed `scope_note` field which
        # should trigger an update on the existing record.
        obj_id, refr = create_concept(
            dal=self.dal,
            scope_note="different scope note"
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Concept, obj_id)  # type: Concept

        self.assertEqual(obj.scope_note, "different scope note")

        # IODU a new `Concept` record.
        obj_id, refr = create_concept(
            dal=self.dal,
            ui="M0000034",
            name="Different name"
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Concept` record as before.
        obj_id, refr = create_concept(
            dal=self.dal,
            ui="M0000034",
            name="Different name"
        )

        self.assertEqual(obj_id, 4)

    def test_delete_concept(self):
        """ Tests the deletion of a `Concept` record via the `delete` method of
            the `DalMesh` class.
        """

        # Create a new `Concept` record.
        obj_id, refr = create_concept(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Concept, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Concept, obj_id)  # type: Concept

        self.assertIsNone(obj)

    def test_update_concept(self):
        """ Tests the update of a `Concept` record via the `update` method of
            the `DalMesh` class.
        """

        # Create a new `Concept` record.
        obj_id, refr = create_concept(dal=self.dal)

        # Retrieve the new record.
        obj_original = self.dal.get(Concept, obj_id)  # type: Concept

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.concept_id, obj_id)
        self.assertEqual(obj_original.ui, refr["ui"])
        self.assertEqual(obj_original.name, refr["name"])
        self.assertEqual(obj_original.casn1_name, refr["casn1_name"])
        self.assertEqual(obj_original.registry_number, refr["registry_number"])
        self.assertEqual(obj_original.scope_note, refr["scope_note"])
        self.assertEqual(
            obj_original.translators_english_scope_note,
            refr["translators_english_scope_note"],
        )
        self.assertEqual(
            obj_original.translators_scope_note,
            refr["translators_scope_note"],
        )

        # Update the record.
        self.dal.update_attr_value(
            Concept,
            obj_id,
            "scope_note",
            "New scope note",
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(Concept, obj_id)  # type: Concept

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.concept_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.scope_note, "New scope note")
