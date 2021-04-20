# coding=utf-8
"""User requesting a web page."""

from dataclasses import dataclass


@dataclass
class User(object):
    login: str = ''
    password: str = ''
    passwordc: str = ''
