# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyIntervention` class as well as the
`iodi_study_intervention` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyIntervention

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_intervention


class DalCtStudyInterventionTest(DalCtTestBase):

    def test_iodi_get_study_intervention(self):
        """ Tests the insertion of a `StudyIntervention` record via the
            `iodi_study_intervention` method of the `DalClinicalTrials` class
            and its retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        intervention_id, _ = create_intervention(dal=self.dal)

        # IODI a new `StudyIntervention` record.
        obj_id = self.dal.iodi_study_intervention(
            study_id=study_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyIntervention, obj_id)  # type: StudyIntervention

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_intervention_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.intervention_id, intervention_id)

    def test_iodi_study_intervention_missing_fk(self):
        """ Tests the insertion of a `StudyIntervention` record via the
            `iodi_study_intervention` method when the required FK is
            non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_study_intervention,
            # This FK is invalid.
            study_id=123,
            intervention_id=123,
        )

    def test_iodi_study_intervention_duplicate(self):
        """ Tests the IODI insertion of duplicate `StudyIntervention` records
            to ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        intervention_id, _ = create_intervention(dal=self.dal)
        intervention_02_id, _ = create_intervention(
            dal=self.dal,
            name="new_name",
        )

        # IODI a new `StudyIntervention` record.
        obj_id = self.dal.iodi_study_intervention(
            study_id=study_id,
            intervention_id=intervention_id,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `StudyIntervention` record as before.
        obj_id = self.dal.iodi_study_intervention(
            study_id=study_id,
            intervention_id=intervention_id,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `StudyIntervention` record.
        obj_id = self.dal.iodi_study_intervention(
            study_id=study_id,
            intervention_id=intervention_02_id,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyIntervention` record as before.
        obj_id = self.dal.iodi_study_intervention(
            study_id=study_id,
            intervention_id=intervention_02_id,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_intervention(self):
        """ Tests the deletion of a `StudyIntervention` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        intervention_id, _ = create_intervention(dal=self.dal)

        # IODI a new `StudyIntervention` record.
        obj_id = self.dal.iodi_study_intervention(
            study_id=study_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyIntervention, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyIntervention, obj_id)  # type: StudyIntervention

        self.assertIsNone(obj)
