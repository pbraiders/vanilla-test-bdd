# coding=utf-8
"""Delete old reservations failure cases."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from datetime import date
from pbraiders.pages.options.parameters import ParametersPage  # pylint: disable=import-error
from pbraiders.pages.options.parameters.actions import PurgeAction  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'options/parameters/purge_failure.feature')


@scenario('No year')
def test_purge_no_year():
    """No year."""


@scenario('Delete with an invalid year', example_converters=dict(year=str))
def test_purge_invalid_year():
    """Delete with an invalid year."""


@given('I want to delete old reservations', target_fixture="page_parameters")
def page_parameters(the_browser, the_config, the_database) -> ParametersPage:
    """I want to delete old reservations."""
    # Parameters page
    p_page = ParametersPage(_driver=the_browser, _config=the_config['urls'])
    if p_page.on_page() is False and p_page.visit() is False:
        # Signin
        assert sign_in(driver=the_browser, config=the_config, user="admin") is True
        assert p_page.visit() is True
    return p_page


@when('I do not enter a year')
def enter_not_a_year(page_parameters) -> None:
    """I do not enter a year."""
    p_action = PurgeAction(_page=page_parameters)
    assert p_action.purge().has_failed() is True


@when('I enter the <year>')
def enter_the_year(page_parameters, year) -> None:
    """I enter the <year>."""
    assert isinstance(year, str)
    switcher = {
        "future": date.today().year + 1,
    }
    p_action = PurgeAction(_page=page_parameters)
    p_action.fill(str(switcher.get(year, year))).purge()


@then('I should see the error message')
def error_message(page_parameters) -> None:
    """I should see the error message."""
    p_action = PurgeAction(_page=page_parameters)
    assert p_action.has_failed() is True
