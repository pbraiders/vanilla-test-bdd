# coding=utf-8
"""Signin failure feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error
from pbraiders.pages.signin import SigninPage  # pylint: disable=import-error
from pbraiders.pages.signin.actions import SigninAction  # pylint: disable=import-error

scenario = partial(scenario, 'signin/failure.feature')


@scenario('Credential is mandatory')
def test_no_credentials() -> None:
    """Credential is mandatory."""


@scenario('Name is mandatory')
def test_no_name() -> None:
    """Name is mandatory."""


@scenario('Password is mandatory')
def test_no_password() -> None:
    """Password is mandatory."""


@scenario('Right password is mandatory')
def test_wrong_password() -> None:
    """Right password is mandatory."""


@given('I am on the signin page', target_fixture="page_signin")
def page_signin(the_browser, the_config, the_database) -> SigninPage:
    """I am on the signin page."""
    p_page = SigninPage(_driver=the_browser, _config=the_config['urls'], _user=None)
    if p_page.on_page() is False:
        assert p_page.visit() is True
    return p_page


@when('I send no credential')
def connect(page_signin) -> None:
    """I press the connect button."""
    p_action = SigninAction(_page=page_signin)
    p_action.click()


@when('I send the credential without the name')
def send_without_name(the_config, page_signin) -> None:
    """I send the credential without the name."""
    p_user = UserAdminFactory().initialize(the_config["data"]["users"])
    p_user.login = ''
    page_signin.set_user(p_user)
    p_action = SigninAction(_page=page_signin)
    p_action.fill_password().click()


@when('I send the credential without the password')
def send_without_password(the_config, page_signin) -> None:
    """I send the credential without the password."""
    p_user = UserAdminFactory().initialize(the_config["data"]["users"])
    p_user.password = ''
    page_signin.set_user(p_user)
    p_action = SigninAction(_page=page_signin)
    p_action.fill_name().click()


@when('I send the credential with a wrong password')
def send_wrong_password(the_config, page_signin) -> None:
    """I send the credential with a wrong password."""
    p_user = UserAdminFactory().initialize(the_config["data"]["users"])
    p_user.password = p_user.password + ' wrong password'
    page_signin.set_user(p_user)
    p_action = SigninAction(_page=page_signin)
    p_action.fill_credential().click()


@then('I should see the error message')
def error_message(page_signin) -> None:
    """I should see the error message."""
    p_action = SigninAction(_page=page_signin)
    assert p_action.has_failed() is True
