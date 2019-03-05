# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Eligibility` class as well as the
`insert_eligibility` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import Eligibility
from fform.orm_ct import SamplingMethodType
from fform.orm_ct import GenderType

from tests.bases import DalCtTestBase


class DalCtEligibilityTest(DalCtTestBase):

    def test_insert_get_eligibility(self):
        """ Tests the insertion of a `Eligibility` record via the
            `insert_eligibility` method of the `DalClinicalTrials` class and its
            retrieval via the `get` method.
        """

        # Insert a new `Eligibility` record.
        obj_id = self.dal.insert_eligibility(
            study_pop="study_pop",
            sampling_method=SamplingMethodType.PROBABILITY,
            criteria="criteria",
            gender=GenderType.ALL,
            gender_based=False,
            gender_description="gender_description",
            minimum_age="1 year",
            maximum_age="10 years",
            healthy_volunteers="healthy_volunteers",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Eligibility, obj_id)  # type: Eligibility

        # Assert that the different fields of the record match.
        self.assertEqual(obj.eligibility_id, 1)
        self.assertEqual(obj.study_pop, "study_pop")
        self.assertEqual(obj.sampling_method, SamplingMethodType.PROBABILITY)
        self.assertEqual(obj.criteria, "criteria")
        self.assertEqual(obj.gender, GenderType.ALL)
        self.assertEqual(obj.gender_based, False)
        self.assertEqual(obj.gender_description, "gender_description")
        self.assertEqual(obj.minimum_age, "1 year")
        self.assertEqual(obj.maximum_age, "10 years")
        self.assertEqual(obj.healthy_volunteers, "healthy_volunteers")

    def test_insert_eligibility_duplicate(self):
        """ Tests the Inserts insertion of duplicate `Eligibility` records to
            ensure that no deduplication checks occurs.
        """

        # Inserts a new `Eligibility` record.
        obj_id = self.dal.insert_eligibility(
            study_pop="study_pop",
            sampling_method=SamplingMethodType.PROBABILITY,
            criteria="criteria",
            gender=GenderType.ALL,
            gender_based=False,
            gender_description="gender_description",
            minimum_age="1 year",
            maximum_age="10 years",
            healthy_volunteers="healthy_volunteers",
        )

        self.assertEqual(obj_id, 1)

        # Inserts an identical `Eligibility` record.
        obj_id = self.dal.insert_eligibility(
            study_pop="study_pop",
            sampling_method=SamplingMethodType.PROBABILITY,
            criteria="criteria",
            gender=GenderType.ALL,
            gender_based=False,
            gender_description="gender_description",
            minimum_age="1 year",
            maximum_age="10 years",
            healthy_volunteers="healthy_volunteers",
        )

        self.assertEqual(obj_id, 2)

        # Inserts a new `Eligibility` record.
        obj_id = self.dal.insert_eligibility(
            study_pop="new_study_pop",
            sampling_method=SamplingMethodType.NON_PROBABILITY,
            criteria="new_criteria",
            gender=GenderType.MALE,
            gender_based=True,
            gender_description="new_gender_description",
            minimum_age="new 1 year",
            maximum_age="new 10 years",
            healthy_volunteers="new_healthy_volunteers",
        )

        self.assertEqual(obj_id, 3)

        # Inserts the same `Eligibility` record as before.
        obj_id = self.dal.insert_eligibility(
            study_pop="new_study_pop",
            sampling_method=SamplingMethodType.NON_PROBABILITY,
            criteria="new_criteria",
            gender=GenderType.MALE,
            gender_based=True,
            gender_description="new_gender_description",
            minimum_age="new 1 year",
            maximum_age="new 10 years",
            healthy_volunteers="new_healthy_volunteers",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_eligibility(self):
        """ Tests the deletion of a `Eligibility` record via the `delete` method
            of the `DalClinicalTrials` class.
        """

        # Inserts a new `Eligibility` record.
        obj_id = self.dal.insert_eligibility(
            study_pop="study_pop",
            sampling_method=SamplingMethodType.PROBABILITY,
            criteria="criteria",
            gender=GenderType.ALL,
            gender_based=False,
            gender_description="gender_description",
            minimum_age="1 year",
            maximum_age="10 years",
            healthy_volunteers="healthy_volunteers",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Eligibility, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Eligibility, obj_id)  # type: Eligibility

        self.assertIsNone(obj)
