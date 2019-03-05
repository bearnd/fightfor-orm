# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `OversightInfo` class as well as the
`insert_oversight_info` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import OversightInfo

from tests.bases import DalCtTestBase


class DalCtOversightInfoTest(DalCtTestBase):

    def test_insert_get_oversight_info(self):
        """ Tests the insertion of a `OversightInfo` record via the
            `insert_oversight_info` method of the `DalClinicalTrials` class and
            its retrieval via the `get` method.
        """

        # IODI a new `OversightInfo` record.
        obj_id = self.dal.insert_oversight_info(
            has_dmc=True,
            is_fda_regulated_drug=True,
            is_fda_regulated_device=True,
            is_unapproved_device=True,
            is_ppsd=True,
            is_us_export=True,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(OversightInfo, obj_id)  # type: OversightInfo

        # Assert that the different fields of the record match.
        self.assertEqual(obj.oversight_info_id, 1)
        self.assertEqual(obj.has_dmc, True)
        self.assertEqual(obj.is_fda_regulated_drug, True)
        self.assertEqual(obj.is_fda_regulated_device, True)
        self.assertEqual(obj.is_unapproved_device, True)
        self.assertEqual(obj.is_ppsd, True)
        self.assertEqual(obj.is_us_export, True)

    def test_insert_oversight_info_duplicate(self):
        """ Tests the insertion of duplicate `OversightInfo` records to ensure
            that no deduplication checks occurs.
        """

        # IODI a new `OversightInfo` record.
        obj_id = self.dal.insert_oversight_info(
            has_dmc=True,
            is_fda_regulated_drug=True,
            is_fda_regulated_device=True,
            is_unapproved_device=True,
            is_ppsd=True,
            is_us_export=True,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `OversightInfo` record.
        obj_id = self.dal.insert_oversight_info(
            has_dmc=True,
            is_fda_regulated_drug=True,
            is_fda_regulated_device=True,
            is_unapproved_device=True,
            is_ppsd=True,
            is_us_export=True,
        )

        self.assertEqual(obj_id, 2)

        # IODI a new `OversightInfo` record.
        obj_id = self.dal.insert_oversight_info(
            has_dmc=False,
            is_fda_regulated_drug=True,
            is_fda_regulated_device=True,
            is_unapproved_device=True,
            is_ppsd=True,
            is_us_export=True,
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `OversightInfo` record as before only lowercased.
        obj_id = self.dal.insert_oversight_info(
            has_dmc=False,
            is_fda_regulated_drug=True,
            is_fda_regulated_device=True,
            is_unapproved_device=True,
            is_ppsd=True,
            is_us_export=True,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_oversight_info(self):
        """ Tests the deletion of a `OversightInfo` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # IODI a new `OversightInfo` record.
        obj_id = self.dal.insert_oversight_info(
            has_dmc=True,
            is_fda_regulated_drug=True,
            is_fda_regulated_device=True,
            is_unapproved_device=True,
            is_ppsd=True,
            is_us_export=True,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(OversightInfo, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(OversightInfo, obj_id)  # type: OversightInfo

        self.assertIsNone(obj)
