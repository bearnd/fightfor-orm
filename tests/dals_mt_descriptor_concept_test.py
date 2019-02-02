# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `DescriptorConcept` class as well as the
`iodu_descriptor_concept` method of the `DalMesh` class.
"""

from fform.orm_mt import DescriptorConcept

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_descriptor
from tests.assets.items_mt import create_concept


class DalMtDescriptorConceptTest(DalMtTestBase):

    def test_iodu_get_descriptor_concept(self):
        """ Tests the IODU insertion of a `DescriptorConcept` record via the
            `iodu_descriptor_concept` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `DescriptorConcept` record.
        obj_id = self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(DescriptorConcept, obj_id)  # type: DescriptorConcept

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_concept_id, obj_id)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.concept_id, concept_id)
        self.assertEqual(obj.is_preferred, True)

    def test_iodu_descriptor_concept(self):
        """ Tests the IODU insertion of duplicate `DescriptorConcept` records to
            ensure deduplication functions as intended.
        """

        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)
        # Create a second `Concept` record as a fixture.
        concept_02_id, _ = create_concept(dal=self.dal, ui="UI2", name="Name2")

        # IODU a new `DescriptorConcept` record.
        obj_id = self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `DescriptorConcept` record.
        obj_id = self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `DescriptorConcept` record with a changed `is_preferred`
        # field which should trigger an update on the existing record.
        obj_id = self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_id,
            is_preferred=False,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(DescriptorConcept, obj_id)  # type: DescriptorConcept

        self.assertEqual(obj.is_preferred, False)

        # IODU a new `DescriptorConcept` record.
        obj_id = self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_02_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `DescriptorConcept` record as before.
        obj_id = self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_02_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_descriptor_concept(self):
        """ Tests the deletion of a `DescriptorConcept` record via the `delete`
            method of the `DalMesh` class.
        """

        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `DescriptorConcept` record.
        obj_id = self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(DescriptorConcept, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(DescriptorConcept, obj_id)  # type: DescriptorConcept

        self.assertIsNone(obj)

    def test_update_descriptor_concept(self):
        """ Tests the update of a `DescriptorConcept` record via the `update`
            method of the `DalMesh` class.
        """

        # Create a `Descriptor` record as a fixture.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `DescriptorConcept` record.
        obj_id = self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        # Retrieve the new record.
        obj_original = self.dal.get(
            DescriptorConcept,
            obj_id,
        )  # type: DescriptorConcept

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.descriptor_concept_id, obj_id)
        self.assertEqual(obj_original.descriptor_id, descriptor_id)
        self.assertEqual(obj_original.concept_id, concept_id)
        self.assertEqual(obj_original.is_preferred, True)

        # Update the record.
        self.dal.update_attr_value(
            DescriptorConcept,
            obj_id,
            "is_preferred",
            False,
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(
            DescriptorConcept,
            obj_id,
        )  # type: DescriptorConcept

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.descriptor_concept_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.is_preferred, False)
