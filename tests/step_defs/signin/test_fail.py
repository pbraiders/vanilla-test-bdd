# coding=utf-8
"""Signin feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin import PageSignin
from pbraiders.user import AdminUserFactory

scenario = partial(scenario, 'signin/fail.feature')


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
def signin_page(the_browser, the_config, the_database):
    """I am on the signin page."""
    p_page = PageSignin(
        browser=the_browser, config=the_config['urls'],
        user=AdminUserFactory().initialize(the_config["data"]["users"]))
    p_page.visit()
    return p_page


@given('I fill the password field')
def fill_password(signin_page):
    """I fill the password field."""
    signin_page.fill_password()


@given('I fill the password field with the wrong password')
def fill_wrong_password(signin_page):
    """I fill the password field."""
    s_password = signin_page.user.password
    signin_page.user.password = s_password + ' wrong password'
    signin_page.fill_password()
    signin_page.user.password = s_password


@given('I fill the username field')
def fill_username(signin_page):
    """I fill the username field."""
    signin_page.fill_name()


@when('I press the connect button')
def connect(signin_page):
    """I press the connect button."""
    signin_page.click()


@then('I should see the error message')
def error_message(signin_page):
    """I should see the error message."""
    signin_page.has_failed()
