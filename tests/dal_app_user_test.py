# -*- coding: utf-8 -*-

from fform.orm_app import User

from tests.bases import DalAppTestBase


class DalAppUserTest(DalAppTestBase):
    """ Tests the `DalApp` methods on the `User` class."""

    def test_iodi_get_user(self):
        """ Tests the insertion of a `User` record via the `iodi_user` method of
            the `DalApp` class and its retrieval via the `get` method.
        """

        # IODI a new `User` record.
        obj_id = self.dal.iodi_user(
            auth0_user_id="auth0|12345678",
            email="fake@email.com",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(User, obj_id)  # type: User

        # Assert that the different fields of the record match.
        self.assertEqual(obj.user_id, 1)
        self.assertEqual(obj.auth0_user_id, "auth0|12345678")
        self.assertEqual(obj.email, "fake@email.com")

    def test_iodi_user_duplicate(self):
        """ Tests the IODI insertion of duplicate `User` records to ensure
            deduplication functions as intended.
        """

        # IODI a new `User` record.
        obj_id = self.dal.iodi_user(
            auth0_user_id="auth0|12345678",
            email="fake@email.com",
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `Condition` record.
        obj_id = self.dal.iodi_user(
            auth0_user_id="auth0|12345678",
            email="fake@email.com",
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `User` record.
        obj_id = self.dal.iodi_user(
            auth0_user_id="auth0|87654321",
            email="fake@email.com",
        )

        self.assertEqual(obj_id, 3)

    def test_delete_user(self):
        """ Tests the deletion of a `User` record via the `delete` method of
            the `DalApp` class.
        """

        # IODI a new `User` record.
        obj_id = self.dal.iodi_user(
            auth0_user_id="auth0|12345678",
            email="fake@email.com",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(User, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(User, obj_id)  # type: User

        self.assertIsNone(obj)

    def test_update_user(self):
        """ Tests the update of a `User` record via the `update` method of the
            `DalApp` class.
        """

        # IODI a new `User` record.
        obj_id = self.dal.iodi_user(
            auth0_user_id="auth0|12345678",
            email="fake@email.com",
        )

        # Update the record.
        self.dal.update_attr_value(
            orm_class=User,
            pk=obj_id,
            attr_name="email",
            attr_value="different@email.com",
        )

        # Retrieve the updated record.
        obj_updated = self.dal.get(User, obj_id)  # type: User

        # Assert that the ID remained the same.
        self.assertEqual(obj_updated.user_id, 1)
        # Assert that attribute changed.
        self.assertEqual(obj_updated.email, "different@email.com")
