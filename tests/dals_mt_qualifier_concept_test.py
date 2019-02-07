# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `QualifierConcept` class as well as the
`iodu_qualifier_concept` method of the `DalMesh` class.
"""

from fform.orm_mt import QualifierConcept

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_qualifier
from tests.assets.items_mt import create_concept


class DalMtQualifierConceptTest(DalMtTestBase):

    def test_iodu_get_qualifier_concept(self):
        """ Tests the IODU insertion of a `QualifierConcept` record via the
            `iodu_qualifier_concept` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `QualifierConcept` record.
        obj_id = self.dal.iodu_qualifier_concept(
            qualifier_id=qualifier_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(QualifierConcept, obj_id)  # type: QualifierConcept

        # Assert that the different fields of the record match.
        self.assertEqual(obj.qualifier_concept_id, obj_id)
        self.assertEqual(obj.qualifier_id, qualifier_id)
        self.assertEqual(obj.concept_id, concept_id)
        self.assertEqual(obj.is_preferred, True)

    def test_iodu_qualifier_concept(self):
        """ Tests the IODU insertion of duplicate `QualifierConcept` records to
            ensure deduplication functions as intended.
        """

        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)
        # Create a second `Concept` record as a fixture.
        concept_02_id, _ = create_concept(dal=self.dal, ui="UI2", name="Name2")

        # IODU a new `QualifierConcept` record.
        obj_id = self.dal.iodu_qualifier_concept(
            qualifier_id=qualifier_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `QualifierConcept` record.
        obj_id = self.dal.iodu_qualifier_concept(
            qualifier_id=qualifier_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `QualifierConcept` record with a changed `is_preferred`
        # field which should trigger an update on the existing record.
        obj_id = self.dal.iodu_qualifier_concept(
            qualifier_id=qualifier_id,
            concept_id=concept_id,
            is_preferred=False,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(QualifierConcept, obj_id)  # type: QualifierConcept

        self.assertEqual(obj.is_preferred, False)

        # IODU a new `QualifierConcept` record.
        obj_id = self.dal.iodu_qualifier_concept(
            qualifier_id=qualifier_id,
            concept_id=concept_02_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `QualifierConcept` record as before.
        obj_id = self.dal.iodu_qualifier_concept(
            qualifier_id=qualifier_id,
            concept_id=concept_02_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_qualifier_concept(self):
        """ Tests the deletion of a `QualifierConcept` record via the `delete`
            method of the `DalMesh` class.
        """

        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `QualifierConcept` record.
        obj_id = self.dal.iodu_qualifier_concept(
            qualifier_id=qualifier_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(QualifierConcept, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(QualifierConcept, obj_id)  # type: QualifierConcept

        self.assertIsNone(obj)

    def test_update_qualifier_concept(self):
        """ Tests the update of a `QualifierConcept` record via the `update`
            method of the `DalMesh` class.
        """

        # Create a `Qualifier` record as a fixture.
        qualifier_id, _ = create_qualifier(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `QualifierConcept` record.
        obj_id = self.dal.iodu_qualifier_concept(
            qualifier_id=qualifier_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        # Retrieve the new record.
        obj_original = self.dal.get(
            QualifierConcept,
            obj_id,
        )  # type: QualifierConcept

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.qualifier_concept_id, obj_id)
        self.assertEqual(obj_original.qualifier_id, qualifier_id)
        self.assertEqual(obj_original.concept_id, concept_id)
        self.assertEqual(obj_original.is_preferred, True)

        # Update the record.
        self.dal.update_attr_value(
            QualifierConcept,
            obj_id,
            "is_preferred",
            False,
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(
            QualifierConcept,
            obj_id,
        )  # type: QualifierConcept

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.qualifier_concept_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.is_preferred, False)
