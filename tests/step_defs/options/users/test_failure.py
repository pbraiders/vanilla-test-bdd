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

scenario = partial(scenario, 'options/users/failure.feature')


@scenario('Name is mandatory')
def test_name_is_mandatory():
    """Name is mandatory."""


@scenario('Password is mandatory')
def test_password_is_mandatory():
    """Password is mandatory."""


@scenario('Confirmed password is mandatory')
def test_confirmed_password_is_mandatory():
    """Confirmed password is mandatory."""


@scenario('User already exists')
def test_user_exists():
    """User already exists."""


@given('I am on the users page', target_fixture="page_users")
def page_users(the_config, the_browser, the_database) -> PageUsers:
    """I am on the users page."""
    p_pageusers = PageUsers(
        browser=the_browser,
        config=the_config['urls'],
        user=None)
    if p_pageusers.on_page() is False:
        # Sign in
        p_pagesignin = PageSignin(
            browser=the_browser, config=the_config['urls'],
            user=AdminUserFactory().initialize(the_config["data"]["users"]))
        p_pagesignin.connect_success()
        del p_pagesignin
        # Visit users page
        p_pageusers.visit()
    return p_pageusers


@given('I have a new user to create', target_fixture="new_user")
def new_user(the_faker) -> User:
    """I have a new user to create."""
    # Generate test data
    s_name = the_faker.first_name()
    s_passwd = s_name + 'password'
    return User(login=s_name, password=s_passwd, passwordc=s_passwd)


@when('I send the credential without the name')
def send_credential_without_name(page_users, new_user):
    """I send the credential without the name."""
    page_users.set_user(new_user).fill_password().confirm_password().click()


@when('I send the credential without the password')
def send_credential_without_password(page_users, new_user):
    """I send the credential without the password."""
    page_users.set_user(new_user).fill_name().confirm_password().click()


@when('I send the credential without the confirmed password')
def send_credential_without_confirmed_password(page_users, new_user):
    """I send the credential without the confirmed password."""
    page_users.set_user(new_user).fill_name().fill_password().click()


@when('I send the credential of an already existing user')
def send_credential(the_config, page_users):
    """I send the credential of an already existing user."""
    page_users.set_user(AdminUserFactory().initialize(
        the_config["data"]["users"])).fill_name().fill_password().confirm_password().click()


@then('I should see the error message')
def error_message(page_users):
    """I should see the error message."""
    assert page_users.has_failed() is True


@then('I should see the already exist error message')
def error_exist_message(page_users):
    """I should see the already exist error message."""
    assert page_users.has_failed_exist() is True
