# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyReference` class as well as the
`iodu_study_reference` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyReference
from fform.orm_ct import ReferenceType

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_reference


class DalCtStudyReferenceTest(DalCtTestBase):

    def test_iodu_get_study_reference(self):
        """ Tests the insertion of a `StudyReference` record via the
            `iodu_study_reference` method of the `DalClinicalTrials` class and
            its retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        reference_id, _ = create_reference(dal=self.dal)

        # IODU a new `StudyReference` record.
        obj_id = self.dal.iodu_study_reference(
            study_id=study_id,
            reference_id=reference_id,
            reference_type=ReferenceType.STANDARD,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyReference, obj_id)  # type: StudyReference

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_reference_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.reference_id, reference_id)
        self.assertEqual(obj.reference_type, ReferenceType.STANDARD)

    def test_iodu_study_reference_missing_fk(self):
        """ Tests the insertion of a `StudyReference` record via the
            `iodu_study_reference` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodu_study_reference,
            # This FK is invalid.
            study_id=123,
            reference_id=123,
            reference_type=ReferenceType.STANDARD,
        )

    def test_iodu_study_reference_duplicate(self):
        """ Tests the IODU insertion of duplicate `StudyReference` records to
            ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        reference_id, _ = create_reference(dal=self.dal)
        reference_02_id, _ = create_reference(
            dal=self.dal,
            pmid=2,
        )

        # IODU a new `StudyReference` record.
        obj_id = self.dal.iodu_study_reference(
            study_id=study_id,
            reference_id=reference_id,
            reference_type=ReferenceType.STANDARD,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODU the same `StudyReference` record as before.
        obj_id = self.dal.iodu_study_reference(
            study_id=study_id,
            reference_id=reference_id,
            reference_type=ReferenceType.STANDARD,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODU the same `StudyReference` record with a changed `reference_type`
        # field which should trigger an update on the existing record.
        obj_id = self.dal.iodu_study_reference(
            study_id=study_id,
            reference_id=reference_id,
            reference_type=ReferenceType.RESULTS,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyReference, obj_id)  # type: StudyReference

        self.assertEqual(obj.reference_type, ReferenceType.RESULTS)

        # IODU a new `StudyReference` record.
        obj_id = self.dal.iodu_study_reference(
            study_id=study_id,
            reference_id=reference_02_id,
            reference_type=ReferenceType.RESULTS,
        )

        # The PK should be `4` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 4)

        # IODU the same `StudyReference` record as before.
        obj_id = self.dal.iodu_study_reference(
            study_id=study_id,
            reference_id=reference_02_id,
            reference_type=ReferenceType.RESULTS,
        )

        # The PK should still be `4` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 4)

    def test_delete_study_reference(self):
        """ Tests the deletion of a `StudyReference` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        reference_id, _ = create_reference(dal=self.dal)

        # IODU a new `StudyReference` record.
        obj_id = self.dal.iodu_study_reference(
            study_id=study_id,
            reference_id=reference_id,
            reference_type=ReferenceType.STANDARD,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyReference, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyReference, obj_id)  # type: StudyReference

        self.assertIsNone(obj)
