# coding=utf-8
"""Password update, success cases feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error
from pbraiders.pages.users_utilities import new_account  # pylint: disable=import-error
from pbraiders.pages.options.users import UserPage  # pylint: disable=import-error
from pbraiders.pages.options.users.actions import FillUserAction  # pylint: disable=import-error
from pbraiders.pages.options.users.actions import UpdateUserAction  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/password_update_success.feature')


@scenario('Update a password')
def test_update_password():
    """Update a password."""


@given('I am on an activated user account page', target_fixture="page_user")
def page_user(the_config, the_browser, the_database, new_user) -> UserPage:
    """I am on an activated user account page"""
    # Sign in as admin
    assert sign_in(driver=the_browser, config=the_config, user="admin") is True

    # To create new user
    assert new_account(driver=the_browser, config=the_config['urls'], user=new_user)
    assert sign_in(driver=the_browser, config=the_config, user=new_user.login, password=new_user.password) is True
    assert sign_in(driver=the_browser, config=the_config, user="admin") is True

    # Go to the account page
    p_page = UserPage(_driver=the_browser,
                      _config=the_config['urls'],
                      _user=new_user)
    assert p_page.visit() is True
    return p_page


@when('I change the password')
def i_change_the_password(page_user) -> None:
    """I change the password."""
    # Change password
    page_user.user.password = page_user.user.password + "_updated"
    page_user.user.passwordc = page_user.user.passwordc + "_updated"
    # Fill the fields
    p_action = FillUserAction(_page=page_user)
    p_action.fill_password() \
            .confirm_password()
    del p_action

    # Update
    p_action = UpdateUserAction(_page=page_user)
    p_action.update()


@then('I can sign in to this account using the new password')
def i_can_sign_in_to_this_account_using_the_new_password(
        the_config, the_browser, page_user) -> None:
    """I can sign in to this account using the new password."""
    assert sign_in(driver=the_browser, config=the_config, user=page_user.user.login, password=page_user.user.password) is True
