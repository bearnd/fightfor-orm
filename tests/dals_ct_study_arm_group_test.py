# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyArmGroup` class as well as the
`iodi_study_arm_group` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyArmGroup

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_arm_group


class DalCtStudyArmGroupTest(DalCtTestBase):

    def test_iodi_get_study_arm_group(self):
        """ Tests the insertion of a `StudyArmGroup` record via the
            `iodi_study_arm_group` method of the `DalClinicalTrials` class and
            its retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        arm_group_id, _ = create_arm_group(dal=self.dal)

        # IODI a new `StudyArmGroup` record.
        obj_id = self.dal.iodi_study_arm_group(
            study_id=study_id,
            arm_group_id=arm_group_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyArmGroup, obj_id)  # type: StudyArmGroup

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_arm_group_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.arm_group_id, arm_group_id)

    def test_iodi_study_arm_group_missing_fk(self):
        """ Tests the insertion of a `StudyArmGroup` record via the
            `iodi_study_arm_group` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_study_arm_group,
            # This FK is invalid.
            study_id=123,
            arm_group_id=123,
        )

    def test_iodi_study_arm_group_duplicate(self):
        """ Tests the IODI insertion of duplicate `StudyArmGroup` records to
            ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        arm_group_id, _ = create_arm_group(dal=self.dal)
        arm_group_02_id, _ = create_arm_group(dal=self.dal, label="new_label")

        # IODI a new `StudyArmGroup` record.
        obj_id = self.dal.iodi_study_arm_group(
            study_id=study_id,
            arm_group_id=arm_group_id,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `StudyArmGroup` record as before.
        obj_id = self.dal.iodi_study_arm_group(
            study_id=study_id,
            arm_group_id=arm_group_id,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `StudyArmGroup` record.
        obj_id = self.dal.iodi_study_arm_group(
            study_id=study_id,
            arm_group_id=arm_group_02_id,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyArmGroup` record as before.
        obj_id = self.dal.iodi_study_arm_group(
            study_id=study_id,
            arm_group_id=arm_group_02_id,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_arm_group(self):
        """ Tests the deletion of a `StudyArmGroup` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        arm_group_id, _ = create_arm_group(dal=self.dal)

        # IODI a new `StudyArmGroup` record.
        obj_id = self.dal.iodi_study_arm_group(
            study_id=study_id,
            arm_group_id=arm_group_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyArmGroup, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyArmGroup, obj_id)  # type: StudyArmGroup

        self.assertIsNone(obj)
