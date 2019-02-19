# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Contact` class as well as the
`iodi_contact` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import Contact

from tests.bases import DalCtTestBase


class DalCtContactTest(DalCtTestBase):

    def test_iodi_get_contact(self):
        """Tests the insertion of a `Contact` record via the `iodi_contact`
        method of the `DalClinicalTrials` class and its retrieval via the `get`
        method."""

        # IODI a new `Person` record as a fixture.
        person_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        # IODI a new `Contact` record.
        obj_id = self.dal.iodi_contact(
            person_id=person_id,
            phone="1",
            phone_ext="2",
            email="adam@bearnd.io"
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Contact, obj_id)  # type: Contact

        # Assert that the different fields of the record match.
        self.assertEqual(obj.contact_id, 1)
        self.assertEqual(obj.person_id, person_id)
        self.assertEqual(obj.phone, "1")
        self.assertEqual(obj.phone_ext, "2")
        self.assertEqual(obj.email, "adam@bearnd.io")

    def test_iodi_contact_missing_fk(self):
        """Tests the insertion of a `Contact` record via the `iodi_contact`
        method when the required FK is non-existing."""

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_contact,
            # This FK is invalid.
            person_id=123,
            phone="1",
            phone_ext="2",
            email="adam@bearnd.io"
        )

    def test_iodi_contact_duplicate(self):
        """Tests the IODI insertion of duplicate `Contact` records to ensure
        deduplication functions as intended."""

        # IODI a new `Person` record as a fixture.
        person_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        # IODI a new `Contact` record.
        obj_id = self.dal.iodi_contact(
            person_id=person_id,
            phone="1",
            phone_ext="2",
            email="adam@bearnd.io"
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `Contact` record as before.
        obj_id = self.dal.iodi_contact(
            person_id=person_id,
            phone="1",
            phone_ext="2",
            email="adam@bearnd.io"
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `Contact` record.
        obj_id = self.dal.iodi_contact(
            person_id=person_id,
            phone="100",
            phone_ext="200",
            email="adam@bearnd.io"
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

    def test_delete_contact(self):
        """Tests the deletion of a `Contact` record via the `delete` method of
        the `DalClinicalTrials` class."""

        # IODI a new `Person` record as a fixture.
        person_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        # IODI a new `Contact` record.
        obj_id = self.dal.iodi_contact(
            person_id=person_id,
            phone="1",
            phone_ext="2",
            email="adam@bearnd.io"
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Contact, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Contact, obj_id)  # type: Contact

        self.assertIsNone(obj)
