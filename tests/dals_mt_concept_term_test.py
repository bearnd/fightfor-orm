# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `ConceptTerm` class as well as the
`iodu_concept_term` method of the `DalMesh` class.
"""

from fform.orm_mt import ConceptTerm
from fform.orm_mt import LexicalTagType

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_term
from tests.assets.items_mt import create_concept


class DalMtConceptTermTest(DalMtTestBase):

    def test_iodu_get_concept_term(self):
        """ Tests the IODU insertion of a `ConceptTerm` record via the
            `iodu_concept_term` method of the `DalMesh` class and its retrieval
            via the `get` method.
        """

        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)
        # Create a `Term` record as a fixture.
        term_id, _ = create_term(dal=self.dal)

        # IODU a new `ConceptTerm` record.
        obj_id = self.dal.iodu_concept_term(
            concept_id=concept_id,
            term_id=term_id,
            is_concept_preferred_term=True,
            is_permuted_term=False,
            lexical_tag=LexicalTagType.ABB,
            is_record_preferred_term=True,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(ConceptTerm, obj_id)  # type: ConceptTerm

        # Assert that the different fields of the record match.
        self.assertEqual(obj.concept_term_id, obj_id)
        self.assertEqual(obj.concept_id, concept_id)
        self.assertEqual(obj.term_id, term_id)
        self.assertEqual(obj.is_concept_preferred_term, True)
        self.assertEqual(obj.is_permuted_term, False)
        self.assertEqual(obj.lexical_tag, LexicalTagType.ABB)
        self.assertEqual(obj.is_record_preferred_term, True)

    def test_iodu_concept_term_duplicate(self):
        """ Tests the IODU insertion of duplicate `ConceptTerm` records to
            ensure deduplication functions as intended.
        """

        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)
        # Create a `Term` record as a fixture.
        term_id, _ = create_term(dal=self.dal)
        # Create a second`Term` record as a fixture.
        term_02_id, _ = create_term(dal=self.dal, ui="UI2", name="Name2")

        # IODU a new `ConceptTerm` record.
        obj_id = self.dal.iodu_concept_term(
            concept_id=concept_id,
            term_id=term_id,
            is_concept_preferred_term=True,
            is_permuted_term=False,
            lexical_tag=LexicalTagType.ABB,
            is_record_preferred_term=True,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `ConceptTerm` record.
        obj_id = self.dal.iodu_concept_term(
            concept_id=concept_id,
            term_id=term_id,
            is_concept_preferred_term=True,
            is_permuted_term=False,
            lexical_tag=LexicalTagType.ABB,
            is_record_preferred_term=True,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `ConceptTerm` record with a changed `lexical_tag` field
        # which should trigger an update on the existing record.
        obj_id = self.dal.iodu_concept_term(
            concept_id=concept_id,
            term_id=term_id,
            is_concept_preferred_term=True,
            is_permuted_term=False,
            lexical_tag=LexicalTagType.ABX,
            is_record_preferred_term=True,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(ConceptTerm, obj_id)  # type: ConceptTerm

        self.assertEqual(obj.lexical_tag, LexicalTagType.ABX)

        # IODU a new `Concept` record.
        obj_id = self.dal.iodu_concept_term(
            concept_id=concept_id,
            term_id=term_02_id,
            is_concept_preferred_term=True,
            is_permuted_term=False,
            lexical_tag=LexicalTagType.ABX,
            is_record_preferred_term=True,
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Concept` record as before.
        obj_id = self.dal.iodu_concept_term(
            concept_id=concept_id,
            term_id=term_02_id,
            is_concept_preferred_term=True,
            is_permuted_term=False,
            lexical_tag=LexicalTagType.ABX,
            is_record_preferred_term=True,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_concept_term(self):
        """ Tests the deletion of a `ConceptTerm` record via the `delete` method
            of the `DalMesh` class.
        """

        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)
        # Create a `Term` record as a fixture.
        term_id, _ = create_term(dal=self.dal)

        # IODU a new `ConceptTerm` record.
        obj_id = self.dal.iodu_concept_term(
            concept_id=concept_id,
            term_id=term_id,
            is_concept_preferred_term=True,
            is_permuted_term=False,
            lexical_tag=LexicalTagType.ABB,
            is_record_preferred_term=True,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(ConceptTerm, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(ConceptTerm, obj_id)  # type: ConceptTerm

        self.assertIsNone(obj)

    def test_update_concept_term(self):
        """ Tests the update of a `ConceptTerm` record via the `update` method
            of the `DalMesh` class.
        """

        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)
        # Create a `Term` record as a fixture.
        term_id, _ = create_term(dal=self.dal)

        # IODU a new `ConceptTerm` record.
        obj_id = self.dal.iodu_concept_term(
            concept_id=concept_id,
            term_id=term_id,
            is_concept_preferred_term=True,
            is_permuted_term=False,
            lexical_tag=LexicalTagType.ABB,
            is_record_preferred_term=True,
        )

        # Retrieve the new record.
        obj_original = self.dal.get(ConceptTerm, obj_id)  # type: ConceptTerm

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.concept_term_id, obj_id)
        self.assertEqual(obj_original.concept_id, concept_id)
        self.assertEqual(obj_original.term_id, term_id)
        self.assertEqual(obj_original.is_concept_preferred_term, True)
        self.assertEqual(obj_original.is_permuted_term, False)
        self.assertEqual(obj_original.lexical_tag, LexicalTagType.ABB)
        self.assertEqual(obj_original.is_record_preferred_term, True)

        # Update the record.
        self.dal.update_attr_value(
            ConceptTerm,
            obj_id,
            "lexical_tag",
            LexicalTagType.ACR,
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(ConceptTerm, obj_id)  # type: ConceptTerm

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.concept_term_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.lexical_tag, LexicalTagType.ACR)
