# coding=utf-8
"""Factory used to create a database mapper."""

from pbraiders.database.adapter import AbstractAdapter
from pbraiders.database.adapter import AdapterFactory
from pbraiders.database.adapter import PyMySQLAdapter


class PyMySQLAdapterFactory(AdapterFactory):

    def create(self, config: dict) -> AbstractAdapter:
        return PyMySQLAdapter(
            user=config['credential']['user'],
            password=config['credential']['password'],
            host=config['host']['host'],
            database=config['host']['dbname'])
