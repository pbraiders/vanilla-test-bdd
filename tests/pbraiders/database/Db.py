# coding=utf-8
"""Database"""

from dataclasses import dataclass
import pymysql
import pymysql.cursors


@dataclass
class Db:
    host: str = 'localhost'
    port: str = 3306
    user: str = ''
    password: str = ''
    database: str = ''
    charset: str = 'utf8mb4'
    _pConnection: pymysql.connections.Connection = None

    # locators

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
            self._pConnection.close()
            del self._pConnection
        self._pConnection = None

    def deleteData(self):
        with self._pConnection:
            with self._pConnection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self._pConnection.commit()
