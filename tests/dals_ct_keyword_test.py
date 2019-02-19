# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Keyword` class as well as the
`iodi_keyword` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import Keyword

from tests.bases import DalCtTestBase


class DalCtKeywordTest(DalCtTestBase):

    def test_iodi_get_keyword(self):
        """Tests the insertion of a `Keyword` record via the `iodi_keyword`
        method of the `DalClinicalTrials` class and its retrieval via the `get`
        method."""

        # IODI a new `Keyword` record.
        obj_id = self.dal.iodi_keyword(keyword="Rheumatoid Diseases")

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Keyword, obj_id)  # type: Keyword

        # Assert that the different fields of the record match.
        self.assertEqual(obj.keyword_id, 1)
        # Assert that lowercasing kicked in.
        self.assertEqual(obj.keyword, "rheumatoid diseases")

    def test_iodi_keyword_duplicate(self):
        """Tests the IODI insertion of duplicate `Keyword` records to ensure
        deduplication functions as intended."""

        # IODI a new `Keyword` record.
        obj_id = self.dal.iodi_keyword(keyword="Rheumatoid Diseases")

        self.assertEqual(obj_id, 1)

        # IODI an identical `Keyword` record.
        obj_id = self.dal.iodi_keyword(keyword="Rheumatoid Diseases")

        self.assertEqual(obj_id, 1)

        # IODI a new `Keyword` record.
        obj_id = self.dal.iodi_keyword(keyword="Ocular Melanoma")

        self.assertEqual(obj_id, 3)

        # IODI the same `Keyword` record as before only lowercased.
        obj_id = self.dal.iodi_keyword(keyword="ocular melanoma")

        self.assertEqual(obj_id, 3)

    def test_delete_keyword(self):
        """Tests the deletion of a `Keyword` record via the `delete` method of
        the `DalClinicalTrials` class."""

        # IODI a new `Keyword` record.
        obj_id = self.dal.iodi_keyword(keyword="Rheumatoid Diseases")

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Keyword, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Keyword, obj_id)  # type: Keyword

        self.assertIsNone(obj)
