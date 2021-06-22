# coding=utf-8
"""Password update, success cases feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.options.users import PageAccount  # pylint: disable=import-error
from pbraiders.options.users import PageUsers  # pylint: disable=import-error
from pbraiders.options.users import new_account  # pylint: disable=import-error
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/password_update_success.feature')


@scenario('Update a password')
def test_update_password():
    """Update a password."""


@given('I am on an activated user account page',
       target_fixture="page_user_account")
def page_user_account(the_config, the_browser, the_database, new_user) -> PageAccount:
    """I am on an activated user account page"""
    # Sign in as admin
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    sign_in(p_page_signin, UserAdminFactory().initialize(the_config["data"]["users"]))
    # To create new user
    p_page_users = PageUsers(browser=the_browser, config=the_config['urls'], user=None)
    new_account(p_page_users, new_user)
    del p_page_users
    # Sign in successfully to this user account
    sign_in(p_page_signin, new_user)
    # Sign in as admin again
    sign_in(p_page_signin, UserAdminFactory().initialize(the_config["data"]["users"]))
    del p_page_signin
    # Go to the account page
    p_page_account = PageAccount(browser=the_browser, config=the_config['urls'], user=new_user)
    assert p_page_account.visit() is True
    return p_page_account


@ when('I change the password')
def i_change_the_password(page_user_account) -> None:
    """I change the password."""
    page_user_account.fill_password().confirm_password().click()


@ then('I can sign in to this account using the new password')
def i_can_sign_in_to_this_account_using_the_new_password(
        the_config, the_browser, page_user_account) -> None:
    """I can sign in to this account using the new password."""
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    sign_in(p_page_signin, page_user_account.user)
