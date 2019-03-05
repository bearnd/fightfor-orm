# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `ProtocolOutcome` class as well as the
`insert_protocol_outcome` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import ProtocolOutcome

from tests.bases import DalCtTestBase


class DalCtProtocolOutcomeTest(DalCtTestBase):

    def test_insert_get_protocol_outcome(self):
        """ Tests the insertion of a `ProtocolOutcome` record via the
            `insert_protocol_outcome` method of the `DalClinicalTrials`
            class and its retrieval via the `get` method.
        """

        # IODI a new `ProtocolOutcome` record.
        obj_id = self.dal.insert_protocol_outcome(
            measure="measure",
            time_frame="time_frame",
            description="description",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            ProtocolOutcome,
            obj_id,
        )  # type: ProtocolOutcome

        # Assert that the different fields of the record match.
        self.assertEqual(obj.protocol_outcome_id, 1)
        self.assertEqual(obj.measure, "measure")
        self.assertEqual(obj.time_frame, "time_frame")
        self.assertEqual(obj.description, "description")

    def test_insert_protocol_outcome_duplicate(self):
        """ Tests the insertion of duplicate `ProtocolOutcome` records to
            ensure that no deduplication checks occurs.
        """

        # IODI a new `ProtocolOutcome` record.
        obj_id = self.dal.insert_protocol_outcome(
            measure="measure",
            time_frame="time_frame",
            description="description",
        )
        self.assertEqual(obj_id, 1)

        # IODI an identical `ProtocolOutcome` record.
        obj_id = self.dal.insert_protocol_outcome(
            measure="measure",
            time_frame="time_frame",
            description="description",
        )
        self.assertEqual(obj_id, 2)

        # IODI a new `ProtocolOutcome` record.
        obj_id = self.dal.insert_protocol_outcome(
            measure="new_measure",
            time_frame="new_time_frame",
            description="new_description",
        )
        self.assertEqual(obj_id, 3)

        # IODI the same `ProtocolOutcome` record as before only lowercased.
        obj_id = self.dal.insert_protocol_outcome(
            measure="new_measure",
            time_frame="new_time_frame",
            description="new_description",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_protocol_outcome(self):
        """ Tests the deletion of a `ProtocolOutcome` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # IODI a new `ProtocolOutcome` record.
        obj_id = self.dal.insert_protocol_outcome(
            measure="measure",
            time_frame="time_frame",
            description="description",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(ProtocolOutcome, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            ProtocolOutcome,
            obj_id,
        )  # type: ProtocolOutcome

        self.assertIsNone(obj)
