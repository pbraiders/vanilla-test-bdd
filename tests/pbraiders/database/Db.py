# coding=utf-8
"""Database"""

from dataclasses import dataclass
import sqlalchemy
from sqlalchemy import create_engine


@dataclass
class Db:
    user: str = ''
    password: str = ''
    server: str = 'localhost'
    port: str = '3306'
    dbname: str = ''
    charset: str = 'utf8mb4'
    _pEngine: sqlalchemy.engine.Engine = None

    # locators
    _URL = "mysql+pymysql://{u}:{w}@{s}:{p}/{n}?charset={c}"

    def connect(self):
        self._pEngine = create_engine(self._URL.format(u=self.user, w=self.password, s=self.server,
                                                       p=self.port, n=self.dbname, c=self.charset))

    def quit(self):
        if isinstance(self._pEngine, sqlalchemy.engine.Engine):
            self._pEngine.dispose()
            del self._pEngine
