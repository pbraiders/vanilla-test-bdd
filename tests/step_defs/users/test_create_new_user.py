# coding=utf-8
"""Creating a new user feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('users/create_new_user.feature', 'Confirmed password is mandatory when creating user')
def test_confirmed_password_is_mandatory_when_creating_user():
    """Confirmed password is mandatory when creating user."""


@scenario('users/create_new_user.feature', 'Creating a new user')
def test_creating_a_new_user():
    """Creating a new user."""


@scenario('users/create_new_user.feature', 'Name is mandatory when creating user')
def test_name_is_mandatory_when_creating_user():
    """Name is mandatory when creating user."""


@scenario('users/create_new_user.feature', 'Password is mandatory when creating user')
def test_password_is_mandatory_when_creating_user():
    """Password is mandatory when creating user."""


@given('I am logged in as the administrator')
def i_am_logged_in_as_the_administrator():
    """I am logged in as the administrator."""
    raise NotImplementedError


@given('I am on the users page')
def i_am_on_the_users_page():
    """I am on the users page."""
    raise NotImplementedError


@given('I confirm the password')
def i_confirm_the_password():
    """I confirm the password."""
    raise NotImplementedError


@given('I confirm the password field')
def i_confirm_the_password_field():
    """I confirm the password field."""
    raise NotImplementedError


@given('I fill the password field')
def i_fill_the_password_field():
    """I fill the password field."""
    raise NotImplementedError


@given('I fill the username field')
def i_fill_the_username_field():
    """I fill the username field."""
    raise NotImplementedError


@when('I press the send button')
def i_press_the_send_button():
    """I press the send button."""
    raise NotImplementedError


@then('I should see the activated user on the list')
def i_should_see_the_activated_user_on_the_list():
    """I should see the activated user on the list."""
    raise NotImplementedError


@then('I should see the error message')
def i_should_see_the_error_message():
    """I should see the error message."""
    raise NotImplementedError


@then('I should see the success message')
def i_should_see_the_success_message():
    """I should see the success message."""
    raise NotImplementedError

