# -*- coding: utf-8 -*-

import uuid

from fform.orm_app import Search
from fform.orm_ct import GenderType

from tests.bases import DalAppTestBase


class DalAppUserSearch(DalAppTestBase):
    """ Tests the `DalApp` methods on the `Search` class."""

    def test_iodu_get_search(self):
        """ Tests the insertion of a `Search` record via the `iodu_search`
            method  of the `DalApp` class and its retrieval via the `get`
            method.
        """

        search_uuid = uuid.uuid4()

        # IODI a new `Search` record.
        obj_id = self.dal.iodu_search(
            search_uuid=search_uuid,
            title="Search Title",
            gender=GenderType.FEMALE,
            year_beg=2013,
            year_end=2023,
            age_beg=10,
            age_end=30,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Search, obj_id)  # type: Search

        # Assert that the different fields of the record match.
        self.assertEqual(obj.search_id, 1)
        self.assertEqual(obj.search_uuid, search_uuid)
        self.assertEqual(obj.title, "Search Title")
        self.assertEqual(obj.gender, GenderType.FEMALE)
        self.assertEqual(obj.year_beg, 2013)
        self.assertEqual(obj.year_end, 2023)
        self.assertEqual(obj.age_beg, 10)
        self.assertEqual(obj.age_end, 30)

    def test_iodu_search_duplicate(self):
        """ Tests the IODU insertion of duplicate `Search` records to ensure
            deduplication functions as intended.
        """

        search_uuid = uuid.uuid4()

        # IODU a new `Search` record.
        obj_id = self.dal.iodu_search(
            search_uuid=search_uuid,
            title="Search Title",
            gender=GenderType.FEMALE,
            year_beg=2013,
            year_end=2023,
            age_beg=10,
            age_end=30,
        )

        self.assertEqual(obj_id, 1)

        # IODU an identical `Search` record.
        obj_id = self.dal.iodu_search(
            search_uuid=search_uuid,
            title="Search Title",
            gender=GenderType.FEMALE,
            year_beg=2013,
            year_end=2023,
            age_beg=10,
            age_end=30,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `Search` record.
        obj_id = self.dal.iodu_search(
            search_uuid=uuid.uuid4(),
            title="Search Title",
            gender=GenderType.FEMALE,
            year_beg=2013,
            year_end=2023,
            age_beg=10,
            age_end=30,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_search(self):
        """ Tests the deletion of a `Search` record via the `delete` method of
            the `DalApp` class.
        """

        search_uuid = uuid.uuid4()

        # IODU a new `Search` record.
        obj_id = self.dal.iodu_search(
            search_uuid=search_uuid,
            title="Search Title",
            gender=GenderType.FEMALE,
            year_beg=2013,
            year_end=2023,
            age_beg=10,
            age_end=30,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Search, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Search, obj_id)  # type: Search

        self.assertIsNone(obj)

    def test_update_search(self):
        """ Tests the update of a `Search` record via the `update` method of the
            `DalApp` class.
        """

        search_uuid = uuid.uuid4()

        # IODU a new `Search` record.
        obj_id = self.dal.iodu_search(
            search_uuid=search_uuid,
            title="Search Title",
            gender=GenderType.FEMALE,
            year_beg=2013,
            year_end=2023,
            age_beg=10,
            age_end=30,
        )

        # Update the record.
        self.dal.update_attr_value(
            orm_class=Search,
            pk=obj_id,
            attr_name="title",
            attr_value="New title",
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(Search, obj_id)  # type: Search

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.search_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.title, "New title")
