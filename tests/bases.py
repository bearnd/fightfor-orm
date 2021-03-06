# -*- coding: utf-8 -*-

import abc
import unittest

from fform.dals_ct import DalClinicalTrials
from fform.dals_pubmed import DalPubmed
from fform.dals_mt import DalMesh
from fform.dals_app import DalApp
from fform.orm_base import Base

from tests.utils import load_config


class DalTestBase(unittest.TestCase):

    def setUp(self):
        """Instantiates the DAL and creates the schema."""

        # Load the configuration.
        self.cfg = load_config(
            filename_config="/etc/fightfor-orm/fightfor-orm-test.json",
        )

        self.dal = self.setup_dal()

        # Drop any schema remnants and recreate it.
        Base.metadata.drop_all(self.dal.engine)
        Base.metadata.create_all(self.dal.engine)

    def tearDown(self):
        """Drops the DB schema created during setup."""

        Base.metadata.drop_all(self.dal.engine)

    @abc.abstractmethod
    def setup_dal(self):
        raise NotImplementedError


class DalCtTestBase(DalTestBase):

    def setup_dal(self) -> DalClinicalTrials:
        # Instantiate a DAL.
        dal = DalClinicalTrials(
            sql_username=self.cfg.sql_username,
            sql_password=self.cfg.sql_password,
            sql_host=self.cfg.sql_host,
            sql_port=self.cfg.sql_port,
            sql_db=self.cfg.sql_db
        )

        return dal


class DalPubmedTestBase(DalTestBase):

    def setup_dal(self) -> DalPubmed:
        # Instantiate a DAL.
        dal = DalPubmed(
            sql_username=self.cfg.sql_username,
            sql_password=self.cfg.sql_password,
            sql_host=self.cfg.sql_host,
            sql_port=self.cfg.sql_port,
            sql_db=self.cfg.sql_db
        )

        return dal


class DalMtTestBase(DalTestBase):

    def setup_dal(self) -> DalMesh:
        # Instantiate a DAL.
        dal = DalMesh(
            sql_username=self.cfg.sql_username,
            sql_password=self.cfg.sql_password,
            sql_host=self.cfg.sql_host,
            sql_port=self.cfg.sql_port,
            sql_db=self.cfg.sql_db
        )

        return dal


class DalAppTestBase(DalTestBase):

    def setup_dal(self) -> DalApp:
        # Instantiate a DAL.
        dal = DalApp(
            sql_username=self.cfg.sql_username,
            sql_password=self.cfg.sql_password,
            sql_host=self.cfg.sql_host,
            sql_port=self.cfg.sql_port,
            sql_db=self.cfg.sql_db
        )

        return dal
