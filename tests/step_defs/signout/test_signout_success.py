# coding=utf-8
"""Successful signout feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.pages.signout import SignoutPage  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'signout/signout_success.feature')


@scenario('Sign out')
def test_sign_out() -> None:
    """Sign out."""


@given('I am using the app', target_fixture="page_signout")
def page_signout(the_browser, the_config, the_database) -> SignoutPage:
    """I am using the app."""
    sign_in(driver=the_browser,
            config=the_config['urls'],
            user=UserSimpleFactory().initialize(the_config["data"]["users"]))
    return SignoutPage(_driver=the_browser, _config=the_config['urls'])


@when('I sign out of the app')
def sign_out(page_signout) -> None:
    """I sign out of the app."""
    page_signout.visit()


@then('I should be disconnected')
def not_connected(page_signout) -> None:
    """I should be disconnected."""
    assert page_signout.on_page() is True
