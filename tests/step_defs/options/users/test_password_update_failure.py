# coding=utf-8
"""Password update, failure cases feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error
from pbraiders.pages.options.users import UserPage  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory

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


@given('I am on the simple user account page', target_fixture="page_user")
def page_user(the_config, the_browser, the_database) -> UserPage:
    """I am on the simple user account page."""
    p_page = UserPage(_driver=the_browser,
                      _config=the_config['urls'],
                      _user=UserSimpleFactory().initialize(the_config["data"]["users"]))
    if p_page.on_page() is False:
        # Sign in as admin
        assert sign_in(driver=the_browser, config=the_config, user="admin") is True
        # Visit simple user account page
        assert p_page.visit() is True
    return p_page


@when('I send the credential with a different confirmed password')
def send_credential_with_different_confirmed_password(page_user) -> None:
    """I send the credential with a different confirmed password."""
    s_confirmed_password = page_user.user.passwordc
    
    page_user.user.passwordc = s_confirmed_password + 'not the same'
    page_user.fill_password().confirm_password().click()
    page_user.user.passwordc = s_confirmed_password


@when('I send the credential without the confirmed password')
def send_credential_without_confirmed_password(page_user) -> None:
    """I send the credential without the confirmed password."""
    page_user.fill_password().click()


@when('I send the credential without the password')
def send_credential_without_password(page_user) -> None:
    """I send the credential without the password."""
    page_user.confirm_password().click()


@then('I should see the error message')
def error_message(page_user) -> None:
    """I should see the error message."""
    assert page_user.has_failed() is True
