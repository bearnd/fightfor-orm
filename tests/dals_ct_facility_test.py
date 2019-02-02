# -*- coding: utf-8 -*-

from fform.orm_ct import Facility

from tests.bases import DalCtTestBase


class DalCtFacilityTest(DalCtTestBase):

    def test_iodi_get_facility(self):
        """Tests the insertion of a `Facility` record via the `iodi_facility`
        method of the `DalClinicalTrials` class and its retrieval via the `get`
        method."""

        # IODI a new `Facility` record.
        obj_id = self.dal.iodi_facility(
            name="Mayo Clinic",
            city="Rochester",
            state="Minnesota",
            zip_code="55905",
            country="United States",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Facility, obj_id)  # type: Facility

        # Assert that the different fields of the record match.
        self.assertEqual(obj.facility_id, 1)
        self.assertEqual(obj.name, "Mayo Clinic")
        self.assertEqual(obj.city, "Rochester")
        self.assertEqual(obj.state, "Minnesota")
        self.assertEqual(obj.zip_code, "55905")
        self.assertEqual(obj.country, "United States")

    def test_iodi_facility_duplicate(self):
        """Tests the IODI insertion of duplicate `Facility` records to ensure
        deduplication functions as intended."""

        # IODI a `Facility` record.
        obj_id = self.dal.iodi_facility(
            name="Mayo Clinic",
            city="Rochester",
            state="Minnesota",
            zip_code="55905",
            country="United States",
        )

        self.assertEqual(obj_id, 1)

        # IODI the same `Facility` record as before.
        obj_id = self.dal.iodi_facility(
            name="Mayo Clinic",
            city="Rochester",
            state="Minnesota",
            zip_code="55905",
            country="United States",
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `Facility` record (while still having the sama name).
        obj_id = self.dal.iodi_facility(
            name="Mayo Clinic",
            city="Jacksonville",
            state="Florida",
            zip_code="32224",
            country="United States",
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `Facility` record as before but with mixed casing.
        obj_id = self.dal.iodi_facility(
            name="mayo clinic",
            city="jacksonville",
            state="florida",
            zip_code="32224",
            country="United States",
        )

        self.assertEqual(obj_id, 3)

    def test_delete_facility(self):
        """Tests the deletion of a `Facility` record via the `delete` method of
        the `DalClinicalTrials` class."""

        # IODI a new `Facility` record.
        obj_id = self.dal.iodi_facility(
            name="Mayo Clinic",
            city="Rochester",
            state="Minnesota",
            zip_code="55905",
            country="United States",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Facility, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Facility, obj_id)  # type: Facility

        self.assertIsNone(obj)
