# coding=utf-8
"""Try to access the graphs page. feature tests."""

from functools import partial
from pytest_bdd import (
    scenario,
    then,
    when,
)
from pbraiders.pages.options.graphs import GraphsPage  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'options/graphs/graphs.feature')


@scenario('Accessing the graphs page.', example_converters=dict(type=str, permission=str))
def test_accessing_the_graphs_page():
    """Accessing the graphs page."""


@when('I am the <type> user')
def type_user(the_config, the_browser, type) -> None:
    """I am the <type> user."""
    assert isinstance(type, str)
    sign_in(driver=the_browser, config=the_config, user=type)


@then('I <permission> access to the graphs page')
def access_page(the_config, the_browser, permission) -> None:
    """I <permission> access to the graphs page."""
    assert isinstance(permission, str)
    p_page = GraphsPage(_driver=the_browser, _config=the_config['urls'])
    if permission.lower() == 'can':
        assert p_page.visit() is True
    else:
        assert p_page.visit() is False
