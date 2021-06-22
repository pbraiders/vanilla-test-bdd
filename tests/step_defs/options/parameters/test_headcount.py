# coding=utf-8
"""Try to access the parameters page. feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.pages.options.parameters import ParametersPage  # pylint: disable=import-error
from pbraiders.pages.options.parameters.actions import HeadcountAction  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error

scenario = partial(scenario, 'options/parameters/headcount.feature')


@scenario('Updating the headcounts')
def test_update_headcount():
    """Updating the headcounts."""


@scenario('Not using a valid value')
def test_value_not_valid():
    """Not using a valid value."""


@given('I want to update the headcount per month', target_fixture="page_parameters")
def page_parameters(the_browser, the_config, the_database) -> HeadcountAction:
    """I want to update the headcount per month."""
    # Parameters page
    p_page = ParametersPage(_driver=the_browser, _config=the_config['urls'])
    if p_page.on_page() is False and p_page.visit() is False:
        # Signin
        assert sign_in(driver=the_browser, config=the_config, user="admin") is True
        assert p_page.visit() is True
    p_action = HeadcountAction(_page=p_page)
    return p_action


@when('I update the headcounts')
def update_headcount(page_parameters) -> None:
    """I update the headcounts."""
    page_parameters.fill_all().update()


@when('I update the headcounts with a non valid value')
def update_headcount_with_invalid_value(page_parameters) -> None:
    """I update the headcounts with a non valid value."""
    page_parameters.fill(2, 'A').update()


@then('I should see the success message')
def success_merssage(page_parameters) -> None:
    """I should see the success message."""
    assert page_parameters.has_succeeded() is True


@then('I should see the error message')
def error_merssage(page_parameters) -> None:
    """I should see the error message."""
    assert page_parameters.has_failed() is True


@then('The update should be permanent')
def permanent_update(the_browser, the_config) -> None:
    """The update should be permanent."""
    assert sign_in(driver=the_browser, config=the_config, user="admin") is True
    p_page = ParametersPage(_driver=the_browser, _config=the_config['urls'])
    assert p_page.visit() is True
    p_action = HeadcountAction(_page=p_page)
    assert p_action.check() is True
