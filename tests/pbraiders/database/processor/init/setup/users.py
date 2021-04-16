# coding=utf-8
"""Insert default users in database"""

import copy
import hashlib
from pbraiders.database.processor import AbstractProcessor


class Users(AbstractProcessor):

    def execute(self, config: dict):
        print('Inserting users')
        # Encrypt password with SHA1
        theUsers = copy.deepcopy(config)
        theUsers['admin']['password'] = hashlib.sha1(theUsers['admin']['password'].encode()).hexdigest()
        theUsers['simple']['password'] = hashlib.sha1(theUsers['simple']['password'].encode()).hexdigest()
        theUsers['disabled']['password'] = hashlib.sha1(theUsers['disabled']['password'].encode()).hexdigest()

        self._pAdapter.executemany(
            'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%(login)s, %(password)s, SYSDATE(), %(role)s, NULL, %(state)s);',
            [theUsers['admin'], theUsers['simple'], theUsers['disabled']])
