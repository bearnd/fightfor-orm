# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Intervention` class as well as the
`iodi_intervention` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import Intervention
from fform.orm_ct import InterventionType

from tests.bases import DalCtTestBase


class DalCtInterventionTest(DalCtTestBase):

    def test_iodi_get_intervention(self):
        """Tests the insertion of a `Intervention` record via the
        `iodi_intervention` method of the `DalClinicalTrials` class and its
        retrieval via the `get` method."""

        # IODI a new `Intervention` record.
        obj_id = self.dal.iodi_intervention(
            intervention_type=InterventionType.DEVICE,
            name="Whole body hyperthermia unit",
            description=None,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Intervention, obj_id)  # type: Intervention

        # Assert that the different fields of the record match.
        self.assertEqual(obj.intervention_id, 1)
        self.assertEqual(obj.intervention_type, InterventionType.DEVICE)
        self.assertEqual(obj.name, "Whole body hyperthermia unit")
        self.assertEqual(obj.description, None)

    def test_iodi_intervention_duplicate(self):
        """Tests the IODI insertion of duplicate `Intervention` records to
        ensure deduplication functions as intended."""

        # IODI a new `Intervention` record.
        obj_id = self.dal.iodi_intervention(
            intervention_type=InterventionType.DEVICE,
            name="Whole body hyperthermia unit",
            description=None,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `Intervention` record.
        obj_id = self.dal.iodi_intervention(
            intervention_type=InterventionType.DEVICE,
            name="Whole body hyperthermia unit",
            description=None,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `Intervention` record.
        obj_id = self.dal.iodi_intervention(
            intervention_type=InterventionType.DRUG,
            name="Topical ocular hypotensive eye drops.",
            description="Topical ocular hypotensive eye drops.",
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `Intervention` record as before only with different
        # casing.
        obj_id = self.dal.iodi_intervention(
            intervention_type=InterventionType.DRUG,
            name="tOpical Ocular hypotensivE eYe drops.",
            description="Topical OCULAR hypotensive eye drops.",
        )

        self.assertEqual(obj_id, 3)

    def test_delete_intervention(self):
        """Tests the deletion of a `Intervention` record via the `delete`
        method of the `DalClinicalTrials` class."""

        # IODI a new `Intervention` record.
        obj_id = self.dal.iodi_intervention(
            intervention_type=InterventionType.DEVICE,
            name="Whole body hyperthermia unit",
            description=None,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Intervention, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Intervention, obj_id)  # type: Intervention

        self.assertIsNone(obj)
