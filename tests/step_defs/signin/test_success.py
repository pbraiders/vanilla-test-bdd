# coding=utf-8
"""Successful signin feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error
from pbraiders.user import UserClosedFactory  # pylint: disable=import-error

scenario = partial(scenario, 'signin/success.feature')


@scenario('Account deactivated')
def test_deactivated() -> None:
    """Account deactivated."""


@scenario('Connecting', example_converters=dict(type=str))
def test_connecting() -> None:
    """Connecting."""


@given('I am on the signin page', target_fixture="page_signin")
def page_signin(the_browser, the_config, the_database) -> PageSignin:
    """I am on the signin page."""
    p_page = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    if p_page.on_page() is False:
        assert p_page.visit() is True
    return p_page


@when('I am the deactivated user')
def deactivated_user(the_config, page_signin) -> None:
    """I am the deactivated user."""
    page_signin.set_user(UserClosedFactory().initialize(the_config["data"]["users"])).fill_credential().click()


@when('I am the <type> user')
def type_user(type, the_config, page_signin) -> None:
    """I am the <type> user."""
    assert isinstance(type, str)
    switcher = {
        "admin": UserAdminFactory().initialize(the_config["data"]["users"]),
        "simple": UserSimpleFactory().initialize(the_config["data"]["users"]),
        "deactivated": UserClosedFactory().initialize(the_config["data"]["users"]),
    }
    page_signin.set_user(switcher.get(type, None)).fill_credential().click()


@then('I should be connected')
def connected(page_signin) -> None:
    """I should be connected."""
    assert page_signin.connected() is True


@then('I should not be connected')
def not_connected(page_signin) -> None:
    """I should not be connected."""
    assert page_signin.has_failed() is True
