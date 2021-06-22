# coding=utf-8
"""Fail to Create a new user feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.pages.options.users import UsersPage  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error
from pbraiders.pages.options.users.actions import CreateUserAction  # pylint: disable=import-error
from pbraiders.pages.options.users.actions import FillUserAction  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error

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
def page_users(the_config, the_browser, the_database) -> UsersPage:
    """I am on the users page."""
    p_page = UsersPage(_driver=the_browser, _config=the_config['urls'], _user=None)
    if p_page.on_page() is False:
        # Sign in as admin
        assert sign_in(driver=the_browser, config=the_config, user="admin") is True
        # Visit users page
        assert p_page.visit() is True
    return p_page


@when('I send the credential without the name')
def send_credential_without_name(page_users, new_user) -> None:
    """I send the credential without the name."""
    page_users.set_user(new_user)

    # Fill the fields
    p_action = FillUserAction(_page=page_users)
    p_action.fill_password() \
            .confirm_password()
    del p_action

    # Create
    p_action = CreateUserAction(_page=page_users)
    p_action.click()


@when('I send the credential without the password')
def send_credential_without_password(page_users, new_user) -> None:
    """I send the credential without the password."""
    page_users.set_user(new_user)

    # Fill the fields
    p_action = FillUserAction(_page=page_users)
    p_action.fill_name() \
            .confirm_password()
    del p_action

    # Create
    p_action = CreateUserAction(_page=page_users)
    p_action.click()


@when('I send the credential without the confirmed password')
def send_credential_without_confirmed_password(page_users, new_user) -> None:
    """I send the credential without the confirmed password."""
    page_users.set_user(new_user)

    # Fill the fields
    p_action = FillUserAction(_page=page_users)
    p_action.fill_name() \
            .fill_password()
    del p_action

    # Create
    p_action = CreateUserAction(_page=page_users)
    p_action.click()


@when('I send the credential of an already existing user')
def send_credential(the_config, page_users) -> None:
    """I send the credential of an already existing user."""
    page_users.set_user(UserSimpleFactory().initialize(the_config["data"]["users"]))

    # Fill the fields
    p_action = FillUserAction(_page=page_users)
    p_action.fill_name() \
            .fill_password() \
            .confirm_password()
    del p_action

    # Create
    p_action = CreateUserAction(_page=page_users)
    p_action.click()


@then('I should see the error message')
def error_message(page_users) -> None:
    """I should see the error message."""
    p_action = CreateUserAction(_page=page_users)
    assert p_action.has_failed() is True


@then('I should see the already exist error message')
def error_exist_message(page_users) -> None:
    """I should see the already exist error message."""
    p_action = CreateUserAction(_page=page_users)
    assert p_action.has_failed_exist() is True
