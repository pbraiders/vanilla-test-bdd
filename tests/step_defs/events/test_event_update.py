# coding=utf-8
"""Event update, success cases."""

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
from pbraiders.pages.events.actions import EventUpdateAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventAgeReadAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventAgeWriteAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventContactReadAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventHeadcountReadAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventHeadcountWriteAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventMoneyReadAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventMoneyWriteAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventReadAction  # pylint: disable=import-error
from pbraiders.pages.events.actions import EventWriteAction  # pylint: disable=import-error
from pbraiders.pages import sign_in  # pylint: disable=import-error
from pbraiders.pages import new_event  # pylint: disable=import-error

scenario = partial(scenario, 'events/event_update_success.feature')


@scenario('Update an event')
def test_update_event() -> None:
    """Update an event."""


@given('I am on an event page', target_fixture="page_event")
def page_event(the_config, the_browser, the_faker, the_database) -> EventPage:
    """I am on an event page."""

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


@when('I update data')
def create_event_for_new_contact(page_event, the_faker) -> None:
    """I update data."""

    p_event = EventFakerFactory(_faker=the_faker).initialize(config={})
    page_event.event = p_event

    # Fill comment
    p_action = EventWriteAction(_page=page_event)
    p_action.fill_comment()
    del p_action

    # Fill event headcount fields
    p_action = EventHeadcountWriteAction(_page=page_event)
    p_action.fill_real() \
            .fill_planned() \
            .fill_canceled() \
            .fill_max()
    del p_action

    # Fill event age fields
    p_action = EventAgeWriteAction(_page=page_event)
    p_action.choose()
    del p_action

    # Fill event arrh fields
    p_action = EventMoneyWriteAction(_page=page_event)
    p_action.choose()
    del p_action

    # Update
    p_action = EventUpdateAction(_page=page_event)
    p_action.update()


@then('I should see the success message')
def success_message(page_event) -> None:
    """I should see the success message."""
    p_action = EventUpdateAction(_page=page_event)
    assert p_action.has_succeeded() is True


@then('I should see the update on the event page')
def access_event(the_config, the_browser, page_event) -> None:
    """I should see the update on the event page."""
    p_page = EventPage(_driver=the_browser,
                       _config=the_config['urls'],
                       _event=page_event.event,
                       _contact=page_event.contact)
    assert p_page.visit() is True

    # Check comment
    p_action = EventReadAction(_page=p_page)
    assert p_action.is_equal_comment() is True
    del p_action

    # Check contact
    p_action = EventContactReadAction(_page=p_page)
    assert p_action.is_equal_lastname() is True and \
        p_action.is_equal_firstname() is True and\
        p_action.is_equal_phone() is True and\
        p_action.is_equal_zip() is True and\
        p_action.is_equal_city() is True and \
        p_action.is_equal_address_more() is True and \
        p_action.is_equal_address() is True and \
        p_action.is_equal_email() is True
    del p_action

    # Check headcount
    p_action = EventHeadcountReadAction(_page=page_event)
    assert p_action.is_valid_real() is True and  \
        p_action.is_valid_planned() and \
        p_action.is_valid_canceled() and \
        p_action.is_valid_max()
    del p_action

    # check age
    p_action = EventAgeReadAction(_page=page_event)
    assert p_action.is_valid() is True
    del p_action

    # check arrh
    p_action = EventMoneyReadAction(_page=page_event)
    assert p_action.is_valid() is True
