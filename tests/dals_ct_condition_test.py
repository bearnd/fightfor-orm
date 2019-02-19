# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Condition` class as well as the
`iodi_condition` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import Condition

from tests.bases import DalCtTestBase


class DalCtConditionTest(DalCtTestBase):

    def test_iodi_get_condition(self):
        """Tests the insertion of a `Condition` record via the `iodi_condition`
        method of the `DalClinicalTrials` class and its retrieval via the `get`
        method."""

        # IODI a new `Condition` record.
        obj_id = self.dal.iodi_condition(condition="Cardiovascular Diseases")

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Condition, obj_id)  # type: Condition

        # Assert that the different fields of the record match.
        self.assertEqual(obj.condition_id, 1)
        # Assert that lowercasing kicked in.
        self.assertEqual(obj.condition, "cardiovascular diseases")

    def test_iodi_condition_duplicate(self):
        """Tests the IODI insertion of duplicate `Condition` records to ensure
        deduplication functions as intended."""

        # IODI a new `Condition` record.
        obj_id = self.dal.iodi_condition(condition="Cardiovascular Diseases")

        self.assertEqual(obj_id, 1)

        # IODI an identical `Condition` record.
        obj_id = self.dal.iodi_condition(condition="Cardiovascular Diseases")

        self.assertEqual(obj_id, 1)

        # IODI a new `Condition` record.
        obj_id = self.dal.iodi_condition(condition="Cataract")

        self.assertEqual(obj_id, 3)

        # IODI the same `Condition` record as before only lowercased.
        obj_id = self.dal.iodi_condition(condition="cataract")

        self.assertEqual(obj_id, 3)

    def test_delete_condition(self):
        """Tests the deletion of a `Condition` record via the `delete` method of
        the `DalClinicalTrials` class."""

        # IODI a new `Condition` record.
        obj_id = self.dal.iodi_condition(condition="Cardiovascular Diseases")

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Condition, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Condition, obj_id)  # type: Condition

        self.assertIsNone(obj)

    def test_update_condition(self):
        """Tests the update of a `Condition` record via the `update` method of
        the `DalClinicalTrials` class."""

        # IODI a new `Condition` record.
        obj_id = self.dal.iodi_condition(condition="Cardiovascular Diseases")

        # Retrieve the new record.
        obj_original = self.dal.get(Condition, obj_id)  # type: Condition

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.condition_id, 1)
        # Assert that lowercasing kicked in.
        self.assertEqual(obj_original.condition, "cardiovascular diseases")

        # Update the record.
        self.dal.update_attr_value(Condition, obj_id, "condition", "test")

        # Retrieve the updated record.
        obj_updated = self.dal.get(Condition, obj_id)  # type: Condition

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.condition_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.condition, "test")
        # Assert that the MD5 changes.
        self.assertNotEqual(obj_original.md5, obj_updated.md5)
