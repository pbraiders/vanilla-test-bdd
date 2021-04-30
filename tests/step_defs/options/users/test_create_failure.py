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
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.options.users import PageUsers  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error
from pbraiders.user import User  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/create_failure.feature')


@scenario('Name is mandatory')
def test_name_is_mandatory() -> None:
    """Name is mandatory."""


@scenario('Password is mandatory')
def test_password_is_mandatory() -> None:
    """Password is mandatory."""


@scenario('Confirmed password is mandatory')
def test_confirmed_password_is_mandatory() -> None:
    """Confirmed password is mandatory."""


@scenario('User already exists')
def test_user_exists() -> None:
    """User already exists."""


@given('I am on the users page', target_fixture="page_users")
def page_users(the_config, the_browser, the_database) -> PageUsers:
    """I am on the users page."""
    p_page_users = PageUsers(
        browser=the_browser,
        config=the_config['urls'],
        user=None)
    if p_page_users.on_page() is False:
        # Sign in as admin
        p_page_signin = PageSignin(
            browser=the_browser,
            config=the_config['urls'],
            user=None)
        sign_in(
            p_page_signin,
            AdminUserFactory().initialize(
                the_config["data"]["users"]))
        del p_page_signin
        # Visit users page
        p_page_users.visit()
    return p_page_users


@when('I send the credential without the name')
def send_credential_without_name(page_users, new_user) -> None:
    """I send the credential without the name."""
    page_users.set_user(new_user).fill_password().confirm_password().click()


@when('I send the credential without the password')
def send_credential_without_password(page_users, new_user) -> None:
    """I send the credential without the password."""
    page_users.set_user(new_user).fill_name().confirm_password().click()


@when('I send the credential without the confirmed password')
def send_credential_without_confirmed_password(page_users, new_user) -> None:
    """I send the credential without the confirmed password."""
    page_users.set_user(new_user).fill_name().fill_password().click()


@when('I send the credential of an already existing user')
def send_credential(the_config, page_users) -> None:
    """I send the credential of an already existing user."""
    page_users.set_user(AdminUserFactory().initialize(
        the_config["data"]["users"])).fill_name().fill_password().confirm_password().click()


@then('I should see the error message')
def error_message(page_users) -> None:
    """I should see the error message."""
    assert page_users.has_failed() is True


@then('I should see the already exist error message')
def error_exist_message(page_users) -> None:
    """I should see the already exist error message."""
    assert page_users.has_failed_exist() is True
