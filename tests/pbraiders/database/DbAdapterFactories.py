# coding=utf-8
"""Factory used to create a database mapper."""

from abc import ABC, abstractmethod
from pbraiders.database.adapter import AbstractAdapter


class DbAdapterFactories(ABC):

    @abstractmethod
    def create(self, config: dict) -> AbstractAdapter:
        pass

    def initialize(self, configDB: dict, configUsers: dict) -> AbstractAdapter:
        pDB = self.create(configDB)
        # pDB.connect().deleteLog().deleteData().insertData()
        return pDB
