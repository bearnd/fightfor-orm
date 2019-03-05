# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyOutcome` class as well as the
`iodu_study_outcome` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyOutcome
from fform.orm_ct import OutcomeType

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_protocol_outcome


class DalCtStudyOutcomeTest(DalCtTestBase):

    def test_iodu_get_study_outcome(self):
        """ Tests the insertion of a `StudyOutcome` record via the
            `iodu_study_outcome` method of the `DalClinicalTrials` class and its
            retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        protocol_outcome_id, _ = create_protocol_outcome(dal=self.dal)

        # IODU a new `StudyOutcome` record.
        obj_id = self.dal.iodu_study_outcome(
            study_id=study_id,
            protocol_outcome_id=protocol_outcome_id,
            outcome_type=OutcomeType.PRIMARY,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyOutcome, obj_id)  # type: StudyOutcome

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_outcome_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.protocol_outcome_id, protocol_outcome_id)
        self.assertEqual(obj.outcome_type, OutcomeType.PRIMARY)

    def test_iodu_study_outcome_missing_fk(self):
        """ Tests the insertion of a `StudyOutcome` record via the
            `iodu_study_outcome` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodu_study_outcome,
            # This FK is invalid.
            study_id=123,
            protocol_outcome_id=123,
            outcome_type=OutcomeType.PRIMARY,
        )

    def test_iodu_study_outcome_duplicate(self):
        """ Tests the IODU insertion of duplicate `StudyOutcome` records to
            ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        protocol_outcome_id, _ = create_protocol_outcome(dal=self.dal)
        protocol_outcome_02_id, _ = create_protocol_outcome(
            dal=self.dal,
            measure="new_measure",
        )

        # IODU a new `StudyOutcome` record.
        obj_id = self.dal.iodu_study_outcome(
            study_id=study_id,
            protocol_outcome_id=protocol_outcome_id,
            outcome_type=OutcomeType.PRIMARY,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODU the same `StudyOutcome` record as before.
        obj_id = self.dal.iodu_study_outcome(
            study_id=study_id,
            protocol_outcome_id=protocol_outcome_id,
            outcome_type=OutcomeType.PRIMARY,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODU the same `StudyOutcome` record with a changed `outcome_type`
        # field which should trigger an update on the existing record.
        obj_id = self.dal.iodu_study_outcome(
            study_id=study_id,
            protocol_outcome_id=protocol_outcome_id,
            outcome_type=OutcomeType.SECONDARY,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyOutcome, obj_id)  # type: StudyOutcome

        self.assertEqual(obj.outcome_type, OutcomeType.SECONDARY)

        # IODU a new `StudyOutcome` record.
        obj_id = self.dal.iodu_study_outcome(
            study_id=study_id,
            protocol_outcome_id=protocol_outcome_02_id,
            outcome_type=OutcomeType.POST_HOC,
        )

        # The PK should be `4` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 4)

        # IODU the same `StudyOutcome` record as before.
        obj_id = self.dal.iodu_study_outcome(
            study_id=study_id,
            protocol_outcome_id=protocol_outcome_02_id,
            outcome_type=OutcomeType.POST_HOC,
        )

        # The PK should still be `4` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 4)

    def test_delete_study_outcome(self):
        """ Tests the deletion of a `StudyOutcome` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        protocol_outcome_id, _ = create_protocol_outcome(dal=self.dal)

        # IODU a new `StudyOutcome` record.
        obj_id = self.dal.iodu_study_outcome(
            study_id=study_id,
            protocol_outcome_id=protocol_outcome_id,
            outcome_type=OutcomeType.PRIMARY,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyOutcome, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyOutcome, obj_id)  # type: StudyOutcome

        self.assertIsNone(obj)
