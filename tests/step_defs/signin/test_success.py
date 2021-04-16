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
def signin_page(theBrowser, theConfig, theDB):
    """I am the deactivated user."""
    pPage = PageSignin(
        browser=theBrowser, config=theConfig['urls'],
        user=DisabledUserFactory().initialize(theConfig["data"]["users"]))
    pPage.visit()
    return pPage


@given('I am the <type> user', target_fixture="signin_page")
def signin_page(type, theBrowser, theConfig, theDB):
    """I am the <type> user."""
    assert isinstance(type, str)
    # Create the user
    switcher = {
        "admin": AdminUserFactory().initialize(theConfig["data"]["users"]),
        "simple": SimpleUserFactory().initialize(theConfig["data"]["users"]),
        "deactivated": DisabledUserFactory().initialize(theConfig["data"]["users"]),
    }
    pUser = switcher.get(type, None)
    # Create the page
    pPage = PageSignin(
        browser=theBrowser, config=theConfig['urls'],
        user=pUser)
    pPage.visit()
    return pPage


@when('I fill the credentials')
def fill_the_credentials(signin_page):
    """I fill the credentials."""
    signin_page.fillName()
    signin_page.fillPassword()
    signin_page.click()


@then('I should be connected')
def connected(signin_page):
    """I should be connected."""
    assert True == signin_page.connected()


@then('I should not be connected')
def not_connected(signin_page):
    """I should not be connected."""
    signin_page.hasFail()
