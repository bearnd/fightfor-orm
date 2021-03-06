# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyLocation` class as well as the
`iodi_study_location` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyLocation
from fform.orm_ct import RecruitmentStatusType

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_facility
from tests.assets.items_ct import create_location


class DalCtStudyLocationTest(DalCtTestBase):

    def test_iodi_get_study_location(self):
        """ Tests the insertion of a `StudyLocation` record via the
            `iodi_study_location` method of the `DalClinicalTrials` class
            and its retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        location_id, _ = create_location(dal=self.dal)

        # IODI a new `StudyLocation` record.
        obj_id = self.dal.iodi_study_location(
            study_id=study_id,
            location_id=location_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyLocation, obj_id)  # type: StudyLocation

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_location_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.location_id, location_id)

    def test_iodi_study_location_missing_fk(self):
        """ Tests the insertion of a `StudyLocation` record via the
            `iodi_study_location` method when the required FK is
            non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_study_location,
            # This FK is invalid.
            study_id=123,
            location_id=123,
        )

    def test_iodi_study_location_duplicate(self):
        """ Tests the IODI insertion of duplicate `StudyLocation` records
            to ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        location_id, _ = create_location(dal=self.dal)
        facility_id, _ = create_facility(dal=self.dal, name="new_facility")
        location_02_id, _ = create_location(
            dal=self.dal,
            facility_id=facility_id,
        )

        # IODI a new `StudyLocation` record.
        obj_id = self.dal.iodi_study_location(
            study_id=study_id,
            location_id=location_id,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `StudyLocation` record as before.
        obj_id = self.dal.iodi_study_location(
            study_id=study_id,
            location_id=location_id,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `StudyLocation` record.
        obj_id = self.dal.iodi_study_location(
            study_id=study_id,
            location_id=location_02_id,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyLocation` record as before.
        obj_id = self.dal.iodi_study_location(
            study_id=study_id,
            location_id=location_02_id,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_location(self):
        """ Tests the deletion of a `StudyLocation` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        location_id, _ = create_location(dal=self.dal)

        # IODI a new `StudyLocation` record.
        obj_id = self.dal.iodi_study_location(
            study_id=study_id,
            location_id=location_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyLocation, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyLocation, obj_id)  # type: StudyLocation

        self.assertIsNone(obj)
