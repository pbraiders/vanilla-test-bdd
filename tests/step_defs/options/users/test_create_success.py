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
from pbraiders.options.users import PageUsers  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error
from pbraiders.user import User  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/create_success.feature')


@scenario('I successfully created a new user')
def test_successful():
    """I successfully created a new user."""


@scenario('I successfully sign in with a new created user')
def test_connect():
    """I successfully sign in with a new created user."""


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
    p_page = PageUsers(browser=the_browser, config=the_config['urls'], user=User(
        login=s_name, password=s_passwd, passwordc=s_passwd))
    p_page.visit()
    return p_page


@when('I send the new credential')
def enter_credential(users_page):
    """I send the new credential."""
    users_page.fill_name().fill_password().confirm_password().click()


@when('I successfully create the new user')
def creates_user(users_page):
    """I successfully create the new user."""
    assert users_page.fill_name().fill_password().confirm_password().click().has_succeeded() is True


@then('I should see the success message')
def success_message(users_page):
    """I should see the success message."""
    assert users_page.has_succeeded() is True


@then('I can sign in to this new user account')
def connect(the_config, the_browser, users_page):
    """ I can sign in to this new user account."""
    p_page = PageSignin(
        browser=the_browser, config=the_config['urls'],
        user=users_page.user)
    p_page.connect_success()
