# coding=utf-8
"""Try to access the logs page feature tests."""

import pytest
from functools import partial
from pytest_bdd import (
    scenario,
    then,
    when,
)
from pbraiders.options.logs import PageLogs  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error
from pbraiders.user import SimpleUserFactory  # pylint: disable=import-error
from pbraiders.user import DisabledUserFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/logs/access.feature')


@scenario('Accessing the logs page')
def test_access():
    """Accessing the logs page."""


@scenario('Not accessing the logs page', example_converters=dict(type=str))
def test_no_access():
    """Not accessing the logs page."""


@when('I am the admin user')
def admin_user(the_config, the_browser, the_database) -> None:
    """I am the admin user."""
    # Connect
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    sign_in(p_page_signin, AdminUserFactory().initialize(the_config["data"]["users"]))
    del p_page_signin


@when('I am the <type> user')
def type_user(the_config, the_browser, type) -> None:
    """I am the <type> user."""
    assert isinstance(type, str)
    switcher = {
        "admin": AdminUserFactory().initialize(the_config["data"]["users"]),
        "simple": SimpleUserFactory().initialize(the_config["data"]["users"]),
        "deactivated": DisabledUserFactory().initialize(the_config["data"]["users"]),
    }
    # Connect
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    p_page_signin.set_user(switcher.get(type, None)).visit().fill_credential().click()
    del p_page_signin


@then('I cannot access to the logs page')
def no_access(the_config, the_browser) -> None:
    """I cannot access to the logs page."""
    p_page_logs = PageLogs(browser=the_browser, config=the_config['urls'])
    assert p_page_logs.visit().on_page() is False


@then('I can access to the logs page')
def access(the_config, the_browser) -> None:
    """I can access to the logs page."""
    p_page_logs = PageLogs(browser=the_browser, config=the_config['urls'])
    assert p_page_logs.visit().on_page() is True
