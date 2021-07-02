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
from pbraiders.event import EventFakerFactory  # pylint: disable=import-error
from pbraiders.event import Date  # pylint: disable=import-error
from pbraiders.event import Headcount  # pylint: disable=import-error
from pbraiders.event import Event  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactPage  # pylint: disable=import-error
from pbraiders.pages.contacts import ContactsPage  # pylint: disable=import-error
from pbraiders.pages.events import EventsPage  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventCreateAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventAgeWriteAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import FillEventContactAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventHeadcountWriteAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventMoneyWriteAction  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'events/event_create_success.feature')


@scenario('Create the event for a new contact')
def test_create_event_for_new_contact() -> None:
    """Create the contact."""


@given('I am on the new event page', target_fixture="page_event_new")
def page_event_new(the_config, the_browser, the_database) -> EventsPage:
    """I am on the new event page."""
    p_page = EventsPage(_driver=the_browser, _config=the_config['urls'])
    p_page.event = Event(Date(), headcount=Headcount())
    if p_page.visit() is False:
        assert sign_in(driver=the_browser, config=the_config, user="simple") is True
        assert p_page.visit() is True
    return p_page


@when('I create an event for a new contact')
def create_event_for_new_contact(page_event_new, the_faker) -> None:
    """I create an event for a new contact."""
    # Create contact and event
    page_event_new.contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    page_event_new.event = EventFakerFactory(_faker=the_faker).initialize(config={})
    # Fill contact fields
    p_action = FillEventContactAction(_page=page_event_new)
    p_action.fill_lastname() \
            .fill_firstname() \
            .fill_phone() \
            .fill_zip() \
            .fill_city() \
            .fill_address_more() \
            .fill_address() \
            .fill_email()
    del p_action
    # Fill event headcount fields
    p_action = EventHeadcountWriteAction(_page=page_event_new)
    p_action.fill_real() \
            .fill_planned()
    del p_action
    # Fill event age fields
    p_action = EventAgeWriteAction(_page=page_event_new)
    p_action.choose()
    del p_action
    # Fill event arrh fields
    p_action = EventMoneyWriteAction(_page=page_event_new)
    p_action.choose()
    del p_action
    # Create
    p_action = EventCreateAction(_page=page_event_new)
    p_action.click()


@then('I should see the success message')
def success_message(page_event_new) -> None:
    """I should see the success message."""
    p_action = EventCreateAction(_page=page_event_new)
    assert p_action.has_succeeded() is True


@then('the event should appear on the event list')
def on_list_event(page_event_new) -> None:
    """the event should appear on the event list."""
    if page_event_new.on_page() is False:
        assert page_event_new.visit() is True
    assert page_event_new.is_on_list() is True


@then('I should access to this event page')
def access_event(page_event_new) -> None:
    """I should access to this event page."""
    if page_event_new.on_page() is False:
        assert page_event_new.visit() is True
    page_event_new.visit_event()


@then('the contact should appear on the contact list')
def on_list_contact(the_config, the_browser, page_event_new) -> None:
    """the contact should appear on the contact list."""
    p_page = ContactsPage(_driver=the_browser, _config=the_config['urls'], _contact=page_event_new.contact)
    if p_page.on_page() is False:
        assert p_page.visit() is True
    assert p_page.is_on_list() is True


@then('I should access to the contact page')
def access_contact(the_config, the_browser, page_event_new) -> None:
    """I should access to the contact page."""
    p_page = ContactPage(_driver=the_browser, _config=the_config['urls'], _contact=page_event_new.contact)
    assert p_page.visit() is True
    assert p_page.is_contact_present() is True
