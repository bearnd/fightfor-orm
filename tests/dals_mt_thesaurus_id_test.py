# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `ThesaurusId` class as well as the
`iodi_thesaurus_id` method of the `DalMesh` class.
"""

from fform.orm_mt import ThesaurusId

from tests.bases import DalMtTestBase


class DalMtThesaurusIdTest(DalMtTestBase):
    """ Defines unit-tests for the `ThesaurusId` class as well as the
        `iodi_thesaurus_id` method of the `DalMesh` class.
    """

    def test_iodi_get_thesaurus_id(self):
        """ Tests the IODI insertion of a `ThesaurusId` record via the
            `iodi_thesaurus_id` method of the `DalMesh` class and its retrieval
            via the `get` method.
        """

        # IODI a new `ThesaurusId` record.
        obj_id = self.dal.iodi_thesaurus_id(thesaurus_id="POPLINE (1978)")

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(ThesaurusId, obj_id)  # type: ThesaurusId

        # Assert that the different fields of the record match.
        self.assertEqual(obj.thesaurus_id_id, 1)
        self.assertEqual(obj.thesaurus_id, "POPLINE (1978)")

    def test_iodi_thesaurus_id_duplicate(self):
        """ Tests the IODI insertion of duplicate `ThesaurusId` records to
            ensure deduplication functions as intended.
        """

        # IODI a new `ThesaurusId` record.
        obj_id = self.dal.iodi_thesaurus_id(thesaurus_id="POPLINE (1978)")

        self.assertEqual(obj_id, 1)

        # IODI an identical `ThesaurusId` record.
        obj_id = self.dal.iodi_thesaurus_id(thesaurus_id="POPLINE (1978)")

        self.assertEqual(obj_id, 1)

        # IODI a new `ThesaurusId` record.
        obj_id = self.dal.iodi_thesaurus_id(thesaurus_id="NLM (1993)")

        self.assertEqual(obj_id, 3)

        # IODI the same `ThesaurusId` record as before only lowercased.
        obj_id = self.dal.iodi_thesaurus_id(thesaurus_id="nlm (1993)")

        self.assertEqual(obj_id, 3)

    def test_delete_tree_number(self):
        """ Tests the deletion of a `ThesaurusId` record via the `delete` method
            of the `DalMesh` class.
        """

        # IODI a new `ThesaurusId` record.
        obj_id = self.dal.iodi_thesaurus_id(thesaurus_id="POPLINE (1978)")

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(ThesaurusId, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(ThesaurusId, obj_id)  # type: ThesaurusId

        self.assertIsNone(obj)
