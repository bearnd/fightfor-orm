# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudySponsor` class as well as the
`iodu_study_sponsor` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudySponsor
from fform.orm_ct import SponsorType

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_sponsor


class DalCtStudySponsorTest(DalCtTestBase):

    def test_iodu_get_study_sponsor(self):
        """ Tests the insertion of a `StudySponsor` record via the
            `iodu_study_sponsor` method of the `DalClinicalTrials` class and its
             retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        sponsor_id, _ = create_sponsor(dal=self.dal)

        # IODU a new `StudySponsor` record.
        obj_id = self.dal.iodu_study_sponsor(
            study_id=study_id,
            sponsor_id=sponsor_id,
            sponsor_type=SponsorType.COLLABORATOR,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudySponsor, obj_id)  # type: StudySponsor

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_sponsor_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.sponsor_id, sponsor_id)
        self.assertEqual(obj.sponsor_type, SponsorType.COLLABORATOR)

    def test_iodu_study_sponsor_missing_fk(self):
        """ Tests the insertion of a `StudySponsor` record via the
            `iodu_study_sponsor` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodu_study_sponsor,
            # This FK is invalid.
            study_id=123,
            sponsor_id=123,
            sponsor_type=SponsorType.COLLABORATOR,
        )

    def test_iodu_study_sponsor_duplicate(self):
        """ Tests the IODU insertion of duplicate `StudySponsor` records to
            ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        sponsor_id, _ = create_sponsor(dal=self.dal)
        sponsor_02_id, _ = create_sponsor(dal=self.dal, agency="new_agency")

        # IODU a new `StudySponsor` record.
        obj_id = self.dal.iodu_study_sponsor(
            study_id=study_id,
            sponsor_id=sponsor_id,
            sponsor_type=SponsorType.COLLABORATOR,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODU the same `StudySponsor` record as before.
        obj_id = self.dal.iodu_study_sponsor(
            study_id=study_id,
            sponsor_id=sponsor_id,
            sponsor_type=SponsorType.COLLABORATOR,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODU the same `StudySponsor` record with a changed `sponsor_type`
        # field which should trigger an update on the existing record.
        obj_id = self.dal.iodu_study_sponsor(
            study_id=study_id,
            sponsor_id=sponsor_id,
            sponsor_type=SponsorType.LEAD,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudySponsor, obj_id)  # type: StudySponsor

        self.assertEqual(obj.sponsor_type, SponsorType.LEAD)

        # IODU a new `StudySponsor` record.
        obj_id = self.dal.iodu_study_sponsor(
            study_id=study_id,
            sponsor_id=sponsor_02_id,
            sponsor_type=SponsorType.COLLABORATOR,
        )

        # The PK should be `4` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 4)

        # IODU the same `StudySponsor` record as before.
        obj_id = self.dal.iodu_study_sponsor(
            study_id=study_id,
            sponsor_id=sponsor_02_id,
            sponsor_type=SponsorType.COLLABORATOR,
        )

        # The PK should still be `4` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 4)

    def test_delete_study_sponsor(self):
        """ Tests the deletion of a `StudySponsor` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        sponsor_id, _ = create_sponsor(dal=self.dal)

        # IODU a new `StudySponsor` record.
        obj_id = self.dal.iodu_study_sponsor(
            study_id=study_id,
            sponsor_id=sponsor_id,
            sponsor_type=SponsorType.COLLABORATOR,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudySponsor, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudySponsor, obj_id)  # type: StudySponsor

        self.assertIsNone(obj)
