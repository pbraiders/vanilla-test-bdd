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
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.options.users import PageUsers  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error
from pbraiders.user import User  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/create_success.feature')


@scenario('Create the user')
def test_successful() -> None:
    """Create the user."""


@given('I am on the users page', target_fixture="page_users")
def page_users(the_config, the_browser, the_database) -> PageUsers:
    """I am on the users page."""
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
    # Go to Users page
    p_page_users = PageUsers(
        browser=the_browser,
        config=the_config['urls'],
        user=None)
    p_page_users.visit()
    return p_page_users


@when('I create a new user')
def creates_user(page_users, new_user) -> None:
    """I create a new user."""
    page_users.set_user(new_user).visit().fill_name(
    ).fill_password().confirm_password().click()


@then('I should see the success message')
def success_message(page_users) -> None:
    """I should see the success message."""
    assert page_users.has_succeeded() is True


@then('I can sign in to this new user account')
def connect(the_config, the_browser, page_users) -> None:
    """ I can sign in to this new user account."""
    p_page_signin = PageSignin(
        browser=the_browser,
        config=the_config['urls'],
        user=None)
    sign_in(p_page_signin, page_users.user)
