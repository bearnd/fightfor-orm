# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudySecondaryId` class as well as the
`insert_study_secondary_id` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import StudySecondaryId

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study


class DalCtStudySecondaryIdTest(DalCtTestBase):

    def test_insert_get_study_secondary_id(self):
        """ Tests the insertion of a `StudySecondaryId` record via the
            `insert_study_secondary_id` method of the `DalClinicalTrials` class
            and its retrieval via the `get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)

        # Insert a new `StudySecondaryId` record.
        obj_id = self.dal.insert_study_secondary_id(
            study_id=study_id,
            secondary_id="secondary_id",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudySecondaryId, obj_id)  # type: StudySecondaryId

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_secondary_id_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.secondary_id, "secondary_id")

    def test_insert_study_secondary_id_duplicate(self):
        """ Tests the Inserts insertion of duplicate `StudySecondaryId` records
            to ensure that no deduplication checks occurs.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)

        # Insert a new `StudySecondaryId` record.
        obj_id = self.dal.insert_study_secondary_id(
            study_id=study_id,
            secondary_id="secondary_id",
        )

        self.assertEqual(obj_id, 1)

        # Inserts an identical `StudySecondaryId` record.
        obj_id = self.dal.insert_study_secondary_id(
            study_id=study_id,
            secondary_id="secondary_id",
        )

        self.assertEqual(obj_id, 2)

        # Inserts a new `StudySecondaryId` record.
        obj_id = self.dal.insert_study_secondary_id(
            study_id=study_id,
            secondary_id="new_secondary_id",
        )

        self.assertEqual(obj_id, 3)

        # Inserts the same `StudySecondaryId` record as before.
        obj_id = self.dal.insert_study_secondary_id(
            study_id=study_id,
            secondary_id="secondary_id",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_study_secondary_id(self):
        """ Tests the deletion of a `StudySecondaryId` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)

        # Inserts a new `StudySecondaryId` record.
        obj_id = self.dal.insert_study_secondary_id(
            study_id=study_id,
            secondary_id="secondary_id",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudySecondaryId, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudySecondaryId, obj_id)  # type: StudySecondaryId

        self.assertIsNone(obj)
