# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Source` class as well as the
`iodi_source` method of the `DalMesh` class.
"""

from fform.orm_mt import Source

from tests.bases import DalMtTestBase


class DalMtSourceTest(DalMtTestBase):
    """ Defines unit-tests for the `Source` class as well as the `iodi_source`
        method of the `DalMesh` class.
    """

    def test_iodi_get_source(self):
        """ Tests the IODI insertion of a `Source` record via the `iodi_source`
            method of the `DalMesh` class and its retrieval via the `get`
            method.
        """

        # IODI a new `Source` record.
        obj_id = self.dal.iodi_source(source="S Afr Med J 50(1):4;1976")

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Source, obj_id)  # type: Source

        # Assert that the different fields of the record match.
        self.assertEqual(obj.source_id, 1)
        self.assertEqual(obj.source, "S Afr Med J 50(1):4;1976")

    def test_iodi_source_duplicate(self):
        """ Tests the IODI insertion of duplicate `Source` records to
            ensure deduplication functions as intended.
        """

        # IODI a new `Source` record.
        obj_id = self.dal.iodi_source(source="S Afr Med J 50(1):4;1976")

        self.assertEqual(obj_id, 1)

        # IODI an identical `Source` record.
        obj_id = self.dal.iodi_source(source="S Afr Med J 50(1):4;1976")

        self.assertEqual(obj_id, 1)

        # IODI a new `Source` record.
        obj_id = self.dal.iodi_source(source="Q J Med 1979;48(191):493")

        self.assertEqual(obj_id, 3)

        # IODI the same `Source` record as before only lowercased.
        obj_id = self.dal.iodi_source(source="Q J Med 1979;48(191):493")

        self.assertEqual(obj_id, 3)

    def test_delete_source(self):
        """ Tests the deletion of a `Source` record via the `delete` method
            of the `DalMesh` class.
        """

        # IODI a new `Source` record.
        obj_id = self.dal.iodi_source(source="S Afr Med J 50(1):4;1976")

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Source, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Source, obj_id)  # type: Source

        self.assertIsNone(obj)
