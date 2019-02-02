# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `SupplementalConcept` class as well as the
`iodu_supplemental_concept` method of the `DalMesh` class.
"""

from fform.orm_mt import SupplementalConcept

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_supplemental
from tests.assets.items_mt import create_concept


class DalMtSupplementalConceptTest(DalMtTestBase):

    def test_iodu_get_supplemental_concept(self):
        """ Tests the IODU insertion of a `SupplementalConcept` record via the
            `iodu_supplemental_concept` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create a `Supplemental` record as a fixture.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `SupplementalConcept` record.
        obj_id = self.dal.iodu_supplemental_concept(
            supplemental_id=supplemental_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            SupplementalConcept,
            obj_id,
        )  # type: SupplementalConcept

        # Assert that the different fields of the record match.
        self.assertEqual(obj.supplemental_concept_id, obj_id)
        self.assertEqual(obj.supplemental_id, supplemental_id)
        self.assertEqual(obj.concept_id, concept_id)
        self.assertEqual(obj.is_preferred, True)

    def test_iodu_supplemental_concept(self):
        """ Tests the IODU insertion of duplicate `SupplementalConcept` records
            to ensure deduplication functions as intended.
        """

        # Create a `Supplemental` record as a fixture.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)
        # Create a second `Concept` record as a fixture.
        concept_02_id, _ = create_concept(dal=self.dal, ui="UI2", name="Name2")

        # IODU a new `SupplementalConcept` record.
        obj_id = self.dal.iodu_supplemental_concept(
            supplemental_id=supplemental_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `SupplementalConcept` record.
        obj_id = self.dal.iodu_supplemental_concept(
            supplemental_id=supplemental_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `SupplementalConcept` record with a changed
        # `is_preferred` field which should trigger an update on the existing
        # record.
        obj_id = self.dal.iodu_supplemental_concept(
            supplemental_id=supplemental_id,
            concept_id=concept_id,
            is_preferred=False,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            SupplementalConcept,
            obj_id,
        )  # type: SupplementalConcept

        self.assertEqual(obj.is_preferred, False)

        # IODU a new `SupplementalConcept` record.
        obj_id = self.dal.iodu_supplemental_concept(
            supplemental_id=supplemental_id,
            concept_id=concept_02_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `SupplementalConcept` record as before.
        obj_id = self.dal.iodu_supplemental_concept(
            supplemental_id=supplemental_id,
            concept_id=concept_02_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_supplemental_concept(self):
        """ Tests the deletion of a `SupplementalConcept` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create a `Supplemental` record as a fixture.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `SupplementalConcept` record.
        obj_id = self.dal.iodu_supplemental_concept(
            supplemental_id=supplemental_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(SupplementalConcept, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            SupplementalConcept,
            obj_id,
        )  # type: SupplementalConcept

        self.assertIsNone(obj)

    def test_update_supplemental_concept(self):
        """ Tests the update of a `SupplementalConcept` record via the `update`
            method of the `DalMesh` class.
        """

        # Create a `Supplemental` record as a fixture.
        supplemental_id, _ = create_supplemental(dal=self.dal)
        # Create a `Concept` record as a fixture.
        concept_id, _ = create_concept(dal=self.dal)

        # IODU a new `SupplementalConcept` record.
        obj_id = self.dal.iodu_supplemental_concept(
            supplemental_id=supplemental_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        # Retrieve the new record.
        obj_original = self.dal.get(
            SupplementalConcept,
            obj_id,
        )  # type: SupplementalConcept

        # Assert that the different fields of the record match.
        self.assertEqual(obj_original.supplemental_concept_id, obj_id)
        self.assertEqual(obj_original.supplemental_id, supplemental_id)
        self.assertEqual(obj_original.concept_id, concept_id)
        self.assertEqual(obj_original.is_preferred, True)

        # Update the record.
        self.dal.update_attr_value(
            SupplementalConcept,
            obj_id,
            "is_preferred",
            False,
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(
            SupplementalConcept,
            obj_id,
        )  # type: SupplementalConcept

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.supplemental_concept_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.is_preferred, False)
