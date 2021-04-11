# coding=utf-8
"""Factory used to create a database mapper."""

from abc import ABC, abstractmethod
from pbraiders.database.Db import Db


class DbFactories(ABC):

    @abstractmethod
    def create(self, config: dict) -> Db:
        pass

    def initialize(self, config: dict) -> Db:
        pDB = self.create(config['db'])
        pDB.connect()
        return pDB


class SqlAlchemyFactory(DbFactories):

    def create(self, config: dict) -> Db:
        return Db(
            user=config['user'],
            password=config['password'],
            server=config['server'],
            dbname=config['dbname'])
