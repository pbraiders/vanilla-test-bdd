# coding=utf-8
"""Try to access the parameters page. feature tests."""

from functools import partial
from pytest_bdd import (
    scenario,
    then,
    when,
)
from pbraiders.options.parameters import PageParameters  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error
from pbraiders.user import UserClosedFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/parameters/parameters.feature')


@scenario('Accessing the parameters page.')
def test_accessing_the_parameters_page():
    """Accessing the parameters page.."""


@scenario('Not accessing the parameters page.', example_converters=dict(type=str))
def test_not_accessing_the_parameters_page():
    """Not accessing the parameters page.."""


@when('I am the admin user')
def i_am_the_admin_user(the_config, the_browser, the_database) -> None:
    """I am the admin user."""
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    sign_in(p_page_signin, UserAdminFactory().initialize(the_config["data"]["users"]))


@when('I am the <type> user')
def i_am_the_type_user(the_config, the_browser, type) -> None:
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


@then('I cannot access to the parameters page')
def i_cannot_access_to_the_parameters_page(the_config, the_browser) -> None:
    """I cannot access to the parameters page."""
    p_page_parameters = PageParameters(browser=the_browser, config=the_config['urls'])
    assert p_page_parameters.visit() is False


@then('I can access to the parameters page')
def i_can_access_to_the_parameters_page(the_config, the_browser) -> None:
    """I can access to the parameters page."""
    p_page_parameters = PageParameters(browser=the_browser, config=the_config['urls'])
    assert p_page_parameters.visit() is True
