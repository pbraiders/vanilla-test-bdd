# coding=utf-8
"""Delete all logs in database"""

from dataclasses import dataclass
from pbraiders.database.adapter import AbstractAdapter


@dataclass
class Log:
    _pAdapter: pbraiders.database.adapter.AbstractAdapter = None

    def execute(self):
        self._pAdapter.execute('truncate table `{d}`.`log`;')
