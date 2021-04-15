# coding=utf-8
"""Insert default user in database"""

from dataclasses import dataclass
from pbraiders.database.adapter import AbstractAdapter


@dataclass
class Users:
    _pAdapter: pbraiders.database.adapter.AbstractAdapter = None

    def execute(self, config: dict):
        self._pAdapter.executemany(
            'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%(login)s, %(password)s, SYSDATE(), %(role)s, NULL, %(state)s);',
            [config['admin'], config['simple'], config['disabled']])
