# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `ResponsibleParty` class as well as the
`insert_responsible_party` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import ResponsibleParty
from fform.orm_ct import ResponsiblePartyType

from tests.bases import DalCtTestBase


class DalCtResponsiblePartyTest(DalCtTestBase):

    def test_insert_get_responsible_party(self):
        """ Tests the insertion of a `ResponsibleParty` record via the
            `insert_responsible_party` method of the `DalClinicalTrials` class
            and its retrieval via the `get` method.
        """

        # Insert a new `ResponsibleParty` record.
        obj_id = self.dal.insert_responsible_party(
            name_title="name_title",
            organization="organization",
            responsible_party_type=ResponsiblePartyType.PRINCIPAL,
            investigator_affiliation="investigator_affiliation",
            investigator_full_name="investigator_full_name",
            investigator_title="investigator_title",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(ResponsibleParty, obj_id)  # type: ResponsibleParty

        # Assert that the different fields of the record match.
        self.assertEqual(obj.responsible_party_id, 1)
        self.assertEqual(obj.name_title, "name_title")
        self.assertEqual(obj.organization, "organization")
        self.assertEqual(
            obj.responsible_party_type,
            ResponsiblePartyType.PRINCIPAL,
        )
        self.assertEqual(
            obj.investigator_affiliation,
            "investigator_affiliation",
        )
        self.assertEqual(obj.investigator_full_name, "investigator_full_name")
        self.assertEqual(obj.investigator_title, "investigator_title")

    def test_insert_responsible_party_duplicate(self):
        """ Tests the insertion of duplicate `ResponsibleParty` records to
            ensure that no deduplication checks occurs.
        """

        # Inserts a new `ResponsibleParty` record.
        obj_id = self.dal.insert_responsible_party(
            name_title="name_title",
            organization="organization",
            responsible_party_type=ResponsiblePartyType.PRINCIPAL,
            investigator_affiliation="investigator_affiliation",
            investigator_full_name="investigator_full_name",
            investigator_title="investigator_title",
        )

        self.assertEqual(obj_id, 1)

        # Inserts an identical `ResponsibleParty` record.
        obj_id = self.dal.insert_responsible_party(
            name_title="name_title",
            organization="organization",
            responsible_party_type=ResponsiblePartyType.PRINCIPAL,
            investigator_affiliation="investigator_affiliation",
            investigator_full_name="investigator_full_name",
            investigator_title="investigator_title",
        )

        self.assertEqual(obj_id, 2)

        # Inserts a new `ResponsibleParty` record.
        obj_id = self.dal.insert_responsible_party(
            name_title="new_name_title",
            organization="new_organization",
            responsible_party_type=ResponsiblePartyType.SPONSOR,
            investigator_affiliation="new_investigator_affiliation",
            investigator_full_name="new_investigator_full_name",
            investigator_title="new_investigator_title",
        )

        self.assertEqual(obj_id, 3)

        # Inserts the same `ResponsibleParty` record as before.
        obj_id = self.dal.insert_responsible_party(
            name_title="new_name_title",
            organization="new_organization",
            responsible_party_type=ResponsiblePartyType.SPONSOR,
            investigator_affiliation="new_investigator_affiliation",
            investigator_full_name="new_investigator_full_name",
            investigator_title="new_investigator_title",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_responsible_party(self):
        """ Tests the deletion of a `ResponsibleParty` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Inserts a new `ResponsibleParty` record.
        obj_id = self.dal.insert_responsible_party(
            name_title="name_title",
            organization="organization",
            responsible_party_type=ResponsiblePartyType.PRINCIPAL,
            investigator_affiliation="investigator_affiliation",
            investigator_full_name="investigator_full_name",
            investigator_title="investigator_title",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(ResponsibleParty, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(ResponsibleParty, obj_id)  # type: ResponsibleParty

        self.assertIsNone(obj)
