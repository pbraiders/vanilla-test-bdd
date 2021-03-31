# coding=utf-8
"""Creating a new user feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

scenario = partial(scenario, 'users/create_new_user.feature')


@scenario('Confirmed password is mandatory when creating user')
def test_confirmed_password_is_mandatory_when_creating_user():
    """Confirmed password is mandatory when creating user."""


@scenario('Creating a new user')
def test_creating_a_new_user():
    """Creating a new user."""


@scenario('Name is mandatory when creating user')
def test_name_is_mandatory_when_creating_user():
    """Name is mandatory when creating user."""


@scenario('Password is mandatory when creating user')
def test_password_is_mandatory_when_creating_user():
    """Password is mandatory when creating user."""


@given('I am logged in as the administrator')
def sign_in_as_admin(theBrowser, theConfig):
    theBrowser.visit(theConfig['urls']['home'])
    pInput = theBrowser.find_by_id("loginusr").first
    pInput.fill(theConfig['users']['admin']['login'])
    pInput = theBrowser.find_by_id("loginpwd").first
    pInput.fill(theConfig['users']['admin']['password'])
    pInput = theBrowser.find_by_name("login").first
    pInput.click()
    assert theBrowser.is_text_present(f"Connecté en tant que {theConfig['users']['admin']['login']}") == 1


@given('I am on the users page')
def users_page(theBrowser, theConfig):
    theBrowser.visit(theConfig['urls']['users'])


@given('I confirm the password')
def i_confirm_the_password():
    """I confirm the password."""
    pass  # raise NotImplementedError


@given('I confirm the password field')
def i_confirm_the_password_field():
    """I confirm the password field."""
    pass  # raise NotImplementedError


@given('I fill the password field')
def i_fill_the_password_field():
    """I fill the password field."""
    pass  # raise NotImplementedError


@given('I fill the username field')
def i_fill_the_username_field():
    """I fill the username field."""
    pass  # raise NotImplementedError


@when('I press the send button')
def i_press_the_send_button():
    """I press the send button."""
    pass  # raise NotImplementedError


@then('I should see the activated user on the list')
def i_should_see_the_activated_user_on_the_list():
    """I should see the activated user on the list."""
    pass  # raise NotImplementedError


@then('I should see the error message')
def i_should_see_the_error_message():
    """I should see the error message."""
    pass  # raise NotImplementedError


@then('I should see the success message')
def i_should_see_the_success_message():
    """I should see the success message."""
    pass  # raise NotImplementedError
