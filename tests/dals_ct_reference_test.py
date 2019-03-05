# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Reference` class as well as the
`iodu_reference` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import Reference

from tests.bases import DalCtTestBase


class DalCtReferenceTest(DalCtTestBase):

    def test_iodu_get_reference(self):
        """ Tests the IODU insertion of a `Reference` record via the
            `iodu_reference` method of the `DalClinicalTrials` class and its
            retrieval via the `get` method.
        """

        # IODU a new `Reference` record.
        obj_id = self.dal.iodu_reference(citation="citation", pmid=1)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Reference, obj_id)  # type: Reference

        # Assert that the different fields of the record match.
        self.assertEqual(obj.reference_id, obj_id)
        self.assertEqual(obj.citation, "citation")
        self.assertEqual(obj.pmid, 1)

    def test_iodu_reference_duplicate(self):
        """ Tests the IODU insertion of duplicate `Reference` records to ensure
            deduplication functions as intended.
        """

        # IODU a new `Reference` record.
        obj_id = self.dal.iodu_reference(citation="citation", pmid=1)

        self.assertEqual(obj_id, 1)

        # IODU the same `Descriptor` record.
        obj_id = self.dal.iodu_reference(citation="citation", pmid=1)

        self.assertEqual(obj_id, 1)

        # IODU the same `Descriptor` record with a changed `citation` field
        # which should trigger an update on the existing record.
        obj_id = self.dal.iodu_reference(citation="new_citation", pmid=1)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Reference, obj_id)  # type: Reference

        self.assertEqual(obj.citation, "new_citation")

        # IODU a new `Descriptor` record.
        obj_id = self.dal.iodu_reference(citation="citation", pmid=2)

        self.assertEqual(obj_id, 4)

        # IODU the same `Descriptor` record as before.
        obj_id = self.dal.iodu_reference(citation="citation", pmid=2)

        self.assertEqual(obj_id, 4)

    def test_delete_reference(self):
        """ Tests the deletion of a `Reference` record via the `delete` method
            of the `DalClinicalTrials` class.
        """

        # IODU a new `Reference` record.
        obj_id = self.dal.iodu_reference(citation="citation", pmid=1)

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Reference, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Reference, obj_id)  # type: Reference

        self.assertIsNone(obj)
