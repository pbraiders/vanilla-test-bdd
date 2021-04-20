# coding=utf-8
"""Fail to Create a new user feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.options.users import PageUsers  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error
from pbraiders.user import User  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/create_fail.feature')


@scenario('Name is mandatory when creating user')
def test_name_is_mandatory():
    """Name is mandatory when creating user."""


@scenario('Password is mandatory when creating user')
def test_password_is_mandatory():
    """Password is mandatory when creating user."""


@scenario('Confirmed password is mandatory when creating user')
def test_confirmed_password_is_mandatory():
    """Confirmed password is mandatory when creating user."""


@given('I am on the users page', target_fixture="users_page")
def users_page(the_config, the_browser, the_database, the_faker):
    """I am on the users page."""
    # Sign in
    p_page = PageSignin(
        browser=the_browser, config=the_config['urls'],
        user=AdminUserFactory().initialize(the_config["data"]["users"]))
    p_page.connect_success()
    del p_page
    # Generate test data
    s_name = the_faker.first_name()
    s_passwd = s_name + 'password'
    # Visit users page
    p_page = PageUsers(
        browser=the_browser,
        config=the_config['urls'],
        user=User(login=s_name, password=s_passwd, passwordc=s_passwd))
    p_page.visit()
    return p_page


@given('I enter the credential but not the confirmed password')
def credential_without_confirmed_password(users_page):
    """I enter the credential but not the confirmed password."""
    users_page.fill_name().fill_password()


@given('I enter the credential but not the password')
def credential_without_password(users_page):
    """I enter the credential but not the password."""
    users_page.fill_name().confirm_password()


@given('I enter the credential but not the name')
def creadential_without_name(users_page):
    """I enter the credential but not the name."""
    users_page.fill_password().confirm_password()


@when('I press the send button')
def send_button(users_page):
    """I press the send button."""
    users_page.click()


@then('I should see the error message')
def error_message(users_page):
    """I should see the error message."""
    assert users_page.has_failed() is True
