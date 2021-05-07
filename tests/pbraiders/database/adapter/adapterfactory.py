# coding=utf-8
"""Factory used to create a database mapper."""

from abc import ABC, abstractmethod
from pbraiders.database.adapter import AbstractAdapter
from pbraiders.database.processor.init.teardown import Log as DeleteLog
from pbraiders.database.processor.init.teardown import Data as DeleteData
from pbraiders.database.processor.init.setup import Users as InsertUsers
from pbraiders.database.processor.init.setup import Config as InsertConfig
from pbraiders.database.processor.init.setup import Contacts as InsertContacts


class AdapterFactory(ABC):

    @abstractmethod
    def create(self, config: dict) -> AbstractAdapter:
        pass

    def initialize(self, configDB: dict, configData: dict) -> AbstractAdapter:
        pDB = self.create(configDB)
        DeleteLog(pDB).execute()
        DeleteData(pDB).execute()
        InsertUsers(pDB).execute(configData['users'])
        InsertConfig(pDB).execute(configData['config'])
        InsertContacts(pDB).execute(configData['contacts'])
        return pDB
