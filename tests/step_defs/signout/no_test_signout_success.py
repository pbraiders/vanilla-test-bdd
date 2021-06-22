# coding=utf-8
"""Successful signout feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.signout import PageSignout  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error

scenario = partial(scenario, 'signout/signout_success.feature')


@scenario('Sign out')
def test_sign_out() -> None:
    """Sign out."""


@given('I am using the app', target_fixture="page_signout")
def page_signout(the_browser, the_config, the_database) -> PageSignout:
    """I am using the app."""
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    sign_in(p_page_signin, UserSimpleFactory().initialize(the_config["data"]["users"]))
    del p_page_signin
    return PageSignout(browser=the_browser, config=the_config['urls'])


@when('I sign out of the app')
def sign_out(page_signout) -> None:
    """I sign out of the app."""
    page_signout.visit()


@then('I should be disconnected')
def not_connected(page_signout) -> None:
    """I should be disconnected."""
    assert page_signout.on_page() is True
