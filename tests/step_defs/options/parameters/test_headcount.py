# coding=utf-8
"""Try to access the parameters page. feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.options.parameters import PageParameters  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/parameters/headcount.feature')


@scenario('Updating the headcounts')
def test_update_headcount():
    """Updating the headcounts."""


@scenario('Not using a valid value')
def test_value_not_valid():
    """Not using a valid value."""


@given('I want to update the headcount per month', target_fixture="page_parameters")
def page_parameters(the_browser, the_config, the_database) -> PageParameters:
    """I want to update the headcount per month."""
    # Parameters page
    p_page_parameters = PageParameters(browser=the_browser, config=the_config['urls'])
    if p_page_parameters.on_page() is False and p_page_parameters.visit() is False:
        # Signin
        p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
        sign_in(p_page_signin, UserAdminFactory().initialize(the_config["data"]["users"]))
        del p_page_signin
        assert p_page_parameters.visit() is True
    return p_page_parameters


@when('I update the headcounts')
def update_headcount(page_parameters) -> None:
    """I update the headcounts."""
    page_parameters.headcounts().update_headcount()


@when('I update the headcounts with a non valid value')
def update_headcount_with_invalid_value(page_parameters) -> None:
    """I update the headcounts with a non valid value."""
    page_parameters.headcount(2, 'A').update_headcount()


@then('I should see the success message')
def success_merssage(page_parameters) -> None:
    """I should see the success message."""
    assert page_parameters.update_has_succeeded() is True


@then('I should see the error message')
def error_merssage(page_parameters) -> None:
    """I should see the error message."""
    assert page_parameters.update_has_failed() is True


@then('The update should be permanent')
def permanent_update(the_browser, the_config) -> None:
    """The update should be permanent."""
    p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
    sign_in(p_page_signin, UserAdminFactory().initialize(the_config["data"]["users"]))
    del p_page_signin
    p_page_parameters = PageParameters(browser=the_browser, config=the_config['urls'])
    assert p_page_parameters.visit() is True
    assert p_page_parameters.check_headcounts() is True
