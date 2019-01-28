# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `DescriptorAllowableQualifier` class as
well as the `iodu_descriptor_allowable_qualifier` method of the `DalMesh` class.
"""

from fform.orm_mt import DescriptorAllowableQualifier

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_descriptor
from tests.assets.items_mt import create_qualifier


class DalMtDescriptorAllowableQualifierTest(DalMtTestBase):

    def test_iodu_get_descriptor_allowable_qualifier(self):
        """ Tests the IODU insertion of a `DescriptorAllowableQualifier` record
            via the `iodu_descriptor_allowable_qualifier` method of the
            `DalMesh` class and its retrieval via the `get` method.
        """

        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)

        # IODU a new `DescriptorAllowableQualifier` record.
        obj_id = self.dal.iodu_descriptor_allowable_qualifier(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            abbreviation="abbreviation",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            DescriptorAllowableQualifier,
            obj_id,
        )  # type: DescriptorAllowableQualifier

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_allowable_qualifier_id, obj_id)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.qualifier_id, qualifier_id)
        self.assertEqual(obj.abbreviation, "abbreviation")

    def test_iodu_descriptor_allowable_qualifier(self):
        """ Tests the IODU insertion of duplicate `DescriptorAllowableQualifier`
            records to ensure deduplication functions as intended.
        """

        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a second `Qualifier` record as a fixture.
        qualifier_02_id, _ = create_qualifier(
            dal=self.dal,
            ui="UI2",
            name="Name2",
        )

        # IODU a new `DescriptorAllowableQualifier` record.
        obj_id = self.dal.iodu_descriptor_allowable_qualifier(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            abbreviation="abbreviation",
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `DescriptorAllowableQualifier` record.
        obj_id = self.dal.iodu_descriptor_allowable_qualifier(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            abbreviation="abbreviation",
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `DescriptorAllowableQualifier` record with a changed
        # `abbreviation` field which should trigger an update on the existing
        #  record.
        obj_id = self.dal.iodu_descriptor_allowable_qualifier(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            abbreviation="NewAbbreviation",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            DescriptorAllowableQualifier,
            obj_id,
        )  # type: DescriptorAllowableQualifier

        self.assertEqual(obj.abbreviation, "NewAbbreviation")

        # IODU a new `DescriptorAllowableQualifier` record.
        obj_id = self.dal.iodu_descriptor_allowable_qualifier(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_02_id,
            abbreviation="NewAbbreviation",
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `DescriptorAllowableQualifier` record as before.
        obj_id = self.dal.iodu_descriptor_allowable_qualifier(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_02_id,
            abbreviation="NewAbbreviation",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_descriptor_allowable_qualifier(self):
        """ Tests the deletion of a `DescriptorAllowableQualifier` record via
            the `delete` method of the `DalMesh` class.
        """

        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)

        # IODU a new `DescriptorAllowableQualifier` record.
        obj_id = self.dal.iodu_descriptor_allowable_qualifier(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            abbreviation="abbreviation",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(DescriptorAllowableQualifier, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            DescriptorAllowableQualifier,
            obj_id,
        )  # type: DescriptorAllowableQualifier

        self.assertIsNone(obj)

    def test_update_descriptor_allowable_qualifier(self):
        """ Tests the update of a `DescriptorAllowableQualifier` record via the
            `update` method of the `DalMesh` class.
        """

        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)

        # IODU a new `DescriptorAllowableQualifier` record.
        obj_id = self.dal.iodu_descriptor_allowable_qualifier(
            descriptor_id=descriptor_id,
            qualifier_id=qualifier_id,
            abbreviation="abbreviation",
        )

        # Retrieve the new record.
        obj_original = self.dal.get(
            DescriptorAllowableQualifier,
            obj_id,
        )  # type: DescriptorAllowableQualifier

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.descriptor_allowable_qualifier_id, obj_id)
        self.assertEqual(obj_original.descriptor_id, descriptor_id)
        self.assertEqual(obj_original.qualifier_id, qualifier_id)
        self.assertEqual(obj_original.abbreviation, "abbreviation")

        # Update the record.
        self.dal.update_attr_value(
            DescriptorAllowableQualifier,
            obj_id,
            "abbreviation",
            "NewAbbreviation",
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(
            DescriptorAllowableQualifier,
            obj_id,
        )  # type: DescriptorAllowableQualifier

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.descriptor_allowable_qualifier_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.abbreviation, "NewAbbreviation")
