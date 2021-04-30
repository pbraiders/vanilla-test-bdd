# coding=utf-8
"""Password update, failure cases feature tests."""

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
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error
from pbraiders.user import SimpleUserFactory  # pylint: disable=import-error
from pbraiders.user import User  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/password_update_failure.feature')


@scenario('Confirmed password is mandatory')
def test_confirmed_password_is_mandatory():
    """Confirmed password is mandatory."""


@scenario('Password and confirmed password must be the same')
def test_password_and_confirmed_password_must_be_the_same():
    """Password and confirmed password must be the same."""


@scenario('Password is mandatory')
def test_password_is_mandatory():
    """Password is mandatory."""


@given('I am on the simple user account page',
       target_fixture="page_user_account")
def page_user_account(the_config, the_browser, the_database) -> PageAccount:
    """I am on the simple user account page."""
    p_page_account = PageAccount(
        browser=the_browser,
        config=the_config['urls'],
        user=SimpleUserFactory().initialize(the_config["data"]["users"]))
    if p_page_account.on_page() is False:
        # Not on the account page. Sign in as admin
        p_page_signin = PageSignin(
            browser=the_browser,
            config=the_config['urls'],
            user=None)
        sign_in(
            p_page_signin,
            AdminUserFactory().initialize(
                the_config["data"]["users"]))
        del p_page_signin
        # Visit simple user account page
        p_page_account.visit()
    return p_page_account


@when('I send the credential with a different confirmed password')
def send_credential_with_different_confirmed_password(
        page_user_account) -> None:
    """I send the credential with a different confirmed password."""
    s_confirmed_password = page_user_account.user.passwordc
    page_user_account.user.passwordc = s_confirmed_password + 'not the same'
    page_user_account.fill_password().confirm_password().click()
    page_user_account.user.passwordc = s_confirmed_password


@when('I send the credential without the confirmed password')
def send_credential_without_confirmed_password(page_user_account) -> None:
    """I send the credential without the confirmed password."""
    page_user_account.fill_password().click()


@when('I send the credential without the password')
def send_credential_without_password(page_user_account) -> None:
    """I send the credential without the password."""
    page_user_account.confirm_password().click()


@then('I should see the error message')
def error_message(page_user_account) -> None:
    """I should see the error message."""
    assert page_user_account.has_failed() is True
