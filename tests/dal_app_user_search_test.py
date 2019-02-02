# -*- coding: utf-8 -*-

import uuid

from fform.orm_app import UserSearch
from fform.orm_ct import GenderType

from tests.bases import DalAppTestBase


class DalAppUserSearchTest(DalAppTestBase):
    """ Tests the `DalApp` methods on the `UserSearch` class."""

    def test_iodi_get_user_search(self):
        """ Tests the insertion of a `UserSearch` record via the
            `iodi_user_search` method of the `DalApp` class and its retrieval
            via the `get` method.
        """

        # IODI a new `User` record.
        user_id = self.dal.iodi_user(
            auth0_user_id="auth0|12345678",
            email="fake@email.com",
        )

        # IODI a new `Search` record.
        search_id = self.dal.iodu_search(
            search_uuid=uuid.uuid4(),
            title="Search Title",
            gender=GenderType.FEMALE,
            year_beg=2013,
            year_end=2023,
            age_beg=10,
            age_end=30,
        )

        # IODI a new `UserSearch` record.
        obj_id = self.dal.iodi_user_search(
            user_id=user_id,
            search_id=search_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(UserSearch, obj_id)  # type: UserSearch

        # Assert that the different fields of the record match.
        self.assertEqual(obj.user_search_id, 1)
        self.assertEqual(obj.user_id, user_id)
        self.assertEqual(obj.search_id, search_id)
