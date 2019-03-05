# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyCondition` class as well as the
`iodi_study_condition` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyCondition

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_condition


class DalCtStudyConditionTest(DalCtTestBase):

    def test_iodi_get_study_condition(self):
        """ Tests the insertion of a `StudyCondition` record via the
            `iodi_study_condition` method of the `DalClinicalTrials` class and
            its retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        condition_id, _ = create_condition(dal=self.dal)

        # IODI a new `StudyCondition` record.
        obj_id = self.dal.iodi_study_condition(
            study_id=study_id,
            condition_id=condition_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyCondition, obj_id)  # type: StudyCondition

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_condition_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.condition_id, condition_id)

    def test_iodi_study_condition_missing_fk(self):
        """ Tests the insertion of a `StudyCondition` record via the
            `iodi_study_condition` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_study_condition,
            # This FK is invalid.
            study_id=123,
            condition_id=123,
        )

    def test_iodi_study_condition_duplicate(self):
        """ Tests the IODI insertion of duplicate `StudyCondition` records to
            ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        condition_id, _ = create_condition(dal=self.dal)
        condition_02_id, _ = create_condition(
            dal=self.dal,
            condition="new_condition",
        )

        # IODI a new `StudyCondition` record.
        obj_id = self.dal.iodi_study_condition(
            study_id=study_id,
            condition_id=condition_id,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `StudyCondition` record as before.
        obj_id = self.dal.iodi_study_condition(
            study_id=study_id,
            condition_id=condition_id,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `StudyCondition` record.
        obj_id = self.dal.iodi_study_condition(
            study_id=study_id,
            condition_id=condition_02_id,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyCondition` record as before.
        obj_id = self.dal.iodi_study_condition(
            study_id=study_id,
            condition_id=condition_02_id,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_condition(self):
        """ Tests the deletion of a `StudyCondition` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        condition_id, _ = create_condition(dal=self.dal)

        # IODI a new `StudyCondition` record.
        obj_id = self.dal.iodi_study_condition(
            study_id=study_id,
            condition_id=condition_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyCondition, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyCondition, obj_id)  # type: StudyCondition

        self.assertIsNone(obj)
