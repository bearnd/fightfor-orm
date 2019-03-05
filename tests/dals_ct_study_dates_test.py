# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyDates` class as well as the
`insert_study_dates` method of the `DalClinicalTrials` class.
"""

import datetime

from fform.orm_ct import StudyDates

from tests.bases import DalCtTestBase


class DalCtStudyDatesTest(DalCtTestBase):

    def test_insert_get_study_dates(self):
        """ Tests the insertion of a `StudyDates` record via the
            `insert_study_dates` method of the `DalClinicalTrials` class and
            its retrieval via the `get` method.
        """

        # Insert a new `StudyDates` record.
        obj_id = self.dal.insert_study_dates(
            study_first_submitted=datetime.date(2019, 1, 1),
            study_first_submitted_qc=datetime.date(2019, 1, 2),
            study_first_posted=datetime.date(2019, 1, 3),
            results_first_submitted=datetime.date(2019, 1, 4),
            results_first_submitted_qc=datetime.date(2019, 1, 5),
            results_first_posted=datetime.date(2019, 1, 6),
            disposition_first_submitted=datetime.date(2019, 1, 7),
            disposition_first_submitted_qc=datetime.date(2019, 1, 8),
            disposition_first_posted=datetime.date(2019, 1, 9),
            last_update_submitted=datetime.date(2019, 1, 10),
            last_update_submitted_qc=datetime.date(2019, 1, 11),
            last_update_posted=datetime.date(2019, 1, 12),
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyDates, obj_id)  # type: StudyDates

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_dates_id, 1)
        self.assertEqual(
            obj.study_first_submitted,
            datetime.date(2019, 1, 1),
        )
        self.assertEqual(
            obj.study_first_submitted_qc,
            datetime.date(2019, 1, 2),
        )
        self.assertEqual(
            obj.study_first_posted,
            datetime.date(2019, 1, 3),
        )
        self.assertEqual(
            obj.results_first_submitted,
            datetime.date(2019, 1, 4),
        )
        self.assertEqual(
            obj.results_first_submitted_qc,
            datetime.date(2019, 1, 5),
        )
        self.assertEqual(
            obj.results_first_posted,
            datetime.date(2019, 1, 6),
        )
        self.assertEqual(
            obj.disposition_first_submitted,
            datetime.date(2019, 1, 7),
        )
        self.assertEqual(
            obj.disposition_first_submitted_qc,
            datetime.date(2019, 1, 8),
        )
        self.assertEqual(
            obj.disposition_first_posted,
            datetime.date(2019, 1, 9),
        )
        self.assertEqual(
            obj.last_update_submitted,
            datetime.date(2019, 1, 10),
        )
        self.assertEqual(
            obj.last_update_submitted_qc,
            datetime.date(2019, 1, 11),
        )
        self.assertEqual(
            obj.last_update_posted,
            datetime.date(2019, 1, 12),
        )

    def test_insert_study_dates_duplicate(self):
        """ Tests the Inserts insertion of duplicate `StudyDates` records to
            ensure that no deduplication checks occurs.
        """

        # Inserts a new `StudyDates` record.
        obj_id = self.dal.insert_study_dates(
            study_first_submitted=datetime.date(2019, 1, 1),
            study_first_submitted_qc=datetime.date(2019, 1, 2),
            study_first_posted=datetime.date(2019, 1, 3),
            results_first_submitted=datetime.date(2019, 1, 4),
            results_first_submitted_qc=datetime.date(2019, 1, 5),
            results_first_posted=datetime.date(2019, 1, 6),
            disposition_first_submitted=datetime.date(2019, 1, 7),
            disposition_first_submitted_qc=datetime.date(2019, 1, 8),
            disposition_first_posted=datetime.date(2019, 1, 9),
            last_update_submitted=datetime.date(2019, 1, 10),
            last_update_submitted_qc=datetime.date(2019, 1, 11),
            last_update_posted=datetime.date(2019, 1, 12),
        )

        self.assertEqual(obj_id, 1)

        # Inserts an identical `StudyDates` record.
        obj_id = self.dal.insert_study_dates(
            study_first_submitted=datetime.date(2019, 1, 1),
            study_first_submitted_qc=datetime.date(2019, 1, 2),
            study_first_posted=datetime.date(2019, 1, 3),
            results_first_submitted=datetime.date(2019, 1, 4),
            results_first_submitted_qc=datetime.date(2019, 1, 5),
            results_first_posted=datetime.date(2019, 1, 6),
            disposition_first_submitted=datetime.date(2019, 1, 7),
            disposition_first_submitted_qc=datetime.date(2019, 1, 8),
            disposition_first_posted=datetime.date(2019, 1, 9),
            last_update_submitted=datetime.date(2019, 1, 10),
            last_update_submitted_qc=datetime.date(2019, 1, 11),
            last_update_posted=datetime.date(2019, 1, 12),
        )

        self.assertEqual(obj_id, 2)

        # Inserts a new `StudyDates` record.
        obj_id = self.dal.insert_study_dates(
            study_first_submitted=datetime.date(2019, 2, 1),
            study_first_submitted_qc=datetime.date(2019, 2, 2),
            study_first_posted=datetime.date(2019, 2, 3),
            results_first_submitted=datetime.date(2019, 2, 4),
            results_first_submitted_qc=datetime.date(2019, 2, 5),
            results_first_posted=datetime.date(2019, 2, 6),
            disposition_first_submitted=datetime.date(2019, 2, 7),
            disposition_first_submitted_qc=datetime.date(2019, 2, 8),
            disposition_first_posted=datetime.date(2019, 2, 9),
            last_update_submitted=datetime.date(2019, 2, 10),
            last_update_submitted_qc=datetime.date(2019, 2, 11),
            last_update_posted=datetime.date(2019, 2, 12),
        )

        self.assertEqual(obj_id, 3)

        # Inserts the same `StudyDates` record as before.
        obj_id = self.dal.insert_study_dates(
            study_first_submitted=datetime.date(2019, 2, 1),
            study_first_submitted_qc=datetime.date(2019, 2, 2),
            study_first_posted=datetime.date(2019, 2, 3),
            results_first_submitted=datetime.date(2019, 2, 4),
            results_first_submitted_qc=datetime.date(2019, 2, 5),
            results_first_posted=datetime.date(2019, 2, 6),
            disposition_first_submitted=datetime.date(2019, 2, 7),
            disposition_first_submitted_qc=datetime.date(2019, 2, 8),
            disposition_first_posted=datetime.date(2019, 2, 9),
            last_update_submitted=datetime.date(2019, 2, 10),
            last_update_submitted_qc=datetime.date(2019, 2, 11),
            last_update_posted=datetime.date(2019, 2, 12),
        )

        self.assertEqual(obj_id, 4)

    def test_delete_study_dates(self):
        """ Tests the deletion of a `StudyDates` record via the `delete` method
            of the `DalClinicalTrials` class.
        """

        # Inserts a new `StudyDates` record.
        obj_id = self.dal.insert_study_dates(
            study_first_submitted=datetime.date(2019, 1, 1),
            study_first_submitted_qc=datetime.date(2019, 1, 2),
            study_first_posted=datetime.date(2019, 1, 3),
            results_first_submitted=datetime.date(2019, 1, 4),
            results_first_submitted_qc=datetime.date(2019, 1, 5),
            results_first_posted=datetime.date(2019, 1, 6),
            disposition_first_submitted=datetime.date(2019, 1, 7),
            disposition_first_submitted_qc=datetime.date(2019, 1, 8),
            disposition_first_posted=datetime.date(2019, 1, 9),
            last_update_submitted=datetime.date(2019, 1, 10),
            last_update_submitted_qc=datetime.date(2019, 1, 11),
            last_update_posted=datetime.date(2019, 1, 12),
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyDates, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyDates, obj_id)  # type: StudyDates

        self.assertIsNone(obj)
