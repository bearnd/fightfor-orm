# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Term` class as well as the `iodu_term`
method of the `DalMesh` class.
"""

from fform.orm_mt import Term

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_term


class DalMtTermTest(DalMtTestBase):

    def test_iodu_get_term(self):
        """ Tests the IODU insertion of a `Term` record via the `iodu_term`
            method of the `DalMesh` class and its retrieval via the `get`
            method.
        """

        # Create a new `Term` record.
        obj_id, refr = create_term(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Term, obj_id)  # type: Term

        # Assert that the different fields of the record match.
        self.assertEqual(obj.term_id, obj_id)
        self.assertEqual(obj.ui, refr["ui"])
        self.assertEqual(obj.name, refr["name"])
        self.assertEqual(obj.created, refr["created"])
        self.assertEqual(obj.abbreviation, refr["abbreviation"])
        self.assertEqual(obj.sort_version, refr["sort_version"])
        self.assertEqual(obj.entry_version, refr["entry_version"])
        self.assertEqual(obj.note, refr["note"])

    def test_iodu_term_duplicate(self):
        """ Tests the IODU insertion of duplicate `Term` records to ensure
            deduplication functions as intended.
        """

        # Create a new `Term` record.
        obj_id, refr = create_term(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Term` record.
        obj_id, refr = create_term(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # IODU the same `Term` record with a changed `note` field which should
        # trigger an update on the existing record.
        obj_id, refr = create_term(
            dal=self.dal,
            note="SomethingDifferent"
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Term, obj_id)  # type: Term

        self.assertEqual(obj.note, "SomethingDifferent")

        # IODU a new `Term` record.
        obj_id, refr = create_term(
            dal=self.dal,
            ui="T000049",
            name="NewTerm"
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Term` record as before.
        obj_id, refr = create_term(
            dal=self.dal,
            ui="T000049",
            name="NewTerm"
        )

        self.assertEqual(obj_id, 4)

    def test_delete_term(self):
        """ Tests the deletion of a `Term` record via the `delete` method of the
            `DalMesh` class.
        """

        # Create a new `Term` record.
        obj_id, refr = create_term(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Term, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Term, obj_id)  # type: Term

        self.assertIsNone(obj)

    def test_update_term(self):
        """ Tests the update of a `Term` record via the `update` method of
            the `DalMesh` class.
        """

        # Create a new `Term` record.
        obj_id, refr = create_term(dal=self.dal)

        # Retrieve the new record.
        obj_original = self.dal.get(Term, obj_id)  # type: Term

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.term_id, obj_id)
        self.assertEqual(obj_original.ui, refr["ui"])
        self.assertEqual(obj_original.name, refr["name"])
        self.assertEqual(obj_original.created, refr["created"])
        self.assertEqual(obj_original.abbreviation, refr["abbreviation"])
        self.assertEqual(obj_original.sort_version, refr["sort_version"])
        self.assertEqual(obj_original.entry_version, refr["entry_version"])
        self.assertEqual(obj_original.note, refr["note"])

        # Update the record.
        self.dal.update_attr_value(
            Term,
            obj_id,
            "note",
            "New note",
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(Term, obj_id)  # type: Term

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.term_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.note, "New note")
