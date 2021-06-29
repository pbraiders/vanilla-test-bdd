# coding=utf-8
"""Delete old reservations success cases."""

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

scenario = partial(scenario, 'options/parameters/purge_success.feature')


@scenario('Confirm the deletion')
def test_purge_confirm_deletion():
    """Confirm the deletion."""


@scenario('Cancel the deletion')
def test_purge_cancel_deletion():
    """Cancel the deletion."""


@given('I want to delete old reservations', target_fixture="page_parameters")
def page_parameters(the_browser, the_config, the_database) -> PurgeAction:
    """I want to delete old reservations."""
    # Parameters page
    p_page = ParametersPage(_driver=the_browser, _config=the_config['urls'])
    if p_page.on_page() is False and p_page.visit() is False:
        # Signin
        assert sign_in(driver=the_browser, config=the_config, user="admin") is True
        assert p_page.visit() is True
    p_action = PurgeAction(_page=p_page)
    p_action.fill(str(date.today().year)).purge()
    return p_action


@when('I confirm the deletion')
def confirm_deletion(page_parameters) -> None:
    """I confirm the deletion."""
    assert page_parameters.on_confirm_page() is True
    page_parameters.confirm()


@when('I cancel the deletion')
def cancel_deletion(page_parameters) -> None:
    """I cancel the deletion."""
    assert page_parameters.on_confirm_page() is True
    page_parameters.cancel()


@then('I should see the success message')
def success_message(page_parameters) -> None:
    """I should see the success message."""
    assert page_parameters.has_succeeded() is True


@then('I should not see any message')
def no_message(page_parameters) -> None:
    """I should not see any message."""
    assert page_parameters.has_succeeded() is False and page_parameters.has_failed() is False
