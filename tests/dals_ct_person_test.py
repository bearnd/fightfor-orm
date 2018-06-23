# coding=utf-8

from fform.orm_ct import Person

from tests.bases import DalCtTestBase


class DalCtPersonTest(DalCtTestBase):

    def test_iodi_get_person(self):
        """Tests the insertion of a `Person` record via the `iodi_person`
        method of the `DalClinicalTrials` class and its retrieval via the `get`
        method."""

        # IODI a new `Person` record.
        obj_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Person, obj_id)  # type: Person

        # Assert that the different fields of the record match.
        self.assertEqual(obj.person_id, 1)
        self.assertEqual(obj.name_first, "Adamos")
        self.assertEqual(obj.name_middle, None)
        self.assertEqual(obj.name_last, "Kyriakou")
        self.assertEqual(obj.degrees, "M.Sc., Ph.D.")

    def test_iodi_keyword_duplicate(self):
        """Tests the IODI insertion of duplicate `Person` records to ensure
        deduplication functions as intended."""

        # IODI a `Person` record.
        obj_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        self.assertEqual(obj_id, 1)

        # IODI the same `Person` record as before.
        obj_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `Person` record.
        obj_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle="Someone else",
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `Person` record as before but with mixed casing.
        obj_id = self.dal.iodi_person(
            name_first="aDamos",
            name_middle="someone else",
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        self.assertEqual(obj_id, 3)

    def test_delete_person(self):
        """Tests the deletion of a `Person` record via the `delete` method of
        the `DalClinicalTrials` class."""

        # IODI a new `Person` record.
        obj_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Person, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Person, obj_id)  # type: Person

        self.assertIsNone(obj)
