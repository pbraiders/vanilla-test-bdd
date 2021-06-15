# coding=utf-8
"""Contact update, success cases."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.contacts import PageContact  # pylint: disable=import-error
from pbraiders.contacts import PageContactUpdate  # pylint: disable=import-error
from pbraiders.contacts import PageContacts  # pylint: disable=import-error
from pbraiders.contacts import new_contact  # pylint: disable=import-error
from pbraiders.user import UserSimpleFactory  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contact_update_success.feature')


@scenario('Update a contact')
def test_update_contact() -> None:
    """Update a contact."""


@given('I am on a contact page', target_fixture="page_contact")
def page_contact(the_config, the_browser, the_faker, the_database) -> PageContact:
    """I am on the contact page."""

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
    assert p_page_contact.visit() is True

    p_page_contact_update = PageContactUpdate(parent=p_page_contact)
    assert p_page_contact_update.is_contact_present() is True

    return p_page_contact


@when('I update data')
def update_data(page_contact) -> None:
    """I update data."""
    page_contact.contact.lastname += '_updated'
    page_contact.contact.firstname += '_updated'
    page_contact.contact.tel += '*'
    page_contact.contact.email += '_updated'
    page_contact.contact.address += '_updated'
    page_contact.contact.address_more += '_updated'
    page_contact.contact.city += '_updated'
    page_contact.contact.zip += '*'
    page_contact.contact.comment = 'updated'

    p_page_contact = PageContactUpdate(parent=page_contact)
    p_page_contact.fill_lastname() \
        .fill_firstname() \
        .fill_phone() \
        .fill_zip() \
        .fill_city() \
        .fill_address_more() \
        .fill_address() \
        .fill_email() \
        .fill_comment() \
        .update()


@then('I should see the success message')
def success_message(page_contact) -> None:
    """I should see the success message."""
    p_page_contact = PageContactUpdate(parent=page_contact)
    assert p_page_contact.has_succeeded() is True


@then('I should see the update on the contacts list')
def check_contacts_list(the_browser, the_config, page_contact) -> None:
    """I should see the update on the contacts list."""
    p_page_contacts = PageContacts(browser=the_browser, config=the_config['urls'], contact=page_contact.contact)
    assert p_page_contacts.visit() is True
    assert p_page_contacts.is_on_list() is True


@then('I should see the update on the contact page')
def check_contact_page(page_contact) -> None:
    """I should see the update on the contact page."""
    assert page_contact.visit() is True
    p_page_contact = PageContactUpdate(parent=page_contact)
    assert p_page_contact.is_contact_present() is True and p_page_contact.is_contact_comments_present() is True
