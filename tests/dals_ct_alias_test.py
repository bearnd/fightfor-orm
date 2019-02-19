# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Alias` class as well as the `iodi_alias`
method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import Alias

from tests.bases import DalCtTestBase


class DalCtAliasTest(DalCtTestBase):

    def test_iodi_get_alias(self):
        """ Tests the insertion of a `Alias` record via the `iodi_alias` method
            of the `DalClinicalTrials` class and its retrieval via the `get`
            method.
        """

        # IODI a new `Alias` record.
        obj_id = self.dal.iodi_alias(alias="Alias")

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Alias, obj_id)  # type: Alias

        # Assert that the different fields of the record match.
        self.assertEqual(obj.alias_id, 1)
        # Assert that lowercasing kicked in.
        self.assertEqual(obj.alias, "alias")

    def test_iodi_alias_duplicate(self):
        """ Tests the IODI insertion of duplicate `Alias` records to ensure
            deduplication functions as intended.
        """

        # IODI a new `Alias` record.
        obj_id = self.dal.iodi_alias(alias="Alias")

        self.assertEqual(obj_id, 1)

        # IODI an identical `Alias` record.
        obj_id = self.dal.iodi_alias(alias="Alias")

        self.assertEqual(obj_id, 1)

        # IODI a new `Alias` record.
        obj_id = self.dal.iodi_alias(alias="NewAlias")

        self.assertEqual(obj_id, 3)

        # IODI the same `Alias` record as before only lowercased.
        obj_id = self.dal.iodi_alias(alias="NewAlias")

        self.assertEqual(obj_id, 3)

    def test_delete_alias(self):
        """ Tests the deletion of a `Alias` record via the `delete` method of
            the `DalClinicalTrials` class.
        """

        # IODI a new `Alias` record.
        obj_id = self.dal.iodi_alias(alias="Alias")

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Alias, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Alias, obj_id)  # type: Alias

        self.assertIsNone(obj)
