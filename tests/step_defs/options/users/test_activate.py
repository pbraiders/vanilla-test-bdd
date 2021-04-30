# coding=utf-8
"""Activate deactivate user feature tests."""

import pytest
from functools import partial
from pytest_bdd import (
    given,
    parsers,
    scenario,
    then,
    when,
)
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.options.users import PageAccount  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error
from pbraiders.user import SimpleUserFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/activate.feature')


@scenario('Deactivate an user')
def test_deactivate():
    """Deactivate an user."""


@scenario('Activate an user')
def test_activate():
    """Activate an user."""


@given(parsers.parse('I am on the {status} user account page'),
       target_fixture="page_user_account")
def page_user_account(
        the_config,
        the_browser,
        the_database,
        status) -> PageAccount:
    """I am on an activated /deactivated user account page"""
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
    # Go to the simple user account page
    p_page_account = PageAccount(
        browser=the_browser,
        config=the_config['urls'],
        user=None)
    p_page_account.set_user(
        SimpleUserFactory().initialize(
            the_config["data"]["users"])).visit()
    # Chech the status
    if "activated" == status:
        assert p_page_account.checked() is True
    if "deactivated" == status:
        assert p_page_account.checked() is False
    return p_page_account


@when(parsers.parse('I {action} this user account'))
def change_status(page_user_account, action) -> None:
    """I activate/deactivate this user account."""
    if "deactivate" == action:
        page_user_account.uncheck()
    else:
        page_user_account.check()
    page_user_account.click()
    assert page_user_account.has_succeeded() is True


@then('I can sign in to this account again')
def can_sign_in(the_config, the_browser) -> None:
    """I can sign in to this account again."""
    p_page_signin = PageSignin(
        browser=the_browser,
        config=the_config['urls'],
        user=None)
    sign_in(
        p_page_signin,
        SimpleUserFactory().initialize(
            the_config["data"]["users"]))


@then('I cannot sign in to this account anymore')
def cannot_sign_in(the_config, the_browser, page_user_account) -> None:
    """I cannot sign in to this account anymore."""
    p_page_signin = PageSignin(
        browser=the_browser,
        config=the_config['urls'],
        user=None)
    p_page_signin.set_user(
        SimpleUserFactory().initialize(
            the_config["data"]["users"]))
    p_page_signin.visit().fill_credential().click()
    assert p_page_signin.has_failed() is True
