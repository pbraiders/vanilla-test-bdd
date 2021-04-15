# coding=utf-8
"""Delete all logs in database"""

from pbraiders.database.processor import AbstractProcessor


class Log(AbstractProcessor):

    def execute(self, config: dict = None):
        self._pAdapter.execute('truncate table `{d}`.`log`;')
