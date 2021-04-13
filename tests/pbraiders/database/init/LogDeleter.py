# coding=utf-8
"""Delete log in database"""

from dataclasses import dataclass
from pbraiders.database.adapter import PyMySQLAdapter


@dataclass
class LogDeleter:
    adapter: pbraiders.database.adapter.PyMySQLAdapter = None

    def execute(self):
        self.adapter.execute('truncate table `{d}`.`log`;')
