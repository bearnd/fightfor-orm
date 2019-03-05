# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyDoc` class as well as the
`insert_study_doc` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import StudyDoc

from tests.bases import DalCtTestBase


class DalCtStudyDocTest(DalCtTestBase):

    def test_insert_get_study_doc(self):
        """ Tests the insertion of a `StudyDoc` record via the
            `insert_study_doc` method of the `DalClinicalTrials` class and
            its retrieval via the `get` method.
        """

        # Insert a new `StudyDoc` record.
        obj_id = self.dal.insert_study_doc(
            doc_id="doc_id",
            doc_type="doc_type",
            doc_url="doc_url",
            doc_comment="doc_comment",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyDoc, obj_id)  # type: StudyDoc

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_doc_id, 1)
        self.assertEqual(obj.doc_id, "doc_id")
        self.assertEqual(obj.doc_type, "doc_type")
        self.assertEqual(obj.doc_url, "doc_url")
        self.assertEqual(obj.doc_comment, "doc_comment")

    def test_insert_study_doc_duplicate(self):
        """ Tests the Inserts insertion of duplicate `StudyDoc` records to
            ensure that no deduplication checks occurs.
        """

        # Inserts a new `StudyDoc` record.
        obj_id = self.dal.insert_study_doc(
            doc_id="doc_id",
            doc_type="doc_type",
            doc_url="doc_url",
            doc_comment="doc_comment",
        )

        self.assertEqual(obj_id, 1)

        # Inserts an identical `StudyDoc` record.
        obj_id = self.dal.insert_study_doc(
            doc_id="doc_id",
            doc_type="doc_type",
            doc_url="doc_url",
            doc_comment="doc_comment",
        )

        self.assertEqual(obj_id, 2)

        # Inserts a new `StudyDoc` record.
        obj_id = self.dal.insert_study_doc(
            doc_id="new_doc_id",
            doc_type="new_doc_type",
            doc_url="new_doc_url",
            doc_comment="new_doc_comment",
        )

        self.assertEqual(obj_id, 3)

        # Inserts the same `StudyDoc` record as before.
        obj_id = self.dal.insert_study_doc(
            doc_id="new_doc_id",
            doc_type="new_doc_type",
            doc_url="new_doc_url",
            doc_comment="new_doc_comment",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_study_doc(self):
        """ Tests the deletion of a `StudyDoc` record via the `delete` method
            of the `DalClinicalTrials` class.
        """

        # Inserts a new `StudyDoc` record.
        obj_id = self.dal.insert_study_doc(
            doc_id="doc_id",
            doc_type="doc_type",
            doc_url="doc_url",
            doc_comment="doc_comment",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyDoc, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyDoc, obj_id)  # type: StudyDoc

        self.assertIsNone(obj)
