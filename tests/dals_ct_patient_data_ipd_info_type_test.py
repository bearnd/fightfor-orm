# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `PatientDataIpdInfoType` class as well as
the `insert_patient_data_ipd_info_type` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import PatientDataIpdInfoType

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_patient_data


class DalCtPatientDataIpdInfoTypeTest(DalCtTestBase):

    def test_insert_get_patient_data_ipd_info_type(self):
        """ Tests the insertion of a `PatientDataIpdInfoType` record via the
            `insert_patient_data_ipd_info_type` method of the
            `DalClinicalTrials` class and its retrieval via the `get` method.
        """

        # Create an `PatientData` record as a fixture.
        patient_data_id, _ = create_patient_data(dal=self.dal)

        # Insert a new `PatientDataIpdInfoType` record.
        obj_id = self.dal.insert_patient_data_ipd_info_type(
            patient_data_id=patient_data_id,
            ipd_info_type="ipd_info_type",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            PatientDataIpdInfoType,
            obj_id,
        )  # type: PatientDataIpdInfoType

        # Assert that the different fields of the record match.
        self.assertEqual(obj.patient_data_ipd_info_type_id, 1)
        self.assertEqual(obj.patient_data_id, patient_data_id)
        self.assertEqual(obj.ipd_info_type, "ipd_info_type")

    def test_insert_patient_data_ipd_info_type_duplicate(self):
        """ Tests the insertion of duplicate `PatientDataIpdInfoType` records to
            ensure that no deduplication checks occurs.
        """

        # Create an `PatientData` record as a fixture.
        patient_data_id, _ = create_patient_data(dal=self.dal)

        # Inserts a new `PatientDataIpdInfoType` record.
        obj_id = self.dal.insert_patient_data_ipd_info_type(
            patient_data_id=patient_data_id,
            ipd_info_type="ipd_info_type",
        )

        self.assertEqual(obj_id, 1)

        # Inserts a new `PatientDataIpdInfoType` record.
        obj_id = self.dal.insert_patient_data_ipd_info_type(
            patient_data_id=patient_data_id,
            ipd_info_type="ipd_info_type",
        )

        self.assertEqual(obj_id, 2)

        # Inserts a new `PatientDataIpdInfoType` record.
        obj_id = self.dal.insert_patient_data_ipd_info_type(
            patient_data_id=patient_data_id,
            ipd_info_type="new_ipd_info_type",
        )

        self.assertEqual(obj_id, 3)

        # Inserts the same `PatientDataIpdInfoType` record as before.
        obj_id = self.dal.insert_patient_data_ipd_info_type(
            patient_data_id=patient_data_id,
            ipd_info_type="new_ipd_info_type",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_intervention_alias(self):
        """ Tests the deletion of a `PatientDataIpdInfoType` record via the
            `delete` method of the `DalClinicalTrials` class.
        """

        # Create an `PatientData` record as a fixture.
        patient_data_id, _ = create_patient_data(dal=self.dal)

        # Inserts a new `PatientDataIpdInfoType` record.
        obj_id = self.dal.insert_patient_data_ipd_info_type(
            patient_data_id=patient_data_id,
            ipd_info_type="ipd_info_type",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(PatientDataIpdInfoType, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            PatientDataIpdInfoType,
            obj_id,
        )  # type: PatientDataIpdInfoType

        self.assertIsNone(obj)
