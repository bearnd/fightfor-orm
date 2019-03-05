# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `PatientData` class as well as the
`insert_patient_data` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import PatientData

from tests.bases import DalCtTestBase


class DalCtPatientDataTest(DalCtTestBase):

    def test_insert_get_patient_data(self):
        """ Tests the insertion of a `PatientData` record via the
            `insert_patient_data` method of the `DalClinicalTrials` class and
            its retrieval via the `get` method.
        """

        # Insert a new `PatientData` record.
        obj_id = self.dal.insert_patient_data(
            sharing_ipd="sharing_ipd",
            ipd_description="ipd_description",
            ipd_time_frame="ipd_time_frame",
            ipd_access_criteria="ipd_access_criteria",
            ipd_url="ipd_url",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(PatientData, obj_id)  # type: PatientData

        # Assert that the different fields of the record match.
        self.assertEqual(obj.patient_data_id, 1)
        self.assertEqual(obj.sharing_ipd, "sharing_ipd")
        self.assertEqual(obj.ipd_description, "ipd_description")
        self.assertEqual(obj.ipd_time_frame, "ipd_time_frame")
        self.assertEqual(obj.ipd_access_criteria, "ipd_access_criteria")
        self.assertEqual(obj.ipd_url, "ipd_url")

    def test_insert_patient_data_duplicate(self):
        """ Tests the insertion of duplicate `PatientData` records to ensure
            that no deduplication checks occurs.
        """

        # Inserts a new `PatientData` record.
        obj_id = self.dal.insert_patient_data(
            sharing_ipd="sharing_ipd",
            ipd_description="ipd_description",
            ipd_time_frame="ipd_time_frame",
            ipd_access_criteria="ipd_access_criteria",
            ipd_url="ipd_url",
        )

        self.assertEqual(obj_id, 1)

        # Inserts an identical `PatientData` record.
        obj_id = self.dal.insert_patient_data(
            sharing_ipd="sharing_ipd",
            ipd_description="ipd_description",
            ipd_time_frame="ipd_time_frame",
            ipd_access_criteria="ipd_access_criteria",
            ipd_url="ipd_url",
        )

        self.assertEqual(obj_id, 2)

        # Inserts a new `PatientData` record.
        obj_id = self.dal.insert_patient_data(
            sharing_ipd="new_sharing_ipd",
            ipd_description="new_ipd_description",
            ipd_time_frame="new_ipd_time_frame",
            ipd_access_criteria="new_ipd_access_criteria",
            ipd_url="new_ipd_url",
        )

        self.assertEqual(obj_id, 3)

        # Inserts the same `PatientData` record as before.
        obj_id = self.dal.insert_patient_data(
            sharing_ipd="new_sharing_ipd",
            ipd_description="new_ipd_description",
            ipd_time_frame="new_ipd_time_frame",
            ipd_access_criteria="new_ipd_access_criteria",
            ipd_url="new_ipd_url",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_patient_data(self):
        """ Tests the deletion of a `PatientData` record via the `delete` method
            of the `DalClinicalTrials` class.
        """

        # Inserts a new `PatientData` record.
        obj_id = self.dal.insert_patient_data(
            sharing_ipd="sharing_ipd",
            ipd_description="ipd_description",
            ipd_time_frame="ipd_time_frame",
            ipd_access_criteria="ipd_access_criteria",
            ipd_url="ipd_url",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(PatientData, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(PatientData, obj_id)  # type: PatientData

        self.assertIsNone(obj)
