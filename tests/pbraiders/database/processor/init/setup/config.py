# coding=utf-8
"""Insert default users in database"""

from pbraiders.database.processor.abstract import AbstractProcessor


class Config(AbstractProcessor):

    def execute(self, config: dict):
        print('Inserting config')
        self._pAdapter.execute(u"delete from `{d}`.`config`;")
        self._pAdapter.executemany(
            u"insert into `{d}`.`config` (`name`, `value`, `role`) VALUES (%(name)s, %(value)s, %(role)s);",
            config)
