# coding=utf-8
"""Factory used to create a database mapper."""

from abc import ABC, abstractmethod
from pbraiders.database.Db import Db


class DbFactories(ABC):

    @abstractmethod
    def create(self, config: dict) -> Db:
        pass

    def initialize(self, configDB: dict, configUsers: dict) -> Db:
        pDB = self.create(configDB)
        pDB.connect()
        return pDB


class PyMySQLFactory(DbFactories):

    def create(self, config: dict) -> Db:
        return Db(
            user=config['credential']['user'],
            password=config['credential']['password'],
            host=config['host']['host'],
            database=config['host']['dbname'])
