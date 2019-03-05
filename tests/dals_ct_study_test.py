# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Study` class as well as the
`iodu_study` method of the `DalClinicalTrials` class.
"""

import datetime

from fform.orm_ct import Study
from fform.orm_ct import OverallStatusType
from fform.orm_ct import StudyType
from fform.orm_ct import PhaseType
from fform.orm_ct import BiospecRetentionType

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_oversight_info
from tests.assets.items_ct import create_expanded_access_info
from tests.assets.items_ct import create_study_design_info
from tests.assets.items_ct import create_enrollment
from tests.assets.items_ct import create_eligibility
from tests.assets.items_ct import create_study_dates
from tests.assets.items_ct import create_responsible_party
from tests.assets.items_ct import create_patient_data
from tests.assets.items_ct import create_person
from tests.assets.items_ct import create_contact


class DalCtStudyTest(DalCtTestBase):

    def test_iodu_get_study(self):
        """ Tests the IODU insertion of a `Study` record via the
            `iodu_study` method of the `DalClinicalTrials` class and its
            retrieval via the `get` method.
        """

        # Create fixtures.
        person_01_id, _ = create_person(dal=self.dal, name_first="A")
        person_02_id, _ = create_person(dal=self.dal, name_first="B")
        contact_primary_id, _ = create_contact(
            dal=self.dal,
            person_id=person_01_id,
        )
        contact_backup_id, _ = create_contact(
            dal=self.dal,
            person_id=person_02_id,
        )
        oversight_info_id, _ = create_oversight_info(dal=self.dal)
        expanded_access_info_id, _ = create_expanded_access_info(dal=self.dal)
        study_design_info_id, _ = create_study_design_info(dal=self.dal)
        enrollment_id, _ = create_enrollment(dal=self.dal)
        eligibility_id, _ = create_eligibility(dal=self.dal)
        study_dates_id, _ = create_study_dates(dal=self.dal)
        responsible_party_id, _ = create_responsible_party(dal=self.dal)
        patient_data_id, _ = create_patient_data(dal=self.dal)
        # IODU a new `Study` record.
        obj_id = self.dal.iodu_study(
            org_study_id="org_study_id",
            nct_id="nct_id",
            brief_title="brief_title",
            acronym="acronym",
            official_title="official_title",
            source="source",
            oversight_info_id=oversight_info_id,
            brief_summary="brief_summary",
            detailed_description="detailed_description",
            overall_status=OverallStatusType.ACTIVE_NOT,
            last_known_status=OverallStatusType.APPROVED,
            why_stopped="why_stopped",
            start_date=datetime.date(2019, 1, 1),
            completion_date=datetime.date(2019, 1, 1),
            primary_completion_date=datetime.date(2019, 1, 1),
            verification_date=datetime.date(2019, 1, 1),
            phase=PhaseType.PHASE_1,
            study_type=StudyType.EXPANDED,
            expanded_access_info_id=expanded_access_info_id,
            study_design_info_id=study_design_info_id,
            target_duration="target_duration",
            enrollment_id=enrollment_id,
            biospec_retention=BiospecRetentionType.SAMPLES_W_DNA,
            biospec_description="biospec_description",
            eligibility_id=eligibility_id,
            contact_primary_id=contact_primary_id,
            contact_backup_id=contact_backup_id,
            study_dates_id=study_dates_id,
            responsible_party_id=responsible_party_id,
            patient_data_id=patient_data_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Study, obj_id)  # type: Study

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_id, obj_id)
        self.assertEqual(obj.org_study_id, "org_study_id")
        self.assertEqual(obj.nct_id, "nct_id")
        self.assertEqual(obj.brief_title, "brief_title")
        self.assertEqual(obj.acronym, "acronym")
        self.assertEqual(obj.official_title, "official_title")
        self.assertEqual(obj.source, "source")
        self.assertEqual(obj.oversight_info_id, oversight_info_id)
        self.assertEqual(obj.brief_summary, "brief_summary")
        self.assertEqual(obj.detailed_description, "detailed_description")
        self.assertEqual(obj.overall_status, OverallStatusType.ACTIVE_NOT)
        self.assertEqual(obj.last_known_status, OverallStatusType.APPROVED)
        self.assertEqual(obj.why_stopped, "why_stopped")
        self.assertEqual(obj.start_date, datetime.date(2019, 1, 1))
        self.assertEqual(obj.completion_date, datetime.date(2019, 1, 1))
        self.assertEqual(obj.primary_completion_date, datetime.date(2019, 1, 1))
        self.assertEqual(obj.verification_date, datetime.date(2019, 1, 1))
        self.assertEqual(obj.phase, PhaseType.PHASE_1)
        self.assertEqual(obj.study_type, StudyType.EXPANDED)
        self.assertEqual(obj.expanded_access_info_id, expanded_access_info_id)
        self.assertEqual(obj.study_design_info_id, study_design_info_id)
        self.assertEqual(obj.target_duration, "target_duration")
        self.assertEqual(obj.enrollment_id, enrollment_id)
        self.assertEqual(
            obj.biospec_retention,
            BiospecRetentionType.SAMPLES_W_DNA,
        )
        self.assertEqual(obj.biospec_description, "biospec_description")
        self.assertEqual(obj.eligibility_id, eligibility_id)
        self.assertEqual(obj.contact_primary_id, contact_primary_id)
        self.assertEqual(obj.contact_backup_id, contact_backup_id)
        self.assertEqual(obj.study_dates_id, study_dates_id)
        self.assertEqual(obj.responsible_party_id, responsible_party_id)
        self.assertEqual(obj.patient_data_id, patient_data_id)

    def test_iodu_study_duplicate(self):
        """ Tests the IODU insertion of duplicate `Study` records to ensure
            deduplication functions as intended.
        """

        # Create fixtures.
        person_01_id, _ = create_person(dal=self.dal, name_first="A")
        person_02_id, _ = create_person(dal=self.dal, name_first="B")
        contact_primary_id, _ = create_contact(
            dal=self.dal,
            person_id=person_01_id,
        )
        contact_backup_id, _ = create_contact(
            dal=self.dal,
            person_id=person_02_id,
        )
        oversight_info_id, _ = create_oversight_info(dal=self.dal)
        expanded_access_info_id, _ = create_expanded_access_info(dal=self.dal)
        study_design_info_id, _ = create_study_design_info(dal=self.dal)
        enrollment_id, _ = create_enrollment(dal=self.dal)
        eligibility_id, _ = create_eligibility(dal=self.dal)
        study_dates_id, _ = create_study_dates(dal=self.dal)
        responsible_party_id, _ = create_responsible_party(dal=self.dal)
        patient_data_id, _ = create_patient_data(dal=self.dal)
        # IODU a new `Study` record.
        obj_id = self.dal.iodu_study(
            org_study_id="org_study_id",
            nct_id="nct_id",
            brief_title="brief_title",
            acronym="acronym",
            official_title="official_title",
            source="source",
            oversight_info_id=oversight_info_id,
            brief_summary="brief_summary",
            detailed_description="detailed_description",
            overall_status=OverallStatusType.ACTIVE_NOT,
            last_known_status=OverallStatusType.APPROVED,
            why_stopped="why_stopped",
            start_date=datetime.date(2019, 1, 1),
            completion_date=datetime.date(2019, 1, 1),
            primary_completion_date=datetime.date(2019, 1, 1),
            verification_date=datetime.date(2019, 1, 1),
            phase=PhaseType.PHASE_1,
            study_type=StudyType.EXPANDED,
            expanded_access_info_id=expanded_access_info_id,
            study_design_info_id=study_design_info_id,
            target_duration="target_duration",
            enrollment_id=enrollment_id,
            biospec_retention=BiospecRetentionType.SAMPLES_W_DNA,
            biospec_description="biospec_description",
            eligibility_id=eligibility_id,
            contact_primary_id=contact_primary_id,
            contact_backup_id=contact_backup_id,
            study_dates_id=study_dates_id,
            responsible_party_id=responsible_party_id,
            patient_data_id=patient_data_id,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `Study` record.
        obj_id = self.dal.iodu_study(
            org_study_id="org_study_id",
            nct_id="nct_id",
            brief_title="brief_title",
            acronym="acronym",
            official_title="official_title",
            source="source",
            oversight_info_id=oversight_info_id,
            brief_summary="brief_summary",
            detailed_description="detailed_description",
            overall_status=OverallStatusType.ACTIVE_NOT,
            last_known_status=OverallStatusType.APPROVED,
            why_stopped="why_stopped",
            start_date=datetime.date(2019, 1, 1),
            completion_date=datetime.date(2019, 1, 1),
            primary_completion_date=datetime.date(2019, 1, 1),
            verification_date=datetime.date(2019, 1, 1),
            phase=PhaseType.PHASE_1,
            study_type=StudyType.EXPANDED,
            expanded_access_info_id=expanded_access_info_id,
            study_design_info_id=study_design_info_id,
            target_duration="target_duration",
            enrollment_id=enrollment_id,
            biospec_retention=BiospecRetentionType.SAMPLES_W_DNA,
            biospec_description="biospec_description",
            eligibility_id=eligibility_id,
            contact_primary_id=contact_primary_id,
            contact_backup_id=contact_backup_id,
            study_dates_id=study_dates_id,
            responsible_party_id=responsible_party_id,
            patient_data_id=patient_data_id,
        )

        self.assertEqual(obj_id, 1)

        # IODU the same `Study` record with a changed `brief_title` field
        # which should trigger an update on the existing record.
        obj_id = self.dal.iodu_study(
            org_study_id="org_study_id",
            nct_id="nct_id",
            brief_title="new_brief_title",
            acronym="acronym",
            official_title="official_title",
            source="source",
            oversight_info_id=oversight_info_id,
            brief_summary="brief_summary",
            detailed_description="detailed_description",
            overall_status=OverallStatusType.ACTIVE_NOT,
            last_known_status=OverallStatusType.APPROVED,
            why_stopped="why_stopped",
            start_date=datetime.date(2019, 1, 1),
            completion_date=datetime.date(2019, 1, 1),
            primary_completion_date=datetime.date(2019, 1, 1),
            verification_date=datetime.date(2019, 1, 1),
            phase=PhaseType.PHASE_1,
            study_type=StudyType.EXPANDED,
            expanded_access_info_id=expanded_access_info_id,
            study_design_info_id=study_design_info_id,
            target_duration="target_duration",
            enrollment_id=enrollment_id,
            biospec_retention=BiospecRetentionType.SAMPLES_W_DNA,
            biospec_description="biospec_description",
            eligibility_id=eligibility_id,
            contact_primary_id=contact_primary_id,
            contact_backup_id=contact_backup_id,
            study_dates_id=study_dates_id,
            responsible_party_id=responsible_party_id,
            patient_data_id=patient_data_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(Study, obj_id)  # type: Study

        self.assertEqual(obj.brief_title, "new_brief_title")

        # IODU a new `Study` record.
        obj_id = self.dal.iodu_study(
            org_study_id="org_study_id",
            nct_id="new_nct_id",
            brief_title="brief_title",
            acronym="acronym",
            official_title="official_title",
            source="source",
            oversight_info_id=oversight_info_id,
            brief_summary="brief_summary",
            detailed_description="detailed_description",
            overall_status=OverallStatusType.ACTIVE_NOT,
            last_known_status=OverallStatusType.APPROVED,
            why_stopped="why_stopped",
            start_date=datetime.date(2019, 1, 1),
            completion_date=datetime.date(2019, 1, 1),
            primary_completion_date=datetime.date(2019, 1, 1),
            verification_date=datetime.date(2019, 1, 1),
            phase=PhaseType.PHASE_1,
            study_type=StudyType.EXPANDED,
            expanded_access_info_id=expanded_access_info_id,
            study_design_info_id=study_design_info_id,
            target_duration="target_duration",
            enrollment_id=enrollment_id,
            biospec_retention=BiospecRetentionType.SAMPLES_W_DNA,
            biospec_description="biospec_description",
            eligibility_id=eligibility_id,
            contact_primary_id=contact_primary_id,
            contact_backup_id=contact_backup_id,
            study_dates_id=study_dates_id,
            responsible_party_id=responsible_party_id,
            patient_data_id=patient_data_id,
        )

        self.assertEqual(obj_id, 4)

        # IODU the same `Descriptor` record as before.
        obj_id = self.dal.iodu_study(
            org_study_id="org_study_id",
            nct_id="new_nct_id",
            brief_title="brief_title",
            acronym="acronym",
            official_title="official_title",
            source="source",
            oversight_info_id=oversight_info_id,
            brief_summary="brief_summary",
            detailed_description="detailed_description",
            overall_status=OverallStatusType.ACTIVE_NOT,
            last_known_status=OverallStatusType.APPROVED,
            why_stopped="why_stopped",
            start_date=datetime.date(2019, 1, 1),
            completion_date=datetime.date(2019, 1, 1),
            primary_completion_date=datetime.date(2019, 1, 1),
            verification_date=datetime.date(2019, 1, 1),
            phase=PhaseType.PHASE_1,
            study_type=StudyType.EXPANDED,
            expanded_access_info_id=expanded_access_info_id,
            study_design_info_id=study_design_info_id,
            target_duration="target_duration",
            enrollment_id=enrollment_id,
            biospec_retention=BiospecRetentionType.SAMPLES_W_DNA,
            biospec_description="biospec_description",
            eligibility_id=eligibility_id,
            contact_primary_id=contact_primary_id,
            contact_backup_id=contact_backup_id,
            study_dates_id=study_dates_id,
            responsible_party_id=responsible_party_id,
            patient_data_id=patient_data_id,
        )

        self.assertEqual(obj_id, 4)

    def test_delete_reference(self):
        """ Tests the deletion of a `Study` record via the `delete` method
            of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        person_01_id, _ = create_person(dal=self.dal, name_first="A")
        person_02_id, _ = create_person(dal=self.dal, name_first="B")
        contact_primary_id, _ = create_contact(
            dal=self.dal,
            person_id=person_01_id,
        )
        contact_backup_id, _ = create_contact(
            dal=self.dal,
            person_id=person_02_id,
        )
        oversight_info_id, _ = create_oversight_info(dal=self.dal)
        expanded_access_info_id, _ = create_expanded_access_info(dal=self.dal)
        study_design_info_id, _ = create_study_design_info(dal=self.dal)
        enrollment_id, _ = create_enrollment(dal=self.dal)
        eligibility_id, _ = create_eligibility(dal=self.dal)
        study_dates_id, _ = create_study_dates(dal=self.dal)
        responsible_party_id, _ = create_responsible_party(dal=self.dal)
        patient_data_id, _ = create_patient_data(dal=self.dal)
        # IODU a new `Study` record.
        obj_id = self.dal.iodu_study(
            org_study_id="org_study_id",
            nct_id="nct_id",
            brief_title="brief_title",
            acronym="acronym",
            official_title="official_title",
            source="source",
            oversight_info_id=oversight_info_id,
            brief_summary="brief_summary",
            detailed_description="detailed_description",
            overall_status=OverallStatusType.ACTIVE_NOT,
            last_known_status=OverallStatusType.APPROVED,
            why_stopped="why_stopped",
            start_date=datetime.date(2019, 1, 1),
            completion_date=datetime.date(2019, 1, 1),
            primary_completion_date=datetime.date(2019, 1, 1),
            verification_date=datetime.date(2019, 1, 1),
            phase=PhaseType.PHASE_1,
            study_type=StudyType.EXPANDED,
            expanded_access_info_id=expanded_access_info_id,
            study_design_info_id=study_design_info_id,
            target_duration="target_duration",
            enrollment_id=enrollment_id,
            biospec_retention=BiospecRetentionType.SAMPLES_W_DNA,
            biospec_description="biospec_description",
            eligibility_id=eligibility_id,
            contact_primary_id=contact_primary_id,
            contact_backup_id=contact_backup_id,
            study_dates_id=study_dates_id,
            responsible_party_id=responsible_party_id,
            patient_data_id=patient_data_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(Study, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(Study, obj_id)  # type: Study

        self.assertIsNone(obj)
