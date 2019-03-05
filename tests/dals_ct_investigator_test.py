# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Investigator` class as well as the
`iodi_investigator` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import Investigator
from fform.orm_ct import RoleType

from tests.bases import DalCtTestBase


class DalCtInvestigatorTest(DalCtTestBase):

    def test_iodi_get_investigator(self):
        """ Tests the insertion of an `Investigator` record via the
            `iodi_investigator` method of the `DalClinicalTrials` class and its
            retrieval via the `get` method.
        """

        # IODI a new `Person` record as a fixture.
        person_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        # IODI a new `Investigator` record.
        obj_id = self.dal.iodi_investigator(
            person_id=person_id,
            role=RoleType.CHAIR,
            affiliation="affiliation",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Investigator, obj_id)  # type: Investigator

        # Assert that the different fields of the record match.
        self.assertEqual(obj.investigator_id, 1)
        self.assertEqual(obj.person_id, person_id)
        self.assertEqual(obj.role, RoleType.CHAIR)
        self.assertEqual(obj.affiliation, "affiliation")

    def test_iodi_investigator_missing_fk(self):
        """ Tests the insertion of an `Investigator` record via the
            `iodi_investigator` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_investigator,
            # This FK is invalid.
            person_id=123,
            role=RoleType.CHAIR,
            affiliation="affiliation",
        )

    def test_iodi_investigator_duplicate(self):
        """ Tests the IODI insertion of duplicate `Investigator` records to
            ensure deduplication functions as intended.
        """

        # IODI a new `Person` record as a fixture.
        person_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        # IODI a new `Investigator` record.
        obj_id = self.dal.iodi_investigator(
            person_id=person_id,
            role=RoleType.CHAIR,
            affiliation="affiliation",
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `Investigator` record as before.
        obj_id = self.dal.iodi_investigator(
            person_id=person_id,
            role=RoleType.CHAIR,
            affiliation="affiliation",
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `Investigator` record.
        obj_id = self.dal.iodi_investigator(
            person_id=person_id,
            role=RoleType.DIRECTOR,
            affiliation="affiliation",
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

    def test_delete_investigator(self):
        """ Tests the deletion of an `Investigator` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # IODI a new `Person` record as a fixture.
        person_id = self.dal.iodi_person(
            name_first="Adamos",
            name_middle=None,
            name_last="Kyriakou",
            degrees="M.Sc., Ph.D."
        )

        # IODI a new `Investigator` record.
        obj_id = self.dal.iodi_investigator(
            person_id=person_id,
            role=RoleType.CHAIR,
            affiliation="affiliation",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Investigator, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Investigator, obj_id)  # type: Investigator

        self.assertIsNone(obj)
