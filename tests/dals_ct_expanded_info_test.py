# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `ExpandedAccessInfo` class as well as the
`insert_expanded_access_info` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import ExpandedAccessInfo

from tests.bases import DalCtTestBase


class DalCtExpandedInfoTest(DalCtTestBase):

    def test_insert_get_expanded_access_info(self):
        """ Tests the insertion of a `ExpandedAccessInfo` record via the
            `insert_expanded_access_info` method of the `DalClinicalTrials`
            class and its retrieval via the `get` method.
        """

        # IODI a new `ExpandedAccessInfo` record.
        obj_id = self.dal.insert_expanded_access_info(
            expanded_access_type_individual=True,
            expanded_access_type_intermediate=True,
            expanded_access_type_treatment=True,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            ExpandedAccessInfo,
            obj_id,
        )  # type: ExpandedAccessInfo

        # Assert that the different fields of the record match.
        self.assertEqual(obj.expanded_access_info_id, 1)
        self.assertEqual(obj.expanded_access_type_individual, True)
        self.assertEqual(obj.expanded_access_type_intermediate, True)
        self.assertEqual(obj.expanded_access_type_treatment, True)

    def test_insert_expanded_access_info_duplicate(self):
        """ Tests the insertion of duplicate `ExpandedAccessInfo` records to
            ensure that no deduplication checks occurs.
        """

        # IODI a new `ExpandedAccessInfo` record.
        obj_id = self.dal.insert_expanded_access_info(
            expanded_access_type_individual=True,
            expanded_access_type_intermediate=True,
            expanded_access_type_treatment=True,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `ExpandedAccessInfo` record.
        obj_id = self.dal.insert_expanded_access_info(
            expanded_access_type_individual=True,
            expanded_access_type_intermediate=True,
            expanded_access_type_treatment=True,
        )

        self.assertEqual(obj_id, 2)

        # IODI a new `ExpandedAccessInfo` record.
        obj_id = self.dal.insert_expanded_access_info(
            expanded_access_type_individual=True,
            expanded_access_type_intermediate=True,
            expanded_access_type_treatment=True,
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `ExpandedAccessInfo` record as before only lowercased.
        obj_id = self.dal.insert_expanded_access_info(
            expanded_access_type_individual=True,
            expanded_access_type_intermediate=True,
            expanded_access_type_treatment=True,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_expanded_access_info(self):
        """ Tests the deletion of a `ExpandedAccessInfo` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # IODI a new `ExpandedAccessInfo` record.
        obj_id = self.dal.insert_expanded_access_info(
            expanded_access_type_individual=True,
            expanded_access_type_intermediate=True,
            expanded_access_type_treatment=True,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(ExpandedAccessInfo, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            ExpandedAccessInfo,
            obj_id,
        )  # type: ExpandedAccessInfo

        self.assertIsNone(obj)
