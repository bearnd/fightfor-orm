# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `LocationInvestigator` class as well as
the `iodi_location_investigator` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import LocationInvestigator

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_facility
from tests.assets.items_ct import create_person
from tests.assets.items_ct import create_contact
from tests.assets.items_ct import create_location
from tests.assets.items_ct import create_investigator


class DalCtLocationInvestigatorTest(DalCtTestBase):

    def test_iodi_get_location_investigator(self):
        """ Tests the insertion of a `LocationInvestigator` record via the
            `iodi_location_investigator` method of the `DalClinicalTrials` class
            and its retrieval via the `get` method.
        """

        # Create a `Location` record as a fixture.
        facility_id, _ = create_facility(dal=self.dal)
        person_id, _ = create_person(dal=self.dal)
        contact_id, _ = create_contact(dal=self.dal, person_id=person_id)
        location_id, _ = create_location(
            dal=self.dal,
            facility_id=facility_id,
            contact_primary_id=contact_id,
            contact_backup_id=contact_id,
        )
        # Create an `Investigator` record as a fixture.
        investigator_id, _ = create_investigator(
            dal=self.dal,
            person_id=person_id,
        )

        # IODI a new `LocationInvestigator` record.
        obj_id = self.dal.iodi_location_investigator(
            location_id=location_id,
            investigator_id=investigator_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            LocationInvestigator,
            obj_id,
        )  # type: LocationInvestigator

        # Assert that the different fields of the record match.
        self.assertEqual(obj.location_investigator_id, 1)
        self.assertEqual(obj.location_id, location_id)
        self.assertEqual(obj.investigator_id, investigator_id)

    def test_iodi_location_investigator_duplicate(self):
        """ Tests the IODI insertion of duplicate `LocationInvestigator` records
            to ensure deduplication functions as intended.
        """

        # Create a `Location` record as a fixture.
        facility_id, _ = create_facility(dal=self.dal)
        person_id, _ = create_person(dal=self.dal)
        contact_id, _ = create_contact(dal=self.dal, person_id=person_id)
        location_id, _ = create_location(
            dal=self.dal,
            facility_id=facility_id,
            contact_primary_id=contact_id,
            contact_backup_id=contact_id,
        )
        # Create an `Investigator` record as a fixture.
        investigator_id, _ = create_investigator(
            dal=self.dal,
            person_id=person_id,
        )
        # Create additional `Investigator` record.
        investigator_02_id, _ = create_investigator(
            dal=self.dal,
            person_id=person_id,
            affiliation="NewAffiliation"
        )

        # IODI a new `LocationInvestigator` record.
        obj_id = self.dal.iodi_location_investigator(
            location_id=location_id,
            investigator_id=investigator_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `Intervention` record.
        obj_id = self.dal.iodi_location_investigator(
            location_id=location_id,
            investigator_id=investigator_id,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `Intervention` record.
        obj_id = self.dal.iodi_location_investigator(
            location_id=location_id,
            investigator_id=investigator_02_id,
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `Intervention` record as before.
        obj_id = self.dal.iodi_location_investigator(
            location_id=location_id,
            investigator_id=investigator_02_id,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_location_investigator(self):
        """ Tests the deletion of a `LocationInvestigator` record via the
            `delete` method of the `DalClinicalTrials` class.
        """

        # Create a `Location` record as a fixture.
        facility_id, _ = create_facility(dal=self.dal)
        person_id, _ = create_person(dal=self.dal)
        contact_id, _ = create_contact(dal=self.dal, person_id=person_id)
        location_id, _ = create_location(
            dal=self.dal,
            facility_id=facility_id,
            contact_primary_id=contact_id,
            contact_backup_id=contact_id,
        )
        # Create an `Investigator` record as a fixture.
        investigator_id, _ = create_investigator(
            dal=self.dal,
            person_id=person_id,
        )

        # IODI a new `LocationInvestigator` record.
        obj_id = self.dal.iodi_location_investigator(
            location_id=location_id,
            investigator_id=investigator_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(LocationInvestigator, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            LocationInvestigator,
            obj_id,
        )  # type: LocationInvestigator

        self.assertIsNone(obj)
