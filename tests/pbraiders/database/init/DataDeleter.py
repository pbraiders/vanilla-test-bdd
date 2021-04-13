# coding=utf-8
"""Delete all data in database"""

from dataclasses import dataclass
from pbraiders.database.adapter import PyMySQLAdapter


@dataclass
class DataDeleter:
    adapter: pbraiders.database.adapter.PyMySQLAdapter = None

    def execute(self):
        self.adapter.execute('truncate table `{d}`.`session`;')
        self.adapter.execute('truncate table `{d}`.`reservation`;')
        self.adapter.execute('truncate table `{d}`.`contact`;')
        self.adapter.execute('delete from `{d}`.`user` where login like 'test-%';')
