# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `SupplementalSource` class as well as the
`iodi_supplemental_source` method of the `DalMesh` class.
"""

from fform.orm_mt import SupplementalSource

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_source
from tests.assets.items_mt import create_supplemental


class DalMtTermSupplementalSourceTest(DalMtTestBase):
    """ Defines unit-tests for the `SupplementalSource` class as well as the
        `iodi_supplemental_source` method of the `DalMesh` class.
    """

    def test_iodi_get_supplemental_source(self):
        """ Tests the IODI insertion of a `SupplementalSource` record via the
            `iodi_supplemental_source` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        source_id, _ = create_source(dal=self.dal)

        # IODI a new `SupplementalSource` record.
        obj_id = self.dal.iodi_supplemental_source(
            supplemental_id=supplemental_id,
            source_id=source_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            SupplementalSource,
            obj_id,
        )  # type: SupplementalSource

        # Assert that the different fields of the record match.
        self.assertEqual(obj.supplemental_source_id, 1)
        self.assertEqual(obj.supplemental_id, supplemental_id)
        self.assertEqual(obj.source_id, source_id)

    def test_iodi_supplemental_source_duplicate(self):
        """ Tests the IODI insertion of duplicate `SupplementalSource` records
            to ensure deduplication functions as intended.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        source_id, _ = create_source(dal=self.dal)
        source_02_id, _ = create_source(
            dal=self.dal,
            source="Vopr Neirokhir 6:48;1977",
        )

        # IODI a new `SupplementalSource` record.
        obj_id = self.dal.iodi_supplemental_source(
            supplemental_id=supplemental_id,
            source_id=source_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `SupplementalSource` record.
        obj_id = self.dal.iodi_supplemental_source(
            supplemental_id=supplemental_id,
            source_id=source_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `SupplementalSource` record.
        obj_id = self.dal.iodi_supplemental_source(
            supplemental_id=supplemental_id,
            source_id=source_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_supplemental_source(self):
        """ Tests the deletion of a `SupplementalSource` record via the `delete`
            method of the `DalMesh` class.
        """

        # Create fixture records.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        source_id, _ = create_source(dal=self.dal)

        # IODI a new `SupplementalSource` record.
        obj_id = self.dal.iodi_supplemental_source(
            supplemental_id=supplemental_id,
            source_id=source_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(SupplementalSource, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            SupplementalSource,
            obj_id,
        )  # type: SupplementalSource

        self.assertIsNone(obj)
