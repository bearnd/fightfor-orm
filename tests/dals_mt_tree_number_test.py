# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `TreeNumber` class as well as the
`iodi_tree_number` method of the `DalMesh` class.
"""

from fform.orm_mt import TreeNumber

from tests.bases import DalMtTestBase


class DalMtTreeNumberTest(DalMtTestBase):
    """ Defines unit-tests for the `TreeNumber` class as well as the
        `iodi_tree_number` method of the `DalMesh` class.
    """

    def test_iodi_get_tree_number(self):
        """ Tests the IODI insertion of a `TreeNumber` record via the
            `iodi_tree_number` method of the `DalMesh` class and its retrieval
            via the `get` method.
        """

        # IODI a new `TreeNumber` record.
        obj_id = self.dal.iodi_tree_number(tree_number="A13.869.106")

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(TreeNumber, obj_id)  # type: TreeNumber

        # Assert that the different fields of the record match.
        self.assertEqual(obj.tree_number_id, 1)
        self.assertEqual(obj.tree_number, "A13.869.106")

    def test_iodi_tree_number_duplicate(self):
        """ Tests the IODI insertion of duplicate `TreeNumber` records to ensure
            deduplication functions as intended.
        """

        # IODI a new `TreeNumber` record.
        obj_id = self.dal.iodi_tree_number(tree_number="A13.869.106")

        self.assertEqual(obj_id, 1)

        # IODI an identical `TreeNumber` record.
        obj_id = self.dal.iodi_tree_number(tree_number="A13.869.106")

        self.assertEqual(obj_id, 1)

        # IODI a new `TreeNumber` record.
        obj_id = self.dal.iodi_tree_number(tree_number="D27.505.696.875.131")

        self.assertEqual(obj_id, 3)

        # IODI the same `TreeNumber` record as before only lowercased.
        obj_id = self.dal.iodi_tree_number(tree_number="d27.505.696.875.131")

        self.assertEqual(obj_id, 3)

    def test_delete_tree_number(self):
        """ Tests the deletion of a `TreeNumber` record via the `delete` method
            of the `DalMesh` class.
        """

        # IODI a new `TreeNumber` record.
        obj_id = self.dal.iodi_tree_number(tree_number="A13.869.106")

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(TreeNumber, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(TreeNumber, obj_id)  # type: TreeNumber

        self.assertIsNone(obj)
