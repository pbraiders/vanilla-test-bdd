# coding=utf-8
"""User requesting a web page."""

from dataclasses import dataclass


@dataclass
class User:
    login: str
    password: str
    logouturl: str

    def signout(self, theBrowser):
        theBrowser.visit(logouturl)