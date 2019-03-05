# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `InterventionAlias` class as well as
the `iodi_intervention_alias` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import InterventionAlias

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_alias
from tests.assets.items_ct import create_intervention


class DalCtInterventionAliasTest(DalCtTestBase):

    def test_iodi_get_intervention_alias(self):
        """ Tests the insertion of a `InterventionAlias` record via the
            `iodi_intervention_alias` method of the `DalClinicalTrials` class
            and its retrieval via the `get` method.
        """

        # Create an `Alias` record as a fixture.
        alias_id, _ = create_alias(dal=self.dal)
        # Create an `Intervention` record as a fixture.
        intervention_id, _ = create_intervention(dal=self.dal)

        # IODI a new `InterventionAlias` record.
        obj_id = self.dal.iodi_intervention_alias(
            alias_id=alias_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            InterventionAlias,
            obj_id,
        )  # type: InterventionAlias

        # Assert that the different fields of the record match.
        self.assertEqual(obj.intervention_alias_id, 1)
        self.assertEqual(obj.alias_id, alias_id)
        self.assertEqual(obj.intervention_id, intervention_id)

    def test_iodi_intervention_alias_duplicate(self):
        """ Tests the IODI insertion of duplicate `InterventionAlias` records
            to ensure deduplication functions as intended.
        """

        # Create two `Alias` records as fixtures.
        alias_id, _ = create_alias(dal=self.dal)
        alias_02_id, _ = create_alias(dal=self.dal, alias="NewAlias")
        # Create an `Intervention` record as a fixture.
        intervention_id, _ = create_intervention(dal=self.dal)

        # IODI a new `InterventionAlias` record.
        obj_id = self.dal.iodi_intervention_alias(
            alias_id=alias_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `Intervention` record.
        obj_id = self.dal.iodi_intervention_alias(
            alias_id=alias_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `Intervention` record.
        obj_id = self.dal.iodi_intervention_alias(
            alias_id=alias_02_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `Intervention` record as before.
        obj_id = self.dal.iodi_intervention_alias(
            alias_id=alias_02_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_intervention_alias(self):
        """ Tests the deletion of a `InterventionAlias` record via the
            `delete` method of the `DalClinicalTrials` class.
        """

        # Create an `Alias` record as a fixture.
        alias_id, _ = create_alias(dal=self.dal)
        # Create an `Intervention` record as a fixture.
        intervention_id, _ = create_intervention(dal=self.dal)

        # IODI a new `InterventionAlias` record.
        obj_id = self.dal.iodi_intervention_alias(
            alias_id=alias_id,
            intervention_id=intervention_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(InterventionAlias, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            InterventionAlias,
            obj_id,
        )  # type: InterventionAlias

        self.assertIsNone(obj)
