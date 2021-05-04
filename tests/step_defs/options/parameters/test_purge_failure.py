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
from pbraiders.options.parameters import PageParameters  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.user import AdminUserFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/parameters/purge_failure.feature')


@scenario('No year')
def test_purge_no_year():
    """No year."""


@scenario('Delete with an invalid year', example_converters=dict(year=str))
def test_purge_invalid_year():
    """Delete with an invalid year."""


@given('I want to delete old reservations', target_fixture="page_parameters")
def page_parameters(the_browser, the_config, the_database) -> PageParameters:
    """I want to delete old reservations."""
    # Parameters page
    p_page_parameters = PageParameters(browser=the_browser, config=the_config['urls'])
    if p_page_parameters.on_page() is False and p_page_parameters.visit() is False:
        # Signin
        p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
        sign_in(p_page_signin, AdminUserFactory().initialize(the_config["data"]["users"]))
        del p_page_signin
        assert p_page_parameters.visit() is True
    return p_page_parameters


@when('I do not enter a year')
def enter_not_a_year(page_parameters) -> None:
    """I do not enter a year."""
    assert page_parameters.purge().purge_has_failed() is True


@when('I enter the <year>')
def enter_the_year(page_parameters, year) -> None:
    """I enter the <year>."""
    assert isinstance(year, str)
    switcher = {
        "future": date.today().year + 1,
    }
    page_parameters.purge(switcher.get(year, year))


@ then('I should see the error message')
def error_message(page_parameters) -> None:
    """I should see the error message."""
    assert page_parameters.purge_has_failed() is True
