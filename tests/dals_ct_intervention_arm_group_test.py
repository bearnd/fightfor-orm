# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `InterventionArmGroup` class as well as
the `iodi_intervention_arm_group` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import InterventionArmGroup

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_arm_group
from tests.assets.items_ct import create_intervention


class DalCtInterventionArmGroupTest(DalCtTestBase):

    def test_iodi_get_intervention_alias(self):
        """ Tests the insertion of a `InterventionArmGroup` record via the
            `iodi_intervention_arm_group` method of the `DalClinicalTrials`
            class and its retrieval via the `get` method.
        """

        # Create an `ArmGroup` record as a fixture.
        arm_group_id, _ = create_arm_group(dal=self.dal)
        # Create an `Intervention` record as a fixture.
        intervention_id, _ = create_intervention(dal=self.dal)

        # IODI a new `InterventionArmGroup` record.
        obj_id = self.dal.iodi_intervention_arm_group(
            arm_group_id=arm_group_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            InterventionArmGroup,
            obj_id,
        )  # type: InterventionArmGroup

        # Assert that the different fields of the record match.
        self.assertEqual(obj.intervention_arm_group_id, 1)
        self.assertEqual(obj.arm_group_id, arm_group_id)
        self.assertEqual(obj.intervention_id, intervention_id)

    def test_iodi_intervention_arm_group_duplicate(self):
        """ Tests the IODI insertion of duplicate `InterventionArmGroup` records
            to ensure deduplication functions as intended.
        """

        # Create two `Alias` records as fixtures.
        arm_group_id, _ = create_arm_group(dal=self.dal)
        arm_group_02_id, _ = create_arm_group(dal=self.dal, label="NewLabel")
        # Create an `Intervention` record as a fixture.
        intervention_id, _ = create_intervention(dal=self.dal)

        # IODI a new `InterventionArmGroup` record.
        obj_id = self.dal.iodi_intervention_arm_group(
            arm_group_id=arm_group_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `InterventionArmGroup` record.
        obj_id = self.dal.iodi_intervention_arm_group(
            arm_group_id=arm_group_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `InterventionArmGroup` record.
        obj_id = self.dal.iodi_intervention_arm_group(
            arm_group_id=arm_group_02_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `InterventionArmGroup` record as before.
        obj_id = self.dal.iodi_intervention_arm_group(
            arm_group_id=arm_group_02_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_intervention_alias(self):
        """ Tests the deletion of a `InterventionArmGroup` record via the
            `delete` method of the `DalClinicalTrials` class.
        """

        # Create an `ArmGroup` record as a fixture.
        arm_group_id, _ = create_arm_group(dal=self.dal)
        # Create an `Intervention` record as a fixture.
        intervention_id, _ = create_intervention(dal=self.dal)

        # IODI a new `InterventionArmGroup` record.
        obj_id = self.dal.iodi_intervention_arm_group(
            arm_group_id=arm_group_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(InterventionArmGroup, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            InterventionArmGroup,
            obj_id,
        )  # type: InterventionArmGroup

        self.assertIsNone(obj)
