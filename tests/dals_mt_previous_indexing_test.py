# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `PreviousIndexing` class as well as the
`iodi_previous_indexing` method of the `DalMesh` class.
"""

from fform.orm_mt import PreviousIndexing

from tests.bases import DalMtTestBase


class DalMtPreviousIndexingTest(DalMtTestBase):
    """ Defines unit-tests for the `PreviousIndexing` class as well as the
        `iodi_previous_indexing` method of the `DalMesh` class.
    """

    def test_iodi_get_previous_indexing(self):
        """ Tests the IODI insertion of a `PreviousIndexing` record via the
            `iodi_previous_indexing` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # IODI a new `PreviousIndexing` record.
        obj_id = self.dal.iodi_previous_indexing(
            previous_indexing="Abortion, Criminal (1966-1970)",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(PreviousIndexing, obj_id)  # type: PreviousIndexing

        # Assert that the different fields of the record match.
        self.assertEqual(obj.previous_indexing_id, 1)
        self.assertEqual(
            obj.previous_indexing,
            "Abortion, Criminal (1966-1970)",
        )

    def test_iodi_previous_indexing_duplicate(self):
        """ Tests the IODI insertion of duplicate `PreviousIndexing` records to
            ensure deduplication functions as intended.
        """

        # IODI a new `PreviousIndexing` record.
        obj_id = self.dal.iodi_previous_indexing(
            previous_indexing="Abortion, Criminal (1966-1970)",
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `PreviousIndexing` record.
        obj_id = self.dal.iodi_previous_indexing(
            previous_indexing="Abortion, Criminal (1966-1970)",
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `PreviousIndexing` record.
        obj_id = self.dal.iodi_previous_indexing(
            previous_indexing="Abortion, Legal (1966-1970)",
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `PreviousIndexing` record as before only lowercased.
        obj_id = self.dal.iodi_previous_indexing(
            previous_indexing="abortion, legal (1966-1970)",
        )

        self.assertEqual(obj_id, 3)

    def test_delete_tree_number(self):
        """ Tests the deletion of a `PreviousIndexing` record via the `delete`
            method of the `DalMesh` class.
        """

        # IODI a new `PreviousIndexing` record.
        obj_id = self.dal.iodi_previous_indexing(
            previous_indexing="Abortion, Criminal (1966-1970)",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(PreviousIndexing, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(PreviousIndexing, obj_id)  # type: PreviousIndexing

        self.assertIsNone(obj)
