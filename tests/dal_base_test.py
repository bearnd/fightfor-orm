# -*- coding: utf-8 -*-

"""
This module defines unit-tests for the `Dalbase` class and its different
methods.
"""

from fform.orm_mt import Descriptor

from tests.bases import DalMtTestBase
from tests.assets.items_mt import create_tree_number
from tests.assets.items_mt import create_concept
from tests.assets.items_mt import create_descriptor


class DalBase(DalMtTestBase):

    def test_get(self):
        """ Tests the `get` method."""

        # Create a new `Descriptor` record.
        obj_id, refr = create_descriptor(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get(orm_class=Descriptor, pk=obj_id)  # type: Descriptor

        self.assertEqual(obj.descriptor_id, obj_id)

    def test_get_by_attr(self):
        """ Tests the `get_by_attr` method."""

        # Create a new `Descriptor` record.
        obj_id, refr = create_descriptor(dal=self.dal)

        self.assertEqual(obj_id, 1)

        # Retrieve the new record.
        obj = self.dal.get_by_attr(
            orm_class=Descriptor,
            attr_name="ui",
            attr_value=refr["ui"],
        )  # type: Descriptor

        self.assertEqual(obj.descriptor_id, obj_id)
        self.assertEqual(obj.ui, refr["ui"])

    def test_bget_by_attr(self):
        """ Tests the `bget_by_attr` method."""

        # Create two new `Descriptor` records.
        descriptor_01_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI1",
            name="Name01",
            annotation="annotation",
        )
        descriptor_02_id, _ = create_descriptor(
            dal=self.dal,
            ui="UI2",
            name="Name02",
            annotation="annotation",
        )

        # Retrieve a single record with the `bget_by_attr` method.
        objs = self.dal.bget_by_attr(
            orm_class=Descriptor,
            attr_name="ui",
            attr_values=["UI1"],
        )  # type: Descriptor

        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].descriptor_id, descriptor_01_id)
        self.assertEqual(objs[0].ui, "UI1")

        # Retrieve both records with the `bget_by_attr` method.
        objs = self.dal.bget_by_attr(
            orm_class=Descriptor,
            attr_name="annotation",
            attr_values=["annotation"],
        )  # type: Descriptor

        self.assertEqual(len(objs), 2)

    def test_get_joined_single_relationship(self):
        """ Tests the `get_joined` method with a single relationship."""

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        tree_number_id, _ = create_tree_number(dal=self.dal)

        # IODI a new `DescriptorTreeNumber` record.
        self.dal.iodi_descriptor_tree_number(
            descriptor_id=descriptor_id,
            tree_number_id=tree_number_id,
        )

        # Retrieve the `Descriptor` join-loaded with its `TreeNumber` record.
        obj = self.dal.get_joined(
            orm_class=Descriptor,
            pk=descriptor_id,
            joined_relationships=["tree_numbers"]
        )  # type: Descriptor

        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertIsNotNone(obj.tree_numbers)

    def test_get_joined_mutliple_relationship(self):
        """ Tests the `get_joined` method with multiple relationships."""

        # Create fixture records.
        descriptor_id, _ = create_descriptor(dal=self.dal)
        tree_number_id, _ = create_tree_number(dal=self.dal)
        concept_id, _ = create_concept(dal=self.dal)

        # IODI a new `DescriptorTreeNumber` record.
        self.dal.iodi_descriptor_tree_number(
            descriptor_id=descriptor_id,
            tree_number_id=tree_number_id,
        )

        # IODU a new `DescriptorConcept` record.
        self.dal.iodu_descriptor_concept(
            descriptor_id=descriptor_id,
            concept_id=concept_id,
            is_preferred=True,
        )

        # Retrieve the `Descriptor` join-loaded with its `TreeNumber` and
        # `Concept` record.
        obj = self.dal.get_joined(
            orm_class=Descriptor,
            pk=descriptor_id,
            joined_relationships=["tree_numbers", "concepts"]
        )  # type: Descriptor

        self.assertEqual(obj.descriptor_id, descriptor_id)
        self.assertIsNotNone(obj.tree_numbers)
        self.assertIsNotNone(obj.concepts)
