# coding=utf-8
"""Delete all data in database"""

from dataclasses import dataclass
from pbraiders.database.adapter import AbstractAdapter


@dataclass
class Data:
    _pAdapter: pbraiders.database.adapter.AbstractAdapter = None

    def execute(self):
        self._pAdapter.execute('truncate table `{d}`.`session`;')
        self._pAdapter.execute('truncate table `{d}`.`reservation`;')
        self._pAdapter.execute('truncate table `{d}`.`contact`;')
        self._pAdapter.execute('delete from `{d}`.`user` where login like "test-%";')
