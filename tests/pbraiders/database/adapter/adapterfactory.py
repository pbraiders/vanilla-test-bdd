# coding=utf-8
"""Factory used to create a database mapper."""

from abc import ABC, abstractmethod
from pbraiders.database.adapter import AbstractAdapter
from pbraiders.database.processor.init.teardown import Log


class AdapterFactory(ABC):

    @abstractmethod
    def create(self, config: dict) -> AbstractAdapter:
        pass

    def initialize(self, configDB: dict, configData: dict) -> AbstractAdapter:
        pDB = self.create(configDB)
        pDB.connect()
        # deleteLog().deleteData().insertData()
        return pDB
