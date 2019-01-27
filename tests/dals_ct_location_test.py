# -*- coding: utf-8 -*-

from fform.orm_ct import Location
from fform.orm_ct import RecruitmentStatusType

from tests.bases import DalCtTestBase


class DalCtLocationTest(DalCtTestBase):

    def _create_fixtures(self):
        """Creates fixture records for the unit-tests."""

        # IODI a new `Person` record as a fixture.
        person_id_01 = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        # IODI a new `Person` record as a fixture.
        person_id_02 = self.dal.iodi_person(
            name_first="Teigane",
            name_middle="Jaed",
            name_last="Mackay",
            degrees="B.Sc."
        )

        # IODI a new `Contact` record as a fixture.
        contact_id_01 = self.dal.iodi_contact(
            person_id=person_id_01,
            phone=None,
            phone_ext=None,
            email="adam@bearnd.io"
        )

        # IODI a new `Contact` record as a fixture.
        contact_id_02 = self.dal.iodi_contact(
            person_id=person_id_02,
            phone=None,
            phone_ext=None,
            email="teigane@bearnd.io"
        )

        # IODI a new `Facility` record.
        facility_id = self.dal.iodi_facility(
            name="Mayo Clinic",
            city="Rochester",
            state="Minnesota",
            zip_code="55905",
            country="United States",
        )

        return (
            person_id_01,
            person_id_02,
            contact_id_01,
            contact_id_02,
            facility_id
        )

    def test_iodu_get_location(self):
        """Tests the insertion of a `Location` record via the `iodu_location`
        method of the `DalClinicalTrials` class and its retrieval via the `get`
        method."""

        (
            person_id_01,
            person_id_02,
            contact_id_01,
            contact_id_02,
            facility_id
        ) = self._create_fixtures()

        # IODU a new `Location` record.
        obj_id = self.dal.iodu_location(
            facility_id=facility_id,
            status=RecruitmentStatusType.RECRUITING,
            contact_primary_id=contact_id_01,
            contact_backup_id=contact_id_02
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Location, obj_id)  # type: Location

        # Assert that the different fields of the record match.
        self.assertEqual(obj.location_id, 1)
        self.assertEqual(obj.facility_id, facility_id)
        self.assertEqual(obj.status, RecruitmentStatusType.RECRUITING)
        self.assertEqual(obj.contact_primary_id, contact_id_01)
        self.assertEqual(obj.contact_backup_id, contact_id_02)

    def test_iodu_location_duplicate(self):
        """Tests the IODU insertion of duplicate `Location` records to ensure
        deduplication functions as intended."""

        (
            person_id_01,
            person_id_02,
            contact_id_01,
            contact_id_02,
            facility_id
        ) = self._create_fixtures()

        # IODU a new `Location` record.
        obj_id = self.dal.iodu_location(
            facility_id=facility_id,
            status=RecruitmentStatusType.RECRUITING,
            contact_primary_id=contact_id_01,
            contact_backup_id=contact_id_02
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `Location` record.
        obj_id = self.dal.iodu_location(
            facility_id=facility_id,
            status=RecruitmentStatusType.RECRUITING,
            contact_primary_id=contact_id_01,
            contact_backup_id=contact_id_02
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Location, obj_id)  # type: Location

        self.assertEqual(obj.status, RecruitmentStatusType.RECRUITING)

        # IODU the same `Location` record with a changed `status` field which
        # should trigger an update.
        obj_id = self.dal.iodu_location(
            facility_id=facility_id,
            status=RecruitmentStatusType.COMPLETED,
            contact_primary_id=contact_id_01,
            contact_backup_id=contact_id_02
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Location, obj_id)  # type: Location

        self.assertEqual(obj.status, RecruitmentStatusType.COMPLETED)

        # IODU a new `Location` record.
        obj_id = self.dal.iodu_location(
            facility_id=facility_id,
            status=None,
            contact_primary_id=None,
            contact_backup_id=None,
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Location` record as before.
        obj_id = self.dal.iodu_location(
            facility_id=facility_id,
            status=None,
            contact_primary_id=None,
            contact_backup_id=None,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_person(self):
        """Tests the deletion of a `Location` record via the `delete` method of
        the `DalClinicalTrials` class."""

        (
            person_id_01,
            person_id_02,
            contact_id_01,
            contact_id_02,
            facility_id
        ) = self._create_fixtures()

        # IODU a new `Location` record.
        obj_id = self.dal.iodu_location(
            facility_id=facility_id,
            status=RecruitmentStatusType.RECRUITING,
            contact_primary_id=contact_id_01,
            contact_backup_id=contact_id_02
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Location, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Location, obj_id)  # type: Location

        self.assertIsNone(obj)

    def test_update_location(self):
        """Tests the update of a `Location` record via the `update` method of
        the `DalClinicalTrials` class."""

        (
            person_id_01,
            person_id_02,
            contact_id_01,
            contact_id_02,
            facility_id
        ) = self._create_fixtures()

        # IODU a new `Location` record.
        obj_id = self.dal.iodu_location(
            facility_id=facility_id,
            status=RecruitmentStatusType.RECRUITING,
            contact_primary_id=contact_id_01,
            contact_backup_id=contact_id_02
        )

        # Retrieve the new record.
        obj_original = self.dal.get(Location, obj_id)  # type: Location

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.location_id, 1)
        self.assertEqual(obj_original.facility_id, facility_id)
        self.assertEqual(obj_original.status, RecruitmentStatusType.RECRUITING)
        self.assertEqual(obj_original.contact_primary_id, contact_id_01)
        self.assertEqual(obj_original.contact_backup_id, contact_id_02)

        # Update the record.
        self.dal.update_attr_value(
            Location,
            obj_id,
            "status",
            RecruitmentStatusType.COMPLETED,
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(Location, obj_id)  # type: Location

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.location_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.status, RecruitmentStatusType.COMPLETED)
