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


@scenario('Create the user')
def test_successful() -> None:
    """Create the user."""


@scenario('Successfully sign in with a new created user')
def test_connect() -> None:
    """Successfully sign in with a new created user."""


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


@when('I send the credential')
def send_credential(page_users, new_user) -> None:
    """I send the new credential."""
    page_users.set_user(new_user).fill_name().fill_password().confirm_password().click()


@when('I successfully create the new user')
def creates_user(page_users, new_user) -> None:
    """I successfully create the new user."""
    assert page_users.set_user(new_user).fill_name().fill_password().confirm_password().click().has_succeeded() is True


@then('I should see the success message')
def success_message(page_users) -> None:
    """I should see the success message."""
    assert page_users.has_succeeded() is True


@then('I can sign in to this new user account')
def connect(the_config, the_browser, page_users) -> None:
    """ I can sign in to this new user account."""
    p_page = PageSignin(
        browser=the_browser, config=the_config['urls'],
        user=page_users.user)
    p_page.connect_success()
