# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `QualifierTreeNumber` class as well as
the `iodi_qualifier_tree_number` method of the `DalMesh` class.
"""

from fform.orm_mt import QualifierTreeNumber

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_qualifier, create_tree_number


class DalMtTermQualifierTreeNumberTest(DalMtTestBase):
    """ Defines unit-tests for the `QualifierTreeNumber` class as well as the
        `iodi_qualifier_tree_number` method of the `DalMesh` class.
    """

    def test_iodi_get_qualifier_tree_number(self):
        """ Tests the IODI insertion of a `QualifierTreeNumber` record via the
            `iodi_qualifier_tree_number` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create fixture records.
        qualifier_id, qualifier_refr = create_qualifier(dal=self.dal)
        tree_number_id, tree_number_id_refr = create_tree_number(dal=self.dal)

        # IODI a new `QualifierTreeNumber` record.
        obj_id = self.dal.iodi_qualifier_tree_number(
            qualifier_id=qualifier_id,
            tree_number_id=tree_number_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            QualifierTreeNumber,
            obj_id,
        )  # type: QualifierTreeNumber

        # Assert that the different fields of the record match.
        self.assertEqual(obj.qualifier_tree_number_id, 1)
        self.assertEqual(obj.qualifier_id, qualifier_id)
        self.assertEqual(obj.tree_number_id, tree_number_id)

    def test_iodi_qualifier_tree_number_duplicate(self):
        """ Tests the IODI insertion of duplicate `QualifierTreeNumber` records
            to ensure deduplication functions as intended.
        """

        # Create fixture records.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        tree_number_id, _ = create_tree_number(dal=self.dal)
        tree_number_02_id, _ = create_tree_number(
            dal=self.dal,
            tree_number="B13.869.106",
        )

        # IODI a new `QualifierTreeNumber` record.
        obj_id = self.dal.iodi_qualifier_tree_number(
            qualifier_id=qualifier_id,
            tree_number_id=tree_number_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `QualifierTreeNumber` record.
        obj_id = self.dal.iodi_qualifier_tree_number(
            qualifier_id=qualifier_id,
            tree_number_id=tree_number_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `QualifierTreeNumber` record.
        obj_id = self.dal.iodi_qualifier_tree_number(
            qualifier_id=qualifier_id,
            tree_number_id=tree_number_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_qualifier_tree_number(self):
        """ Tests the deletion of a `QualifierTreeNumber` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        qualifier_id, qualifier_refr = create_qualifier(dal=self.dal)
        tree_number_id, tree_number_id_refr = create_tree_number(dal=self.dal)

        # IODI a new `QualifierTreeNumber` record.
        obj_id = self.dal.iodi_qualifier_tree_number(
            qualifier_id=qualifier_id,
            tree_number_id=tree_number_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(QualifierTreeNumber, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            QualifierTreeNumber,
            obj_id,
        )  # type: QualifierTreeNumber

        self.assertIsNone(obj)
