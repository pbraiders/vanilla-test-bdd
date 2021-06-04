# coding=utf-8
"""Try to access the graphs page. feature tests."""

from functools import partial
from pytest_bdd import (
    scenario,
    then,
    when,
)
from pbraiders.options.graphs import PageGraphs  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error
from pbraiders.user import UserClosedFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/graphs/graphs.feature')


@scenario('Accessing the graphs page.', example_converters=dict(type=str, permission=str))
def test_accessing_the_graphs_page():
    """Accessing the graphs page."""


@when('I am the <type> user')
def type_user(the_config, the_browser, type) -> None:
    """I am the <type> user."""
    assert isinstance(type, str)
    switcher = {
        "admin": UserAdminFactory().initialize(the_config["data"]["users"]),
        "simple": UserSimpleFactory().initialize(the_config["data"]["users"]),
        "deactivated": UserClosedFactory().initialize(the_config["data"]["users"]),
    }
    # Connect
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    assert p_page_signin.sign_out().visit() is True
    p_page_signin.set_user(switcher.get(type, None)).fill_credential().click()


@then('I <permission> access to the graphs page')
def access_page(the_config, the_browser, permission) -> None:
    """I <permission> access to the graphs page."""
    assert isinstance(permission, str)
    p_page_graphs = PageGraphs(browser=the_browser, config=the_config['urls'])
    if permission.lower() == 'can':
        assert p_page_graphs.visit() is True
    else:
        assert p_page_graphs.visit() is False
