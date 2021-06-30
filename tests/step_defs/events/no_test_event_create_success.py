# coding=utf-8
"""Event creation, success cases."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.event import Date  # pylint: disable=import-error
from pbraiders.event import Headcount  # pylint: disable=import-error
from pbraiders.event import Event  # pylint: disable=import-error
from pbraiders.pages.events import EventsPage  # pylint: disable=import-error
from pbraiders.pages.events.actions import CreateEventAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import FillEventAction  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'events/event_create_success.feature')


@scenario('Create the event for a new contact')
def test_create_event_for_new_contact() -> None:
    """Create the contact."""


@given('I am on the new event page', target_fixture="page_new_event")
def page_new_event(the_config, the_browser, the_database) -> EventsPage:
    """I am on the new event page."""
    p_page = EventsPage(_driver=the_browser, _config=the_config['urls'])
    p_page.set_event(Event(Date(), headcount=Headcount()))
    if p_page.visit() is False:
        assert sign_in(driver=the_browser, config=the_config, user="simple") is True
        assert p_page.visit() is True
    return p_page


@when('I create an event for a new contact')
def contact_create(page_contact_new, contact_new) -> None:
    """I create an event for a new contact."""
    page_contact_new.set_contact(contact_new)
    p_action = FillContactAction(_page=page_contact_new)
    p_action.fill_lastname() \
        .fill_firstname() \
        .fill_phone() \
        .fill_zip() \
        .fill_city() \
        .fill_address_more() \
        .fill_address() \
        .fill_email()
    del p_action
    p_action = CreateContactAction(_page=page_contact_new)
    p_action.click()


@then('I should see the success message')
def success_message(page_contact_new) -> None:
    """I should see the success message."""
    p_action = CreateContactAction(_page=page_contact_new)
    assert p_action.has_succeeded() is True


@then('It should appear on the contact list')
def contact_list(the_config, the_browser, contact_new):
    """It should appear on the contact list."""
    p_page = ContactsPage(_driver=the_browser, _config=the_config['urls'], _contact=contact_new)
    if p_page.on_page() is False:
        assert p_page.visit() is True
    assert p_page.is_on_list() is True


@then('I should access to this contact page')
def conctact_page(the_config, the_browser, contact_new):
    """I should access to this contact page."""
    p_page = ContactPage(_driver=the_browser, _config=the_config['urls'], _contact=contact_new)
    assert p_page.visit() is True
    assert p_page.is_contact_present() is True
