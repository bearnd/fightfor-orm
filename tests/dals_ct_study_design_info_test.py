# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyDesignInfo` class as well as the
`insert_study_design_info` method of the `DalClinicalTrials` class.
"""

from fform.orm_ct import StudyDesignInfo

from tests.bases import DalCtTestBase


class DalCtStudyDesignInfoTest(DalCtTestBase):

    def test_insert_get_study_design_info(self):
        """ Tests the insertion of a `StudyDesignInfo` record via the
            `insert_study_design_info` method of the `DalClinicalTrials`
            class and its retrieval via the `get` method.
        """

        # IODI a new `StudyDesignInfo` record.
        obj_id = self.dal.insert_study_design_info(
            allocation="allocation",
            intervention_model="intervention_model",
            intervention_model_description="intervention_model_description",
            primary_purpose="primary_purpose",
            observational_model="observational_model",
            time_perspective="time_perspective",
            masking="masking",
            masking_description="masking_description",
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            StudyDesignInfo,
            obj_id,
        )  # type: StudyDesignInfo

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_design_info_id, 1)
        self.assertEqual(obj.allocation, "allocation")
        self.assertEqual(obj.intervention_model, "intervention_model")
        self.assertEqual(
            obj.intervention_model_description,
            "intervention_model_description",
        )
        self.assertEqual(obj.primary_purpose, "primary_purpose")
        self.assertEqual(obj.observational_model, "observational_model")
        self.assertEqual(obj.time_perspective, "time_perspective")
        self.assertEqual(obj.masking, "masking")
        self.assertEqual(obj.masking_description, "masking_description")

    def test_insert_study_design_info_duplicate(self):
        """ Tests the insertion of duplicate `StudyDesignInfo` records to
            ensure that no deduplication checks occurs.
        """

        # IODI a new `StudyDesignInfo` record.
        obj_id = self.dal.insert_study_design_info(
            allocation="allocation",
            intervention_model="intervention_model",
            intervention_model_description="intervention_model_description",
            primary_purpose="primary_purpose",
            observational_model="observational_model",
            time_perspective="time_perspective",
            masking="masking",
            masking_description="masking_description",
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `StudyDesignInfo` record.
        obj_id = self.dal.insert_study_design_info(
            allocation="allocation",
            intervention_model="intervention_model",
            intervention_model_description="intervention_model_description",
            primary_purpose="primary_purpose",
            observational_model="observational_model",
            time_perspective="time_perspective",
            masking="masking",
            masking_description="masking_description",
        )

        self.assertEqual(obj_id, 2)

        # IODI a new `StudyDesignInfo` record.
        obj_id = self.dal.insert_study_design_info(
            allocation="new_allocation",
            intervention_model="new_intervention_model",
            intervention_model_description="new_intervention_model_description",
            primary_purpose="new_primary_purpose",
            observational_model="new_observational_model",
            time_perspective="new_time_perspective",
            masking="new_masking",
            masking_description="new_masking_description",
        )

        self.assertEqual(obj_id, 3)

        # IODI the same `StudyDesignInfo` record as before only lowercased.
        obj_id = self.dal.insert_study_design_info(
            allocation="new_allocation",
            intervention_model="new_intervention_model",
            intervention_model_description="new_intervention_model_description",
            primary_purpose="new_primary_purpose",
            observational_model="new_observational_model",
            time_perspective="new_time_perspective",
            masking="new_masking",
            masking_description="new_masking_description",
        )

        self.assertEqual(obj_id, 4)

    def test_delete_study_design_info(self):
        """ Tests the deletion of a `StudyDesignInfo` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # IODI a new `StudyDesignInfo` record.
        obj_id = self.dal.insert_study_design_info(
            allocation="allocation",
            intervention_model="intervention_model",
            intervention_model_description="intervention_model_description",
            primary_purpose="primary_purpose",
            observational_model="observational_model",
            time_perspective="time_perspective",
            masking="masking",
            masking_description="masking_description",
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyDesignInfo, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            StudyDesignInfo,
            obj_id,
        )  # type: StudyDesignInfo

        self.assertIsNone(obj)
