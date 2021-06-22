# coding=utf-8
"""Try to access the contacts list page feature tests."""

from functools import partial
from pytest_bdd import (
    scenario,
    then,
    when,
)
from pbraiders.contacts import ContactsPage  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error
from pbraiders.user import UserClosedFactory  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contacts.feature')


@scenario('Accessing the contacts page.', example_converters=dict(type=str, permission=str))
def test_accessing_the_contacts_page() -> None:
    """Accessing the contacts page."""


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
    p_page = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    assert p_page.sign_out().visit() is True
    p_page.set_user(switcher.get(type, None)).fill_credential().click()


@then('I <permission> access to the contacts page')
def access_page(the_config, the_browser, permission) -> None:
    """I <permission> access to the contacts page."""
    assert isinstance(permission, str)
    p_page = ContactsPage(browser=the_browser, config=the_config['urls'])
    if permission.lower() == 'can':
        assert p_page.visit() is True
    else:
        assert p_page.visit() is False
