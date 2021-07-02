# coding=utf-8
"""Event creation, failure cases."""

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
from pbraiders.pages.events.actions import EventCreateAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventContactWriteAction  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'events/event_create_failure.feature')


@scenario('Lastname is mandatory')
def test_lastname_is_mandatory() -> None:
    """Lastname is mandatory."""


@scenario('Firstname is mandatory')
def test_firstname_is_mandatory() -> None:
    """Firstname is mandatory."""


@scenario('Phone number is mandatory')
def test_phone_number_is_mandatory() -> None:
    """Phone number is mandatory."""


@given('I am on the new event page', target_fixture="page_event_new")
def page_event_new(the_config, the_browser, the_database) -> EventsPage:
    """I am on the new event page."""
    p_page = EventsPage(_driver=the_browser, _config=the_config['urls'])
    p_page.event = Event(Date(), headcount=Headcount())
    if p_page.visit() is False:
        assert sign_in(driver=the_browser, config=the_config, user="simple") is True
        assert p_page.visit() is True
    return p_page


@when('I send the data without the lastname')
def send_data_without_lastname(page_event_new, the_faker) -> None:
    """I send the data without the lastname."""
    page_event_new.contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    p_action = EventContactWriteAction(_page=page_event_new)
    p_action.fill_firstname().fill_phone()
    del p_action
    p_action = EventCreateAction(_page=page_event_new)
    p_action.click()


@when('I send the data without the firstname')
def send_data_without_firstname(page_event_new, the_faker) -> None:
    """I send the data without the firstname."""
    page_event_new.contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    p_action = EventContactWriteAction(_page=page_event_new)
    p_action.fill_lastname().fill_phone()
    del p_action
    p_action = EventCreateAction(_page=page_event_new)
    p_action.click()


@when('I send the data without the phone number')
def send_data_without_phone_number(page_event_new, the_faker) -> None:
    """I send the data without the phone number."""
    page_event_new.contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    p_action = EventContactWriteAction(_page=page_event_new)
    p_action.fill_lastname().fill_firstname()
    del p_action
    p_action = EventCreateAction(_page=page_event_new)
    p_action.click()


@then('I should see the error message')
def error_message(page_event_new) -> None:
    """I should see the error message."""
    p_action = EventCreateAction(_page=page_event_new)
    assert p_action.has_failed() is True
