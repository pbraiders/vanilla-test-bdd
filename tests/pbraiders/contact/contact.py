# coding=utf-8
"""Contact."""

from dataclasses import dataclass


@dataclass
class User(object):
    login: str = ''
    password: str = ''
    passwordc: str = ''
