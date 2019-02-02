# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `DescriptorDefinition` class as well as
the `iodi_descriptor_definition` method of the `DalMesh` class.
"""

import hashlib

from fform.orm_mt import DescriptorDefinition
from fform.orm_mt import DescriptorDefinitionSourceType

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_qualifier
from tests.assets.items_mt import create_descriptor
from tests.assets.items_mt import create_entry_combination


class DalMtDescriptorDefinitionTest(DalMtTestBase):
    """ Defines unit-tests for the `DescriptorDefinition` class as well asthe
        `iodi_descriptor_definition` method of the `DalMesh` class.
    """

    def test_iodi_get_descriptor_definition(self):
        """ Tests the IODI insertion of a `DescriptorDefinition` record via the
            `iodi_descriptor_definition` method of the `DalMesh` class and its
            retrieval via the `get` method.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        definition = "definition"
        md5 = hashlib.md5(definition.encode("utf-8")).digest()

        # IODI a new `DescriptorDefinition` record.
        obj_id = self.dal.iodi_descriptor_definition(
            descriptor_id=descriptor_id,
            source=DescriptorDefinitionSourceType.AIR,
            definition=definition,
            md5=md5,
        )

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(
            DescriptorDefinition,
            obj_id,
        )  # type: DescriptorDefinition

        # Assert that the different fields of the record match.
        self.assertEqual(obj.descriptor_definition_id, 1)
        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertEqual(obj.source, DescriptorDefinitionSourceType.AIR)
        self.assertEqual(obj.definition, definition)
        self.assertEqual(obj.md5, md5)

    def test_iodi_descriptor_definition_duplicate(self):
        """ Tests the IODI insertion of duplicate `DescriptorDefinition` records
            to ensure deduplication functions as intended.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        definition = "definition"
        md5 = hashlib.md5(definition.encode("utf-8")).digest()
        definition_02 = "definition02"
        md5_02 = hashlib.md5(definition_02.encode("utf-8")).digest()

        # IODI a new `DescriptorDefinition` record.
        obj_id = self.dal.iodi_descriptor_definition(
            descriptor_id=descriptor_id,
            source=DescriptorDefinitionSourceType.AIR,
            definition=definition,
            md5=md5,
        )

        self.assertEqual(obj_id, 1)

        # IODI an identical `DescriptorDefinition` record.
        obj_id = self.dal.iodi_descriptor_definition(
            descriptor_id=descriptor_id,
            source=DescriptorDefinitionSourceType.AIR,
            definition=definition,
            md5=md5,
        )

        self.assertEqual(obj_id, 1)

        # IODI a new `DescriptorDefinition` record.
        obj_id = self.dal.iodi_descriptor_definition(
            descriptor_id=descriptor_id,
            source=DescriptorDefinitionSourceType.AIR,
            definition=definition_02,
            md5=md5_02,
        )

        self.assertEqual(obj_id, 3)

    def test_delete_descriptor_definition(self):
        """ Tests the deletion of a `DescriptorDefinition` record via the
            `delete` method of the `DalMesh` class.
        """

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)

        definition = "definition"
        md5 = hashlib.md5(definition.encode("utf-8")).digest()

        # IODI a new `DescriptorDefinition` record.
        obj_id = self.dal.iodi_descriptor_definition(
            descriptor_id=descriptor_id,
            source=DescriptorDefinitionSourceType.AIR,
            definition=definition,
            md5=md5,
        )

        self.assertEqual(obj_id, 1)

        # Delete the new record.
        self.dal.delete(DescriptorDefinition, obj_id)

        # (Attempt to) retrieve the deleted record.
        obj = self.dal.get(
            DescriptorDefinition,
            obj_id,
        )  # type: DescriptorDefinition

        self.assertIsNone(obj)
