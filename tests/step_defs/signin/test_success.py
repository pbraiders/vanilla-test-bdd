# coding=utf-8
"""Successful Signin feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin import PageSignin
from pbraiders.user import AdminUserFactory
from pbraiders.user import SimpleUserFactory
from pbraiders.user import DisabledUserFactory

scenario = partial(scenario, 'signin/success.feature')


@scenario('Connecting', example_converters=dict(type=str))
def test_connecting():
    """Connecting."""


@scenario('Connect deactivated')
def test_deactivated():
    """Connect deactivated."""


@given('I am the deactivated user', target_fixture="signin_page")
def signin_page(the_browser, the_config, the_database):
    """I am the deactivated user."""
    p_page = PageSignin(
        browser=the_browser, config=the_config['urls'],
        user=DisabledUserFactory().initialize(the_config["data"]["users"]))
    p_page.visit()
    return p_page


@given('I am the <type> user', target_fixture="signin_page")
def signin_page(type, the_browser, the_config, the_database):
    """I am the <type> user."""
    assert isinstance(type, str)
    # Create the user
    switcher = {
        "admin": AdminUserFactory().initialize(the_config["data"]["users"]),
        "simple": SimpleUserFactory().initialize(the_config["data"]["users"]),
        "deactivated": DisabledUserFactory().initialize(the_config["data"]["users"]),
    }
    p_user = switcher.get(type, None)
    # Create the page
    p_page = PageSignin(
        browser=the_browser, config=the_config['urls'],
        user=p_user)
    p_page.visit()
    return p_page


@when('I fill the credentials')
def fill_the_credentials(signin_page):
    """I fill the credentials."""
    signin_page.fill_name()
    signin_page.fill_password()
    signin_page.click()


@then('I should be connected')
def connected(signin_page):
    """I should be connected."""
    assert signin_page.connected() is True


@then('I should not be connected')
def not_connected(signin_page):
    """I should not be connected."""
    signin_page.has_failed()
