# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `EntryCombination` class as well as the
`iodu_entry_combination` method of the `DalMesh` class.
"""

from fform.orm_mt import EntryCombination
from fform.orm_mt import EntryCombinationType

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_qualifier
from tests.assets.items_mt import create_descriptor


class DalMtEntryCombinationTest(DalMtTestBase):

    def test_iodu_get_entry_combination(self):
        """ Tests the IODU insertion of a `EntryCombination` record via the
            `iodu_entry_combination` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        # IODU a new `EntryCombination` record.
        obj_id = self.dal.iodu_entry_combination(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            combination_type=EntryCombinationType.ECIN,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(EntryCombination, obj_id)  # type: EntryCombination

        # Assert that the different fields of the record match.
        self.assertEqual(obj.entry_combination_id, obj_id)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.qualifier_id, qualifier_id)
        self.assertEqual(obj.combination_type, EntryCombinationType.ECIN)

    def test_iodu_entry_combination(self):
        """ Tests the IODU insertion of duplicate `EntryCombination` records to
            ensure deduplication functions as intended.
        """

        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a second `Descriptor` record as a fixture.
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="Name2",
        )

        # IODU a new `EntryCombination` record.
        obj_id = self.dal.iodu_entry_combination(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            combination_type=EntryCombinationType.ECIN,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `EntryCombination` record.
        obj_id = self.dal.iodu_entry_combination(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            combination_type=EntryCombinationType.ECIN,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `EntryCombination` record with a changed
        # `combination_type` field which should trigger an update on the
        # existing record.
        obj_id = self.dal.iodu_entry_combination(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            combination_type=EntryCombinationType.ECOUT,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(EntryCombination, obj_id)  # type: EntryCombination

        self.assertEqual(obj.combination_type, EntryCombinationType.ECOUT)

        # IODU a new `EntryCombination` record.
        obj_id = self.dal.iodu_entry_combination(
            descriptor_id=descriptor_02_id,
            qualifier_id=qualifier_id,
            combination_type=EntryCombinationType.ECIN,
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `EntryCombination` record as before.
        obj_id = self.dal.iodu_entry_combination(
            descriptor_id=descriptor_02_id,
            qualifier_id=qualifier_id,
            combination_type=EntryCombinationType.ECIN,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_entry_combination(self):
        """ Tests the deletion of a `EntryCombination` record via the `delete`
            method of the `DalMesh` class.
        """

        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        # IODU a new `EntryCombination` record.
        obj_id = self.dal.iodu_entry_combination(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            combination_type=EntryCombinationType.ECIN,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(EntryCombination, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(EntryCombination, obj_id)  # type: EntryCombination

        self.assertIsNone(obj)

    def test_update_entry_combination(self):
        """ Tests the update of a `EntryCombination` record via the `update`
            method of the `DalMesh` class.
        """

        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        # IODU a new `EntryCombination` record.
        obj_id = self.dal.iodu_entry_combination(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            combination_type=EntryCombinationType.ECIN,
        )

        # Retrieve the new record.
        obj_original = self.dal.get(
            EntryCombination,
            obj_id,
        )  # type: EntryCombination

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.entry_combination_id, obj_id)
        self.assertEqual(obj_original.descriptor_id, descriptor_id)
        self.assertEqual(obj_original.qualifier_id, qualifier_id)
        self.assertEqual(
            obj_original.combination_type,
            EntryCombinationType.ECIN,
        )

        # Update the record.
        self.dal.update_attr_value(
            EntryCombination,
            obj_id,
            "combination_type",
            EntryCombinationType.ECOUT,
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(
            EntryCombination,
            obj_id,
        )  # type: EntryCombination

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.entry_combination_id, 1)
        # Assert that attribute changed.
        self.assertEqual(
            obj_updated.combination_type,
            EntryCombinationType.ECOUT,
        )
