# coding=utf-8
"""Creating a new user feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin.PageSignin import PageSignin
from pbraiders.signin.UserFactories import AdminFactory

scenario = partial(scenario, 'users/create_new_user.feature')


@scenario('Name is mandatory when creating user')
def test_name_is_mandatory_when_creating_user():
    """Name is mandatory when creating user."""


@given('I am logged in as the administrator')
def sign_in_as_administrator(theBrowser, theConfig):
    """I am logged in as the administrator."""
    PageSignin(browser=theBrowser, config=theConfig['urls'], user=AdminFactory().initialize(theConfig)).connectSuccess()


@ given('I am on the users page')
def i_am_on_the_users_page():
    """I am on the users page."""
    raise NotImplementedError


@ given('I confirm the password')
def i_confirm_the_password():
    """I confirm the password."""
    raise NotImplementedError


@ given('I fill the password field')
def i_fill_the_password_field():
    """I fill the password field."""
    raise NotImplementedError


@ when('I press the send button')
def i_press_the_send_button():
    """I press the send button."""
    raise NotImplementedError


@ then('I should see the error message')
def i_should_see_the_error_message():
    """I should see the error message."""
    raise NotImplementedError
