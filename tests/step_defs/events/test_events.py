# coding=utf-8
"""Try to access the events list page feature tests."""

from functools import partial
from pytest_bdd import (
    scenario,
    then,
    when,
)
from pbraiders.event import Date  # pylint: disable=import-error
from pbraiders.event import Headcount  # pylint: disable=import-error
from pbraiders.event import Event  # pylint: disable=import-error
from pbraiders.pages.events import EventsPage  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'events/events.feature')


@scenario('Accessing the events page.', example_converters=dict(type=str, permission=str))
def test_accessing_the_events_page() -> None:
    """Accessing the events page."""


@when('I am the <type> user')
def type_user(the_config, the_browser, type) -> None:
    """I am the <type> user."""
    assert isinstance(type, str)
    sign_in(driver=the_browser, config=the_config, user=type)


@then('I <permission> access to the events page')
def access_page(the_config, the_browser, permission) -> None:
    """I <permission> access to the events page."""
    assert isinstance(permission, str)
    p_page = EventsPage(_driver=the_browser, _config=the_config['urls'])
    p_page.event = Event(Date(), headcount=Headcount())
    if permission.lower() == 'can':
        assert p_page.visit() is True
    else:
        assert p_page.visit() is False
