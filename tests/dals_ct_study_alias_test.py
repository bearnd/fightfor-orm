# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `StudyAlias` class as well as the
`iodi_study_alias` method of the `DalClinicalTrials` class.
"""

import sqlalchemy.exc

from fform.orm_ct import StudyAlias

from tests.bases import DalCtTestBase
from tests.assets.items_ct import create_study
from tests.assets.items_ct import create_alias


class DalCtStudyAliasTest(DalCtTestBase):

    def test_iodi_get_study_alias(self):
        """ Tests the insertion of a `StudyAlias` record via the
            `iodi_study_alias` method of the `DalClinicalTrials` class and its
             retrieval via the get` method.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        alias_id, _ = create_alias(dal=self.dal)

        # IODI a new `StudyAlias` record.
        obj_id = self.dal.iodi_study_alias(
            study_id=study_id,
            alias_id=alias_id,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(StudyAlias, obj_id)  # type: StudyAlias

        # Assert that the different fields of the record match.
        self.assertEqual(obj.study_alias_id, 1)
        self.assertEqual(obj.study_id, study_id)
        self.assertEqual(obj.alias_id, alias_id)

    def test_iodi_study_alias_missing_fk(self):
        """ Tests the insertion of a `StudyAlias` record via the
            `iodi_study_alias` method when the required FK is non-existing.
        """

        self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            self.dal.iodi_study_alias,
            # This FK is invalid.
            study_id=123,
            alias_id=123,
        )

    def test_iodi_study_alias_duplicate(self):
        """ Tests the IODI insertion of duplicate `StudyAlias` records to ensure
            deduplication functions as intended.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        alias_id, _ = create_alias(dal=self.dal)
        alias_02_id, _ = create_alias(dal=self.dal, alias="new_alias")

        # IODI a new `StudyAlias` record.
        obj_id = self.dal.iodi_study_alias(
            study_id=study_id,
            alias_id=alias_id,
        )

        # The PK should be `1` as this is the first record.
        self.assertEqual(obj_id, 1)

        # IODI the same `StudyAlias` record as before.
        obj_id = self.dal.iodi_study_alias(
            study_id=study_id,
            alias_id=alias_id,
        )

        # The PK should still be `1` as the record was identical thus no
        # insertion should've occured.
        self.assertEqual(obj_id, 1)

        # IODI a new `StudyAlias` record.
        obj_id = self.dal.iodi_study_alias(
            study_id=study_id,
            alias_id=alias_02_id,
        )

        # The PK should be `3` as the previous failed INSERT will have
        # incremented the PK by 1.
        self.assertEqual(obj_id, 3)

        # IODU the same `StudyAlias` record as before.
        obj_id = self.dal.iodi_study_alias(
            study_id=study_id,
            alias_id=alias_02_id,
        )

        # The PK should still be `3` as the record is identical to the one
        # before.
        self.assertEqual(obj_id, 3)

    def test_delete_study_alias(self):
        """ Tests the deletion of a `StudyAlias` record via the `delete` method
            of the `DalClinicalTrials` class.
        """

        # Create fixtures.
        study_id, _ = create_study(dal=self.dal)
        alias_id, _ = create_alias(dal=self.dal)

        # IODI a new `StudyAlias` record.
        obj_id = self.dal.iodi_study_alias(
            study_id=study_id,
            alias_id=alias_id,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(StudyAlias, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(StudyAlias, obj_id)  # type: StudyAlias

        self.assertIsNone(obj)
