# coding=utf-8
"""Sign in utilities."""

from splinter.driver import DriverAPI
from pbraiders.user import User
from pbraiders.pages.signin import SigninPage
from pbraiders.pages.signin.actions import SigninAction


def sign_in(driver: DriverAPI, config: dict, user: User) -> None:
    """Sign in."""
    p_page = SigninPage(_driver=driver, _config=config, _user=user)
    assert p_page.sign_out().visit() is True
    p_action = SigninAction(_page=p_page)
    p_action.fill_credential().click()
    assert p_action.connected() is True
