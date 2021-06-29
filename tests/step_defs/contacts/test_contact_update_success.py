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
from pbraiders.pages.contacts.actions import FillContactAction  # pylint: disable=import-error
from pbraiders.pages.contacts.actions import UpdateContactAction  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactPage  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactsPage  # pylint: disable=import-error
from pbraiders.pages import new_contact  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'contacts/contact_update_success.feature')


@scenario('Update a contact')
def test_update_contact() -> None:
    """Update a contact."""


@given('I am on a contact page', target_fixture="page_contact")
def page_contact(the_config, the_browser, the_faker, the_database) -> ContactPage:
    """I am on the contact page."""

    # Create new contact
    p_contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    assert sign_in(driver=the_browser, config=the_config, user="simple") is True
    assert new_contact(driver=the_browser, config=the_config['urls'], contact=p_contact) is True

    # Access the contact page
    p_page = ContactPage(_driver=the_browser, _config=the_config['urls'], _contact=p_contact)
    assert p_page.visit() is True
    assert p_page.is_contact_present() is True

    return p_page


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
    if len(page_contact.contact.zip) < 8:
        page_contact.contact.zip += '*'
    page_contact.contact.comment = 'updated'

    # Fill the fields
    p_action = FillContactAction(_page=page_contact)
    p_action.fill_lastname() \
        .fill_firstname() \
        .fill_phone() \
        .fill_zip() \
        .fill_city() \
        .fill_address_more() \
        .fill_address() \
        .fill_email() \
        .fill_comment()
    del p_action

    # Update
    p_action = UpdateContactAction(_page=page_contact)
    p_action.update()


@then('I should see the success message')
def success_message(page_contact) -> None:
    """I should see the success message."""
    p_action = UpdateContactAction(_page=page_contact)
    assert p_action.has_succeeded() is True


@then('I should see the update on the contacts list')
def check_contacts_list(the_browser, the_config, page_contact) -> None:
    """I should see the update on the contacts list."""
    p_page = ContactsPage(_driver=the_browser, _config=the_config['urls'], _contact=page_contact.contact)
    if p_page.on_page() is False:
        assert p_page.visit() is True
    assert p_page.is_on_list() is True


@then('I should see the update on the contact page')
def check_contact_page(page_contact) -> None:
    """I should see the update on the contact page."""
    assert page_contact.visit() is True
    assert page_contact.is_contact_present() is True
    assert page_contact.is_contact_comments_present() is True
