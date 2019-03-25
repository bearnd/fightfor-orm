# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyDescriptor` class as well as the
`iodu_study_descriptor` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyDescriptor
from fform.orm_ct import MeshTermType
from fform.dals_mt import DalMesh

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_mt import create_descriptor


class DalCtStudyDescriptorTest(DalCtTestBase):

    def setUp(self):

        super(DalCtStudyDescriptorTest, self).setUp()

        self.dal_mesh = DalMesh(
            sql_username=self.cfg.sql_username,
            sql_password=self.cfg.sql_password,
            sql_host=self.cfg.sql_host,
            sql_port=self.cfg.sql_port,
            sql_db=self.cfg.sql_db
        )

    def test_iodu_get_study_descriptor(self):
        """ Tests the insertion of a `StudyDescriptor` record via the
            `iodu_study_descriptor` method of the `DalClinicalTrials` class and
            its retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal_mesh)

        # IODU a new `StudyDescriptor` record.
        obj_id = self.dal.iodu_study_descriptor(
            study_id=study_id,
            descriptor_id=descriptor_id,
            study_descriptor_type=MeshTermType.CONDITION,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyDescriptor, obj_id)  # type: StudyDescriptor

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_descriptor_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.study_descriptor_type, MeshTermType.CONDITION)

    def test_iodu_study_descriptor_missing_fk(self):
        """ Tests the insertion of a `StudyDescriptor` record via the
            `iodu_study_descriptor` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodu_study_descriptor,
            # This FK is invalid.
            study_id=123,
            descriptor_id=123,
            study_descriptor_type=MeshTermType.CONDITION,
        )

    def test_iodu_study_descriptor_duplicate(self):
        """ Tests the IODU insertion of duplicate `StudyDescriptor` records to
            ensure deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal_mesh)
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal_mesh,
            ui="new_ui",
            name="new_name",
        )

        # IODU a new `StudyDescriptor` record.
        obj_id = self.dal.iodu_study_descriptor(
            study_id=study_id,
            descriptor_id=descriptor_id,
            study_descriptor_type=MeshTermType.CONDITION,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODU the same `StudyDescriptor` record as before.
        obj_id = self.dal.iodu_study_descriptor(
            study_id=study_id,
            descriptor_id=descriptor_id,
            study_descriptor_type=MeshTermType.CONDITION,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODU a new `StudyDescriptor` record.
        obj_id = self.dal.iodu_study_descriptor(
            study_id=study_id,
            descriptor_id=descriptor_02_id,
            study_descriptor_type=MeshTermType.CONDITION,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyDescriptor` record as before.
        obj_id = self.dal.iodu_study_descriptor(
            study_id=study_id,
            descriptor_id=descriptor_02_id,
            study_descriptor_type=MeshTermType.CONDITION,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_descriptor(self):
        """ Tests the deletion of a `StudyDescriptor` record via the `delete`
            method of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        descriptor_id, _ = create_descriptor(dal=self.dal_mesh)

        # IODU a new `StudyDescriptor` record.
        obj_id = self.dal.iodu_study_descriptor(
            study_id=study_id,
            descriptor_id=descriptor_id,
            study_descriptor_type=MeshTermType.CONDITION,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyDescriptor, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyDescriptor, obj_id)  # type: StudyDescriptor

        self.assertIsNone(obj)
