# coding=utf-8
"""Try to access an event page feature tests."""

from functools import partial
from pytest_bdd import (
    scenario,
    given,
    then,
    when,
)
from pbraiders.contact import ContactFakerFactory  # pylint: disable=import-error
from pbraiders.event import EventFakerFactory  # pylint: disable=import-error
from pbraiders.pages.events import EventPage  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error
from pbraiders.pages import new_event  # pylint: disable=import-error

scenario = partial(scenario, 'events/event.feature')


@given('One today\'s event', target_fixture="fake_data")
def fake_data(the_config, the_browser, the_faker, the_database) -> EventPage:
    """One today's event."""

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


@scenario('Accessing an event page.', example_converters=dict(type=str, permission=str))
def test_accessing_an_event_page() -> None:
    """Accessing an event page."""


@when('I am the <type> user')
def type_user(the_config, the_browser, type) -> None:
    """I am the <type> user."""
    assert isinstance(type, str)
    sign_in(driver=the_browser, config=the_config, user=type)


@then('I <permission> access to an event page')
def access_page(the_config, the_browser, permission, fake_data) -> None:
    """I <permission> access to an event page."""
    assert isinstance(permission, str)
    p_page = EventPage(_driver=the_browser,
                       _config=the_config['urls'],
                       _event=fake_data.event,
                       _contact=fake_data.contact)
    if permission.lower() == 'can':
        assert p_page.visit() is True
    else:
        assert p_page.visit() is False
