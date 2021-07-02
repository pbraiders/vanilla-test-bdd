# coding=utf-8
"""Event deletion, cancel cases."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.event import EventFakerFactory  # pylint: disable=import-error
from pbraiders.pages.events import EventPage  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventDeleteAction  # pylint: disable=import-error
from pbraiders.pages import new_event  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'events/event_delete_cancel.feature')


@scenario('Not deleting an event')
def test_not_deleting_an_event() -> None:
    """Not deleting an event."""


@given('I am on a event page', target_fixture="page_event")
def page_event(the_config, the_browser, the_faker, the_database) -> EventPage:
    """I am on a event page."""

    # Create new event
    p_contact = ContactFakerFactory(_faker=the_faker).initialize(config={})
    p_event = EventFakerFactory(_faker=the_faker).initialize(config={})
    assert sign_in(driver=the_browser, config=the_config, user="simple") is True
    assert new_event(driver=the_browser, config=the_config['urls'], contact=p_contact, event=p_event) is True

    # Access the event page
    p_page = EventPage(_driver=the_browser,
                       _config=the_config['urls'],
                       _event=p_event,
                       _contact=p_contact)
    assert p_page.visit() is True

    return p_page


@when('I cancel the deletion of the event')
def cancel_delete_event(page_event) -> None:
    """I cancel the deletion of the event."""
    p_action = EventDeleteAction(_page=page_event)
    p_action.delete().cancel()


@then('I should still access into the event page')
def still_access(page_event) -> None:
    """I should still access into the event page."""
    assert page_event.visit() is True
