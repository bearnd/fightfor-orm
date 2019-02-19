# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Enrollment` class as well as the
`insert_enrollment` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import Enrollment
from fform.orm_ct import ActualType

from tests.bases import DalCtTestBase


class DalCtEnrollmentTest(DalCtTestBase):

    def test_insert_get_enrollment(self):
        """ Tests the insertion of a `Enrollment` record via the
            `insert_enrollment` method of the `DalClinicalTrials` class and its
            retrieval via the `get` method.
        """

        # IODI a new `Enrollment` record.
        obj_id = self.dal.insert_enrollment(
            value=1,
            enrollment_type=ActualType.ACTUAL,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            Enrollment,
            obj_id,
        )  # type: Enrollment

        # Assert that the different fields of the record match.
        self.assertEqual(obj.enrollment_id, 1)
        self.assertEqual(obj.value, 1)
        self.assertEqual(obj.enrollment_type, ActualType.ACTUAL)

    def test_insert_enrollment_duplicate(self):
        """ Tests the insertion of duplicate `Enrollment` records to
            ensure that no deduplication checks occurs.
        """

        # IODI a new `Enrollment` record.
        obj_id = self.dal.insert_enrollment(
            value=1,
            enrollment_type=ActualType.ACTUAL,
        )
        self.assertEqual(obj_id, 1)

        # IODI an identical `Enrollment` record.
        obj_id = self.dal.insert_enrollment(
            value=1,
            enrollment_type=ActualType.ACTUAL,
        )
        self.assertEqual(obj_id, 2)

        # IODI a new `Enrollment` record.
        obj_id = self.dal.insert_enrollment(
            value=2,
            enrollment_type=ActualType.ANTICIPATED,
        )
        self.assertEqual(obj_id, 3)

        # IODI the same `Enrollment` record as before only lowercased.
        obj_id = self.dal.insert_enrollment(
            value=2,
            enrollment_type=ActualType.ANTICIPATED,
        )
        self.assertEqual(obj_id, 4)

    def test_delete_enrollment(self):
        """ Tests the deletion of a `Enrollment` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # IODI a new `Enrollment` record.
        obj_id = self.dal.insert_enrollment(
            value=1,
            enrollment_type=ActualType.ACTUAL,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Enrollment, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            Enrollment,
            obj_id,
        )  # type: Enrollment

        self.assertIsNone(obj)
