# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyInvestigator` class as well as the
`iodi_study_investigator` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyInvestigator

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_investigator


class DalCtStudyInvestigatorTest(DalCtTestBase):

    def test_iodi_get_study_investigator(self):
        """ Tests the insertion of a `StudyInvestigator` record via the
            `iodi_study_investigator` method of the `DalClinicalTrials` class
            and its retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        investigator_id, _ = create_investigator(dal=self.dal)

        # IODI a new `StudyInvestigator` record.
        obj_id = self.dal.iodi_study_investigator(
            study_id=study_id,
            investigator_id=investigator_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyInvestigator, obj_id)  # type: StudyInvestigator

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_investigator_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.investigator_id, investigator_id)

    def test_iodi_study_investigator_missing_fk(self):
        """ Tests the insertion of a `StudyInvestigator` record via the
            `iodi_study_investigator` method when the required FK is
            non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_study_investigator,
            # This FK is invalid.
            study_id=123,
            investigator_id=123,
        )

    def test_iodi_study_investigator_duplicate(self):
        """ Tests the IODI insertion of duplicate `StudyInvestigator` records
            to ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        investigator_id, _ = create_investigator(dal=self.dal)
        investigator_02_id, _ = create_investigator(
            dal=self.dal,
            affiliation="new_affiliation",
        )

        # IODI a new `StudyInvestigator` record.
        obj_id = self.dal.iodi_study_investigator(
            study_id=study_id,
            investigator_id=investigator_id,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `StudyInvestigator` record as before.
        obj_id = self.dal.iodi_study_investigator(
            study_id=study_id,
            investigator_id=investigator_id,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `StudyInvestigator` record.
        obj_id = self.dal.iodi_study_investigator(
            study_id=study_id,
            investigator_id=investigator_02_id,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyInvestigator` record as before.
        obj_id = self.dal.iodi_study_investigator(
            study_id=study_id,
            investigator_id=investigator_02_id,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_investigator(self):
        """ Tests the deletion of a `StudyInvestigator` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        investigator_id, _ = create_investigator(dal=self.dal)

        # IODI a new `StudyInvestigator` record.
        obj_id = self.dal.iodi_study_investigator(
            study_id=study_id,
            investigator_id=investigator_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyInvestigator, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyInvestigator, obj_id)  # type: StudyInvestigator

        self.assertIsNone(obj)
