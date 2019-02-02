# -*- coding: utf-8 -*-

from fform.orm_ct import Sponsor
from fform.orm_ct import AgencyClassType

from tests.bases import DalCtTestBase


class DalCtSponsorTest(DalCtTestBase):

    def test_iodi_get_sponsor(self):
        """Tests the insertion of a `Sponsor` record via the `iodi_sponsor`
        method of the `DalClinicalTrials` class and its retrieval via the `get`
        method."""

        # IODI a new `Sponsor` record.
        obj_id = self.dal.iodi_sponsor(
            agency="National Center for Research Resources (NCRR)",
            agency_class=AgencyClassType.INDUSTRY
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Sponsor, obj_id)  # type: Sponsor

        # Assert that the different fields of the record match.
        self.assertEqual(obj.sponsor_id, 1)
        self.assertEqual(
            obj.agency,
            "National Center for Research Resources (NCRR)"
        )
        self.assertEqual(obj.agency_class, AgencyClassType.INDUSTRY)

    def test_iodi_sponsor_duplicate(self):
        """Tests the IODI insertion of duplicate `Sponsor` records to ensure
        deduplication functions as intended."""

        # IODI a `Sponsor` record.
        obj_id = self.dal.iodi_sponsor(
            agency="Johns Hopkins Bloomberg School of Public Health",
            agency_class=AgencyClassType.OTHER
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `Sponsor` record as before.
        obj_id = self.dal.iodi_sponsor(
            agency="Johns Hopkins Bloomberg School of Public Health",
            agency_class=AgencyClassType.OTHER
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `Sponsor` record (different `agency` and `agency_class`).
        obj_id = self.dal.iodi_sponsor(
            agency="National Center for Research Resources (NCRR)",
            agency_class=AgencyClassType.NIH
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODI a new `Sponsor` record (same `agency` as previous record but
        # different `agency_class`).
        obj_id = self.dal.iodi_sponsor(
            agency="National Center for Research Resources (NCRR)",
            agency_class=AgencyClassType.INDUSTRY
        )

        # The PK should be `4` as the different `agency_class` should designate
        # this as a unique record.
        self.assertEqual(obj_id, 4)

    def test_delete_sponsor(self):
        """Tests the deletion of a `Sponsor` record via the `delete` method of
        the `DalClinicalTrials` class."""

        # IODI a new `Sponsor` record.
        obj_id = self.dal.iodi_sponsor(
            agency="National Center for Research Resources (NCRR)",
            agency_class=AgencyClassType.INDUSTRY
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Sponsor, obj_id)

        # (Attempt to) retrieve the deleted record
        obj = self.dal.get(Sponsor, obj_id)  # type: Sponsor

        self.assertIsNone(obj)
