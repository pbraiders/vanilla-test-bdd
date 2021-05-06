# coding=utf-8
"""Delete all logs in database"""

from pbraiders.database.processor.abstract import AbstractProcessor


class Log(AbstractProcessor):

    def execute(self, config: dict = None):
        print('\n' + 'Deleting Log')
        self._pAdapter.execute('truncate table `{d}`.`log`;')
