# -*- coding: utf-8 -*-

import copy

from fform.orm_pubmed import AffiliationCanonical
from geoalchemy2.shape import to_shape

from tests.bases import DalPubmedTestBase


_iodu_affiliation_canonical_args = {
    "google_place_id": "google_place_id",
    "name": "name",
    "google_url": "google_url",
    "url": "url",
    "address": "address",
    "phone_number": "phone_number",
    "coordinate_longitude": 1.0,
    "coordinate_latitude": -1.0,
    "country": "country",
    "administrative_area_level_1": "administrative_area_level_1",
    "administrative_area_level_2": "administrative_area_level_2",
    "administrative_area_level_3": "administrative_area_level_3",
    "administrative_area_level_4": "administrative_area_level_4",
    "administrative_area_level_5": "administrative_area_level_5",
    "locality": "locality",
    "sublocality": "sublocality",
    "sublocality_level_1": "sublocality_level_1",
    "sublocality_level_2": "sublocality_level_2",
    "sublocality_level_3": "sublocality_level_3",
    "sublocality_level_4": "sublocality_level_4",
    "sublocality_level_5": "sublocality_level_5",
    "colloquial_area": "colloquial_area",
    "floor": "floor",
    "room": "room",
    "intersection": "intersection",
    "neighborhood": "neighborhood",
    "post_box": "post_box",
    "postal_code": "postal_code",
    "postal_code_prefix": "postal_code_prefix",
    "postal_code_suffix": "postal_code_suffix",
    "postal_town": "postal_town",
    "premise": "premise",
    "subpremise": "subpremise",
    "route": "route",
    "street_address": "street_address",
    "street_number": "street_number",
}


class DalPubmedAffiliationCanonicalTest(DalPubmedTestBase):

    def test_iodu_affiliation_canonical(self):
        """Tests the insertion of a `AffiliationCanonical` record via the
        `iodu_affiliation_canonical` method of the `DalPubmed` class and
        its retrieval via the `get` method."""

        # IODU a new `AffiliationCanonical` record.
        obj_id = self.dal.iodu_affiliation_canonical(
            **_iodu_affiliation_canonical_args
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            AffiliationCanonical,
            obj_id,
        )  # type: AffiliationCanonical

        # Assert that the different fields of the record match.
        self.assertEqual(obj.affiliation_canonical_id, 1)
        self.assertEqual(obj.google_place_id, "google_place_id")
        self.assertEqual(obj.name, "name")
        self.assertEqual(obj.google_url, "google_url")
        self.assertEqual(obj.url, "url")
        self.assertEqual(obj.address, "address")
        self.assertEqual(obj.phone_number, "phone_number")
        self.assertEqual(to_shape(obj.coordinates).wkt, "POINT (1 -1)")
        self.assertEqual(obj.country, "country")
        self.assertEqual(
            obj.administrative_area_level_1,
            "administrative_area_level_1",
        )
        self.assertEqual(
            obj.administrative_area_level_2,
            "administrative_area_level_2",
        )
        self.assertEqual(
            obj.administrative_area_level_3,
            "administrative_area_level_3",
        )
        self.assertEqual(
            obj.administrative_area_level_4,
            "administrative_area_level_4",
        )
        self.assertEqual(
            obj.administrative_area_level_5,
            "administrative_area_level_5",
        )
        self.assertEqual(obj.locality, "locality")
        self.assertEqual(obj.sublocality, "sublocality")
        self.assertEqual(obj.sublocality_level_1, "sublocality_level_1")
        self.assertEqual(obj.sublocality_level_2, "sublocality_level_2")
        self.assertEqual(obj.sublocality_level_3, "sublocality_level_3")
        self.assertEqual(obj.sublocality_level_4, "sublocality_level_4")
        self.assertEqual(obj.sublocality_level_5, "sublocality_level_5")
        self.assertEqual(obj.colloquial_area, "colloquial_area")
        self.assertEqual(obj.floor, "floor")
        self.assertEqual(obj.room, "room")
        self.assertEqual(obj.intersection, "intersection")
        self.assertEqual(obj.neighborhood, "neighborhood")
        self.assertEqual(obj.post_box, "post_box")
        self.assertEqual(obj.postal_code, "postal_code")
        self.assertEqual(obj.postal_code_prefix, "postal_code_prefix")
        self.assertEqual(obj.postal_code_suffix, "postal_code_suffix")
        self.assertEqual(obj.postal_town, "postal_town")
        self.assertEqual(obj.premise, "premise")
        self.assertEqual(obj.subpremise, "subpremise")
        self.assertEqual(obj.route, "route")
        self.assertEqual(obj.street_address, "street_address")
        self.assertEqual(obj.street_number, "street_number")

    def test_iodu_affiliation_canonical_duplicate(self):
        """Tests the IODU insertion of duplicate `AffiliationCanonical` records
        to ensure deduplication functions as intended."""

        # IODU a new `AffiliationCanonical` record.
        obj_id = self.dal.iodu_affiliation_canonical(
            **_iodu_affiliation_canonical_args
        )

        self.assertEqual(obj_id, 1)

        # IODI the same `AffiliationCanonical` record as before.
        obj_id = self.dal.iodu_affiliation_canonical(
            **_iodu_affiliation_canonical_args
        )

        self.assertEqual(obj_id, 1)

        _iodu_affiliation_canonical_args_copy = copy.deepcopy(
            _iodu_affiliation_canonical_args
        )
        _iodu_affiliation_canonical_args_copy["google_place_id"] = "2"

        # IODI a new `AffiliationCanonical` record (while still having the same
        # name).
        obj_id = self.dal.iodu_affiliation_canonical(
            **_iodu_affiliation_canonical_args_copy
        )

        self.assertEqual(obj_id, 3)

    def test_delete_affiliation_canonical(self):
        """Tests the deletion of a `AffiliationCanonical` record via the
        `delete` method of the `DalPubmed` class."""

        # IODU a new `AffiliationCanonical` record.
        obj_id = self.dal.iodu_affiliation_canonical(
            **_iodu_affiliation_canonical_args
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(AffiliationCanonical, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            AffiliationCanonical,
            obj_id,
        )  # type: AffiliationCanonical

        self.assertIsNone(obj)
