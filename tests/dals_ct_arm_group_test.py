# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `ArmGroup` class as well as the
`insert_arm_group` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import ArmGroup

from tests.bases import DalCtTestBase


class DalCtArmGroupTest(DalCtTestBase):

    def test_insert_get_arm_group(self):
        """ Tests the insertion of a `ArmGroup` record via the
            `insert_arm_group` method of the `DalClinicalTrials` class and its
            retrieval via the `get` method.
        """

        # IODI a new `ArmGroup` record.
        obj_id = self.dal.insert_arm_group(
            label="label",
            arm_group_type="arm_group_type",
            description="description",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            ArmGroup,
            obj_id,
        )  # type: ArmGroup

        # Assert that the different fields of the record match.
        self.assertEqual(obj.arm_group_id, 1)
        self.assertEqual(obj.label, "label")
        self.assertEqual(obj.arm_group_type, "arm_group_type")
        self.assertEqual(obj.description, "description")

    def test_insert_arm_group_duplicate(self):
        """ Tests the insertion of duplicate `ArmGroup` records to
            ensure that no deduplication checks occurs.
        """

        # IODI a new `ArmGroup` record.
        obj_id = self.dal.insert_arm_group(
            label="label",
            arm_group_type="arm_group_type",
            description="description",
        )
        self.assertEqual(obj_id, 1)

        # IODI an identical `ArmGroup` record.
        obj_id = self.dal.insert_arm_group(
            label="label",
            arm_group_type="arm_group_type",
            description="description",
        )
        self.assertEqual(obj_id, 2)

        # IODI a new `ArmGroup` record.
        obj_id = self.dal.insert_arm_group(
            label="new_label",
            arm_group_type="new_arm_group_type",
            description="new_description",
        )
        self.assertEqual(obj_id, 3)

        # IODI the same `ArmGroup` record as before only lowercased.
        obj_id = self.dal.insert_arm_group(
            label="new_label",
            arm_group_type="new_arm_group_type",
            description="new_description",
        )
        self.assertEqual(obj_id, 4)

    def test_delete_arm_group(self):
        """ Tests the deletion of a `ArmGroup` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # IODI a new `ArmGroup` record.
        obj_id = self.dal.insert_arm_group(
            label="label",
            arm_group_type="arm_group_type",
            description="description",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(ArmGroup, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            ArmGroup,
            obj_id,
        )  # type: ArmGroup

        self.assertIsNone(obj)
