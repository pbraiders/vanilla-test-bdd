# coding=utf-8
"""Delete all data in database"""

from pbraiders.database.processor.abstract import AbstractProcessor


class Data(AbstractProcessor):

    def execute(self, config: dict = None):
        print('Deleting tables')
        self._pAdapter.execute('truncate table `{d}`.`session`;')
        self._pAdapter.execute('truncate table `{d}`.`reservation`;')
        self._pAdapter.execute('delete from `{d}`.`contact`;')
        self._pAdapter.execute('alter table `{d}`.`contact` AUTO_INCREMENT=1;')
        self._pAdapter.execute('delete from `{d}`.`user` where iduser>1;')
        self._pAdapter.execute('alter table `{d}`.`user` AUTO_INCREMENT=2;')
