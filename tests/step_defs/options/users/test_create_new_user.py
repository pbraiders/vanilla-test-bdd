# coding=utf-8
"""Creating a new user feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory
from pbraiders.options.users.PageUsers import PageUsers

scenario = partial(scenario, 'options/users/create_new_user.feature')


@scenario('Name is mandatory when creating user')
def test_name_is_mandatory():
    """Name is mandatory when creating user."""


@given('I am on the users page', target_fixture="users_page")
def users_page(the_config, the_browser, the_database):
    """I am on the users page."""
    pPage = PageSignin(
        browser=the_browser, config=the_config['urls'],
        user=AdminUserFactory().initialize(the_config["data"]["users"]))
    pPage.connectSuccess()
    del pPage
    pPage = PageUsers(browser=the_browser, config=the_config['urls'])
    pPage.visit()
    assert the_browser.title == 'PBRaiders - Utilisateurs'
    return pPage


@given('I confirm the password')
def confirm_password():
    """I confirm the password."""
    raise NotImplementedError


@given('I fill the password field')
def i_fill_the_password_field():
    """I fill the password field."""
    raise NotImplementedError


@when('I press the send button')
def i_press_the_send_button():
    """I press the send button."""
    raise NotImplementedError


@then('I should see the error message')
def i_should_see_the_error_message():
    """I should see the error message."""
    raise NotImplementedError
