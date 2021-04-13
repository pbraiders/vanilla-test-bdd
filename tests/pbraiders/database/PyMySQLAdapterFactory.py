# coding=utf-8
"""Factory used to create a database mapper."""

from pbraiders.database import DbAdapterFactories
from pbraiders.database.adapter import AbstractAdapter, PyMySQLAdapter


class PyMySQLAdapterFactory(DbAdapterFactories):

    def create(self, config: dict) -> AbstractAdapter:
        return PyMySQLAdapter(
            user=config['credential']['user'],
            password=config['credential']['password'],
            host=config['host']['host'],
            database=config['host']['dbname'])
