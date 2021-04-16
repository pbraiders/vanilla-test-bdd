# coding=utf-8
"""Signin feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin.PageSignin import PageSignin
from pbraiders.signin.UserFactories import AdminUserFactory

scenario = partial(scenario, 'signin/signin.feature')


@scenario('I have no credentials')
def test_no_credentials():
    """I have no credentials."""


@scenario('I have no password')
def test_no_password():
    """I have no password."""


@scenario('I have no username')
def test_no_username():
    """I have no username."""


@scenario('I have a wrong password')
def test_wrong_password():
    """I have a wrong password."""


@given('I am on the signin page', target_fixture="signin_page")
def signin_page(theBrowser, theConfig, theDB):
    """I am on the signin page."""
    pPage = PageSignin(
        browser=theBrowser, config=theConfig['urls'],
        user=AdminUserFactory().initialize(theConfig["data"]["users"]))
    pPage.visit()
    return pPage


@given('I fill the password field')
def fill_password(signin_page):
    """I fill the password field."""
    signin_page.fillPassword()


@given('I fill the password field with the wrong password')
def fill_wrong_password(signin_page):
    """I fill the password field."""
    sPassword = signin_page.user.password
    signin_page.user.password = sPassword + ' wrong password'
    signin_page.fillPassword()
    signin_page.user.password = sPassword


@given('I fill the username field')
def fill_username(signin_page):
    """I fill the username field."""
    signin_page.fillName()


@when('I press the connect button')
def connect(signin_page):
    """I press the connect button."""
    signin_page.click()


@then('I should see the error message')
def error_message(signin_page):
    """I should see the error message."""
    signin_page.hasFail()
