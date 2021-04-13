# coding=utf-8
"""PyMySQL adapter"""

from pbraiders.database.adapter import AbstractAdapter
import pymysql
import pymysql.cursors


class PyMySQLAdapter(AbstractAdapter):
    _pConnection: pymysql.connections.Connection = None

    def __del__(self):
        self.quit()

    def connect(self):
        self.quit()
        self._pConnection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset,
            cursorclass=pymysql.cursors.DictCursor
        )

    def quit(self):
        if isinstance(self._pConnection, pymysql.connections.Connection):
            if self._pConnection.open:
                self._pConnection.close()
            del self._pConnection
        self._pConnection = None

    def execute(self, query: str, args: dict = None):
        try:
            with self._pConnection:
                with self._pConnection.cursor() as pCursor:
                    sSql = query.format(d=self.database)
                    pCursor.execute(sSql, args)
                self._pConnection.commit()
        except Exception as e:
            print("Exception occured:{}".format(e))

#    def insertUsersData(self, config: dict) -> DbAdapter:
#        try:
#            with self._pConnection:
#                with self._pConnection.cursor() as pCursor:
#                    sSql = 'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%s, %s, SYSDATE(), 10, NULL, 1);'.format(
#                        d=self.database)
#                    pCursor.execute(sSql, (config['admin']['login'], config['admin']['password']))
#                    sSql = 'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%s, %s, SYSDATE(), 0, NULL, 1);'.format(
#                        d=self.database)
#                    pCursor.execute(sSql, (config['simple']['login'], config['simple']['password']))
#                    sSql = 'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%s, %s, SYSDATE(), 10, NULL, 0);'.format(
#                        d=self.database)
#                    pCursor.execute(sSql, (config['disabled']['login'], config['disabled']['password']))
#                self._pConnection.commit()
#        except Exception as e:
#            print("Exception occured:{}".format(e))
#        return self
