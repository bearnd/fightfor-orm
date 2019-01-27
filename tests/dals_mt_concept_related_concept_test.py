# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `ConceptRelatedConcept` class as well as
the `iodu_concept_related_concept` method of the `DalMesh` class.
"""

from fform.orm_mt import ConceptRelatedConcept
from fform.orm_mt import RelationNameType

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_concept


class DalMtConceptRelatedConceptTest(DalMtTestBase):

    def test_iodu_get_concept_related_concept(self):
        """ Tests the IODU insertion of a `ConceptRelatedConcept` record via the
            `iodu_concept_related_concept` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create two `Concept` records as fixtures.
        concept_01_id, _ = create_concept(dal=self.dal, ui="UI1", name="name1")
        concept_02_id, _ = create_concept(dal=self.dal, ui="UI2", name="name2")

        # IODI a new `ConceptRelatedConcept` record.
        obj_id = self.dal.iodu_concept_related_concept(
            concept_id=concept_01_id,
            related_concept_id=concept_02_id,
            relation_name=RelationNameType.BRD,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            ConceptRelatedConcept,
            obj_id,
        )  # type: ConceptRelatedConcept

        # Assert that the different fields of the record match.
        self.assertEqual(obj.concept_related_concept_id, obj_id)
        self.assertEqual(obj.concept_id, concept_01_id)
        self.assertEqual(obj.related_concept_id, concept_02_id)
        self.assertEqual(obj.relation_name, RelationNameType.BRD)

    def test_iodu_concept_related_concept_duplicate(self):
        """ Tests the IODU insertion of duplicate `ConceptRelatedConcept`
            records to ensure deduplication functions as intended.
        """

        # Create three `Concept` records as fixtures.
        concept_01_id, _ = create_concept(dal=self.dal, ui="UI1", name="name1")
        concept_02_id, _ = create_concept(dal=self.dal, ui="UI2", name="name2")
        concept_03_id, _ = create_concept(dal=self.dal, ui="UI3", name="name3")

        # IODI a new `ConceptRelatedConcept` record.
        obj_id = self.dal.iodu_concept_related_concept(
            concept_id=concept_01_id,
            related_concept_id=concept_02_id,
            relation_name=RelationNameType.BRD,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `ConceptRelatedConcept` record.
        obj_id = self.dal.iodu_concept_related_concept(
            concept_id=concept_01_id,
            related_concept_id=concept_02_id,
            relation_name=RelationNameType.BRD,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `ConceptRelatedConcept` record with a changed
        # `relation_name` field which should trigger an update on the existing
        # record.
        obj_id = self.dal.iodu_concept_related_concept(
            concept_id=concept_01_id,
            related_concept_id=concept_02_id,
            relation_name=RelationNameType.NRW,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            ConceptRelatedConcept,
            obj_id,
        )  # type: ConceptRelatedConcept

        self.assertEqual(obj.relation_name, RelationNameType.NRW)

        # IODU a new `Concept` record.
        obj_id = self.dal.iodu_concept_related_concept(
            concept_id=concept_01_id,
            related_concept_id=concept_03_id,
            relation_name=RelationNameType.REL,
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Concept` record as before.
        obj_id = self.dal.iodu_concept_related_concept(
            concept_id=concept_01_id,
            related_concept_id=concept_03_id,
            relation_name=RelationNameType.REL,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_concept_related_concept(self):
        """ Tests the deletion of a `ConceptRelatedConcept` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create two `Concept` records as fixtures.
        concept_01_id, _ = create_concept(dal=self.dal, ui="UI1", name="name1")
        concept_02_id, _ = create_concept(dal=self.dal, ui="UI2", name="name2")

        # IODI a new `ConceptRelatedConcept` record.
        obj_id = self.dal.iodu_concept_related_concept(
            concept_id=concept_01_id,
            related_concept_id=concept_02_id,
            relation_name=RelationNameType.BRD,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(ConceptRelatedConcept, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            ConceptRelatedConcept,
            obj_id,
        )  # type: ConceptRelatedConcept

        self.assertIsNone(obj)

    def test_update_concept_related_concept(self):
        """ Tests the update of a `ConceptRelatedConcept` record via the
            `update` method of the `DalMesh` class.
        """

        # Create two `Concept` records as fixtures.
        concept_01_id, _ = create_concept(dal=self.dal, ui="UI1", name="name1")
        concept_02_id, _ = create_concept(dal=self.dal, ui="UI2", name="name2")

        # IODI a new `ConceptRelatedConcept` record.
        obj_id = self.dal.iodu_concept_related_concept(
            concept_id=concept_01_id,
            related_concept_id=concept_02_id,
            relation_name=RelationNameType.BRD,
        )

        # Retrieve the new record.
        obj_original = self.dal.get(
            ConceptRelatedConcept,
            obj_id
        )  # type: ConceptRelatedConcept

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.concept_related_concept_id, obj_id)
        self.assertEqual(obj_original.concept_id, concept_01_id)
        self.assertEqual(obj_original.related_concept_id, concept_02_id)
        self.assertEqual(obj_original.relation_name, RelationNameType.BRD)

        # Update the record.
        self.dal.update_attr_value(
            ConceptRelatedConcept,
            obj_id,
            "relation_name",
            RelationNameType.REL,
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(
            ConceptRelatedConcept,
            obj_id
        )  # type: ConceptRelatedConcept

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.concept_related_concept_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.relation_name, RelationNameType.REL)
