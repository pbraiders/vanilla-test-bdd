# coding=utf-8
"""Insert default users in database"""

import hashlib
from pbraiders.database.processor import AbstractProcessor


class Users(AbstractProcessor):

    def encrypt(self, config: dict):
        config['password'] = hashlib.sha1(config['password'].encode()).hexdigest()

    def execute(self, config: dict):
        # Encrypt password wiht SHA1
        self.encrypt(config['admin'])
        self.encrypt(config['simple'])
        self.encrypt(config['disabled'])

        self._pAdapter.executemany(
            'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%(login)s, %(password)s, SYSDATE(), %(role)s, NULL, %(state)s);',
            [config['admin'], config['simple'], config['disabled']])
