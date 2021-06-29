# coding=utf-8
"""User creation, success cases."""

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

scenario = partial(scenario, 'options/users/create_success.feature')


@scenario('Create the user')
def test_successful() -> None:
    """Create the user."""


@given('I am on the users page', target_fixture="page_users")
def page_users(the_config, the_browser, the_database) -> UsersPage:
    """I am on the users page."""
    # Sign in as admin
    assert sign_in(driver=the_browser, config=the_config, user="admin") is True
    # Go to Users page
    p_page = UsersPage(_driver=the_browser, _config=the_config['urls'], _user=None)
    assert p_page.visit() is True
    return p_page


@when('I create a new user')
def creates_user(page_users, new_user) -> None:
    """I create a new user."""
    page_users.set_user(new_user)

    # Fill the fields
    p_action = FillUserAction(_page=page_users)
    p_action.fill_name() \
            .fill_password() \
            .confirm_password()
    del p_action

    # Create
    p_action = CreateUserAction(_page=page_users)
    p_action.click()


@then('I should see the success message')
def success_message(page_users) -> None:
    """I should see the success message."""
    p_action = CreateUserAction(_page=page_users)
    assert p_action.has_succeeded() is True


@then('I can sign in to this new user account')
def connect(the_config, the_browser, page_users) -> None:
    """ I can sign in to this new user account."""
    assert sign_in(driver=the_browser, config=the_config, user=page_users.user.login, password=page_users.user.password) is True
