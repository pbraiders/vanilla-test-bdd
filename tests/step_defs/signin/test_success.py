# coding=utf-8
"""Successful signin feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.pages.signin import SigninPage  # pylint: disable=import-error
from pbraiders.pages.signin.actions import SigninAction  # pylint: disable=import-error
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error
from pbraiders.user import UserClosedFactory  # pylint: disable=import-error
from pbraiders.user import User  # pylint: disable=import-error

scenario = partial(scenario, 'signin/success.feature')


@scenario('Sign in', example_converters=dict(type=str, permission=str))
def test_sign_in() -> None:
    """Sign in."""


@given('I am the <type> user', target_fixture="type_user")
def type_user(the_config, type) -> User:
    """I am the <type> user."""
    assert isinstance(type, str)
    switcher = {
        "admin": UserAdminFactory().initialize(the_config["data"]["users"]),
        "simple": UserSimpleFactory().initialize(the_config["data"]["users"]),
        "deactivated": UserClosedFactory().initialize(the_config["data"]["users"]),
    }
    return switcher.get(type, UserClosedFactory().initialize(the_config["data"]["users"]))


@when('I sign in to the app')
def access_page(the_config, the_browser, type_user) -> None:
    """I sign in to the app."""
    p_page = SigninPage(_driver=the_browser, _config=the_config['urls'], _user=type_user)
    assert p_page.sign_out().visit() is True
    p_action = SigninAction(_page=p_page)
    p_action.fill_credential().click()


@then('I <permission> access to the main page')
def permission(the_config, the_browser, type_user, permission) -> None:
    """I <permission> access to the main page."""
    assert isinstance(permission, str)
    p_page = SigninPage(_driver=the_browser, _config=the_config['urls'], _user=type_user)
    p_action = SigninAction(_page=p_page)
    if permission.lower() == 'can':
        assert p_action.connected() is True
    else:
        assert p_action.connected() is False
        assert p_action.has_failed() is True
