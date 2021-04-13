# coding=utf-8
"""Database"""

from dataclasses import dataclass
import pymysql
import pymysql.cursors

# https://pythontic.com/database/mysql/drop%20database
#https://www.programcreek.com/python/example/53260/pymysql.connect

@dataclass
class DbAdapter:
    host: str = 'localhost'
    port: str = 3306
    user: str = ''
    password: str = ''
    database: str = ''
    charset: str = 'utf8mb4'
    _pConnection: pymysql.connections.Connection = None

    # locators

    def __del__(self):
        self.quit()

    def connect(self) -> DbAdapter:
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
        return self

    def quit(self):
        if isinstance(self._pConnection, pymysql.connections.Connection):
            if self._pConnection.open:
                self._pConnection.close()
            del self._pConnection
        self._pConnection = None
        return self

    def deleteData(self) -> DbAdapter:
        try:
            with self._pConnection:
                with self._pConnection.cursor() as pCursor:
                    sSql = 'truncate table `{d}`.`session`;'.format(d=self.database)
                    pCursor.execute(sSql)
                    sSql = 'truncate table `{d}`.`reservation`;'.format(d=self.database)
                    pCursor.execute(sSql)
                    sSql = "delete from `{d}`.`contact`;".format(d=self.database)
                    pCursor.execute(sSql)
                    sSql = "delete from `{d}`.`user` where login like 'test-%';".format(d=self.database)
                    pCursor.execute(sSql)
                self._pConnection.commit()
        except Exception as e:
            print("Exception occured:{}".format(e))
        return self

    def deleteLog(self) -> DbAdapter:
        try:
            with self._pConnection:
                with self._pConnection.cursor() as pCursor:
                    sSql = 'truncate table `{d}`.`log`;'.format(d=self.database)
                    pCursor.execute(sSql)
                self._pConnection.commit()
        except Exception as e:
            print("Exception occured:{}".format(e))
        return self

    def insertUsersData(self, config: dict) -> DbAdapter:
        try:
            with self._pConnection:
                with self._pConnection.cursor() as pCursor:
                    sSql = 'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%s, %s, SYSDATE(), 10, NULL, 1);'.format(d=self.database)
                    pCursor.execute(sSql, (config['admin']['login'], config['admin']['password']))
                    sSql = 'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%s, %s, SYSDATE(), 0, NULL, 1);'.format(d=self.database)
                    pCursor.execute(sSql, (config['simple']['login'], config['simple']['password']))
                    sSql = 'insert into `{d}`.`user` (`login`, `password`, `registered`, `role`, `last_visit`, `state`) VALUES (%s, %s, SYSDATE(), 10, NULL, 0);'.format(d=self.database)
                    pCursor.execute(sSql, (config['disabled']['login'], config['disabled']['password']))
                self._pConnection.commit()
        except Exception as e:
            print("Exception occured:{}".format(e))
        return self
