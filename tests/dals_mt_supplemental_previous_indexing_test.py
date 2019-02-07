# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `SupplementalPreviousIndexing` class as
well as the `iodi_supplemental_previous_indexing` method of the `DalMesh` class.
"""

from fform.orm_mt import SupplementalPreviousIndexing

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_supplemental
from tests.assets.items_mt import create_previous_indexing


class DalMtTermSupplementalPreviousIndexingTest(DalMtTestBase):
    """ Defines unit-tests for the `SupplementalPreviousIndexing` class as well
        as the `iodi_supplemental_previous_indexing` method of the `DalMesh`
        class.
    """

    def test_iodi_get_supplemental_previous_indexing(self):
        """ Tests the IODI insertion of a `SupplementalPreviousIndexing` record
            via the `iodi_supplemental_previous_indexing` method of the
            `DalMesh` class and its retrieval via the `get` method.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        previous_indexing_id, _ = create_previous_indexing(dal=self.dal)

        # IODI a new `SupplementalPreviousIndexing` record.
        obj_id = self.dal.iodi_supplemental_previous_indexing(
            supplemental_id=supplemental_id,
            previous_indexing_id=previous_indexing_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            SupplementalPreviousIndexing,
            obj_id,
        )  # type: SupplementalPreviousIndexing

        # Assert that the different fields of the record match.
        self.assertEqual(obj.supplemental_previous_indexing_id, 1)
        self.assertEqual(obj.supplemental_id, supplemental_id)
        self.assertEqual(obj.previous_indexing_id, previous_indexing_id)

    def test_iodi_supplemental_previous_indexing_duplicate(self):
        """ Tests the IODI insertion of duplicate `SupplementalPreviousIndexing`
            records to ensure deduplication functions as intended.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        previous_indexing_id, _ = create_previous_indexing(dal=self.dal)
        previous_indexing_02_id, _ = create_previous_indexing(
            dal=self.dal,
            previous_indexing="NewPreviousIndexing"
        )

        # IODI a new `SupplementalPreviousIndexing` record.
        obj_id = self.dal.iodi_supplemental_previous_indexing(
            supplemental_id=supplemental_id,
            previous_indexing_id=previous_indexing_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `SupplementalPreviousIndexing` record.
        obj_id = self.dal.iodi_supplemental_previous_indexing(
            supplemental_id=supplemental_id,
            previous_indexing_id=previous_indexing_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `SupplementalPreviousIndexing` record.
        obj_id = self.dal.iodi_supplemental_previous_indexing(
            supplemental_id=supplemental_id,
            previous_indexing_id=previous_indexing_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_supplemental_previous_indexing(self):
        """ Tests the deletion of a `SupplementalPreviousIndexing` record via
            the `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        previous_indexing_id, _ = create_previous_indexing(dal=self.dal)

        # IODI a new `SupplementalPreviousIndexing` record.
        obj_id = self.dal.iodi_supplemental_previous_indexing(
            supplemental_id=supplemental_id,
            previous_indexing_id=previous_indexing_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(SupplementalPreviousIndexing, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            SupplementalPreviousIndexing,
            obj_id,
        )  # type: SupplementalPreviousIndexing

        self.assertIsNone(obj)
