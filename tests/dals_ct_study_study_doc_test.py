# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyStudyDoc` class as well as the
`iodi_study_study_doc` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyStudyDoc

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_study_doc


class DalCtStudyStudyDocTest(DalCtTestBase):

    def test_iodi_get_study_study_doc(self):
        """ Tests the insertion of a `StudyStudyDoc` record via the
            `iodi_study_study_doc` method of the `DalClinicalTrials` class and its
             retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        study_doc_id, _ = create_study_doc(dal=self.dal)

        # IODI a new `StudyStudyDoc` record.
        obj_id = self.dal.iodi_study_study_doc(
            study_id=study_id,
            study_doc_id=study_doc_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyStudyDoc, obj_id)  # type: StudyStudyDoc

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_study_doc_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.study_doc_id, study_doc_id)

    def test_iodi_study_study_doc_missing_fk(self):
        """ Tests the insertion of a `StudyStudyDoc` record via the
            `iodi_study_study_doc` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_study_study_doc,
            # This FK is invalid.
            study_id=123,
            study_doc_id=123,
        )

    def test_iodi_study_study_doc_duplicate(self):
        """ Tests the IODI insertion of duplicate `StudyStudyDoc` records to
            ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        study_doc_id, _ = create_study_doc(dal=self.dal)
        keyword_02_id, _ = create_study_doc(dal=self.dal, doc_id="new_doc_id")

        # IODI a new `StudyStudyDoc` record.
        obj_id = self.dal.iodi_study_study_doc(
            study_id=study_id,
            study_doc_id=study_doc_id,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `StudyStudyDoc` record as before.
        obj_id = self.dal.iodi_study_study_doc(
            study_id=study_id,
            study_doc_id=study_doc_id,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `StudyStudyDoc` record.
        obj_id = self.dal.iodi_study_study_doc(
            study_id=study_id,
            study_doc_id=keyword_02_id,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyStudyDoc` record as before.
        obj_id = self.dal.iodi_study_study_doc(
            study_id=study_id,
            study_doc_id=keyword_02_id,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_study_doc(self):
        """ Tests the deletion of a `StudyStudyDoc` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        study_doc_id, _ = create_study_doc(dal=self.dal)

        # IODI a new `StudyStudyDoc` record.
        obj_id = self.dal.iodi_study_study_doc(
            study_id=study_id,
            study_doc_id=study_doc_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyStudyDoc, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyStudyDoc, obj_id)  # type: StudyStudyDoc

        self.assertIsNone(obj)
