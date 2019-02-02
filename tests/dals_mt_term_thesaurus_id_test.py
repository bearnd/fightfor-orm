# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `TermThesaurusId` class as well as the
`iodi_term_thesaurus_id` method of the `DalMesh` class.
"""

from fform.orm_mt import TermThesaurusId

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_term, create_thesaurus_id


class DalMtTermThesaurusIdTest(DalMtTestBase):
    """ Defines unit-tests for the `TermThesaurusId` class as well as the
        `iodi_term_thesaurus_id` method of the `DalMesh` class.
    """

    def test_iodi_get_term_thesaurus_id(self):
        """ Tests the IODI insertion of a `TermThesaurusId` record via the
            `iodi_term_thesaurus_id` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create fixture records.
        term_id, term_refr = create_term(dal=self.dal)
        thesaurus_id_id, thesaurus_id_refr = create_thesaurus_id(dal=self.dal)

        # IODI a new `TermThesaurusId` record.
        obj_id = self.dal.iodi_term_thesaurus_id(
            term_id=term_id,
            thesaurus_id_id=thesaurus_id_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(TermThesaurusId, obj_id)  # type: TermThesaurusId

        # Assert that the different fields of the record match.
        self.assertEqual(obj.term_thesaurus_id_id, 1)
        self.assertEqual(obj.term_id, term_id)
        self.assertEqual(obj.thesaurus_id_id, thesaurus_id_id)

    def test_iodi_term_thesaurus_id_duplicate(self):
        """ Tests the IODI insertion of duplicate `TermThesaurusId` records to
            ensure deduplication functions as intended.
        """

        # Create fixture records.
        term_id, term_refr = create_term(dal=self.dal)
        thesaurus_id_id, thesaurus_id_refr = create_thesaurus_id(dal=self.dal)
        thesaurus_id_02_id, thesaurus_id_02_refr = create_thesaurus_id(
            dal=self.dal,
            thesaurus_id="SomeNewThesaurusId"
        )

        # IODI a new `TermThesaurusId` record.
        obj_id = self.dal.iodi_term_thesaurus_id(
            term_id=term_id,
            thesaurus_id_id=thesaurus_id_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `TermThesaurusId` record.
        obj_id = self.dal.iodi_term_thesaurus_id(
            term_id=term_id,
            thesaurus_id_id=thesaurus_id_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `TermThesaurusId` record.
        obj_id = self.dal.iodi_term_thesaurus_id(
            term_id=term_id,
            thesaurus_id_id=thesaurus_id_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_term_thesaurus_id(self):
        """ Tests the deletion of a `TermThesaurusId` record via the `delete`
            method of the `DalMesh` class.
        """

        # Create fixture records.
        term_id, term_refr = create_term(dal=self.dal)
        thesaurus_id_id, thesaurus_id_refr = create_thesaurus_id(dal=self.dal)

        # IODI a new `TermThesaurusId` record.
        obj_id = self.dal.iodi_term_thesaurus_id(
            term_id=term_id,
            thesaurus_id_id=thesaurus_id_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(TermThesaurusId, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(TermThesaurusId, obj_id)  # type: TermThesaurusId

        self.assertIsNone(obj)
