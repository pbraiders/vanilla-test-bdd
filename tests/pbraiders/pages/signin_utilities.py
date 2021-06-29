# coding=utf-8
"""Sign in utilities."""

from splinter.driver import DriverAPI
from pbraiders.user import UserAdminFactory
from pbraiders.user import UserSimpleFactory
from pbraiders.user import UserClosedFactory
from pbraiders.user import UserDictFactory
from pbraiders.pages.signin import SigninPage
from pbraiders.pages.signin.actions import SigninAction


def sign_in(driver: DriverAPI, config: dict, user: str, password: str = '') -> bool:
    """Sign in.
        user= 'admin | simple | deactivated'"""
    switcher = {
        "admin": UserAdminFactory().initialize(config["data"]["users"]),
        "simple": UserSimpleFactory().initialize(config["data"]["users"]),
        "deactivated": UserClosedFactory().initialize(config["data"]["users"]),
    }
    d_user = {"login": user, "password": password}
    p_page = SigninPage(_driver=driver,
                        _config=config['urls'],
                        _user=switcher.get(user, UserDictFactory().initialize(d_user)))
    assert p_page.sign_out().visit() is True
    p_action = SigninAction(_page=p_page)
    p_action.fill_credential().click()
    return p_action.connected()
