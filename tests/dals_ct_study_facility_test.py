# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyFacility` class as well as the
`iodu_study_facility` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyFacility

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_facility


class DalCtStudyFacilityTest(DalCtTestBase):

    def test_iodu_get_study_facility(self):
        """ Tests the insertion of a `StudyFacility` record via the
            `iodu_study_facility` method of the `DalClinicalTrials` class and its
            retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        facility_id, _ = create_facility(dal=self.dal)

        # IODU a new `StudyFacility` record.
        obj_id = self.dal.iodu_study_facility(
            study_id=study_id,
            facility_id=facility_id,
            facility_canonical_id=None,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyFacility, obj_id)  # type: StudyFacility

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_facility_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.facility_id, facility_id)
        self.assertEqual(obj.facility_canonical_id, None)

    def test_iodu_study_facility_missing_fk(self):
        """ Tests the insertion of a `StudyFacility` record via the
            `iodu_study_facility` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodu_study_facility,
            # This FK is invalid.
            study_id=123,
            facility_id=123,
            facility_canonical_id=None,
        )

    def test_iodu_study_facility_duplicate(self):
        """ Tests the IODU insertion of duplicate `StudyFacility` records to
            ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        facility_id, _ = create_facility(dal=self.dal)
        facility_02_id, _ = create_facility(dal=self.dal, name="new_name")

        # IODU a new `StudyFacility` record.
        obj_id = self.dal.iodu_study_facility(
            study_id=study_id,
            facility_id=facility_id,
            facility_canonical_id=None,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODU the same `StudyFacility` record as before.
        obj_id = self.dal.iodu_study_facility(
            study_id=study_id,
            facility_id=facility_id,
            facility_canonical_id=None,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODU a new `StudyFacility` record.
        obj_id = self.dal.iodu_study_facility(
            study_id=study_id,
            facility_id=facility_02_id,
            facility_canonical_id=None,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyFacility` record as before.
        obj_id = self.dal.iodu_study_facility(
            study_id=study_id,
            facility_id=facility_02_id,
            facility_canonical_id=None,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_facility(self):
        """ Tests the deletion of a `StudyFacility` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        facility_id, _ = create_facility(dal=self.dal)

        # IODU a new `StudyFacility` record.
        obj_id = self.dal.iodu_study_facility(
            study_id=study_id,
            facility_id=facility_id,
            facility_canonical_id=None,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyFacility, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyFacility, obj_id)  # type: StudyFacility

        self.assertIsNone(obj)
