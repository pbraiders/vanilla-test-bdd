# coding=utf-8
"""Contact delete, success cases feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.contacts import PageContact  # pylint: disable=import-error
from pbraiders.contacts import PageContacts  # pylint: disable=import-error
from pbraiders.contacts import new_contact  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contact_delete_success.feature')


@scenario('Delete a contact')
def test_delete_a_contact() -> None:
    """Delete a contact."""


@given('I am on a contact page', target_fixture="page_contact")
def page_contact(the_config, the_browser, the_faker, the_database) -> PageContact:
    """I am on a contact page."""

    # Create new contact
    p_contact = new_contact(p_driver=the_browser,
                            a_config=the_config,
                            p_contact_factory=ContactFakerFactory(faker=the_faker),
                            p_user_factory=UserSimpleFactory())

    # Access the contact page
    p_page_contacts = PageContacts(browser=the_browser, config=the_config['urls'], contact=p_contact)
    assert p_page_contacts.visit() is True
    assert p_page_contacts.is_on_list() is True
    del p_page_contacts

    p_page_contact = PageContact(browser=the_browser, config=the_config['urls'], contact=p_contact)
    assert p_page_contact.visit() is True and p_page_contact.is_contact_present() is True

    return p_page_contact


@when('I delete the contact')
def delete_contact(page_contact) -> None:
    """I delete the contact."""
    page_contact.delete()


@then('I should not see the contact on the list anymore')
def i_should_not_see_the_contact_on_the_list_anymore():
    """I should not see the contact on the list anymore."""
    raise NotImplementedError


@then('I should see the success message')
def i_should_see_the_success_message():
    """I should see the success message."""
    raise NotImplementedError
