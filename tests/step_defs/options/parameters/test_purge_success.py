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
from pbraiders.options.parameters import PageParameters  # pylint: disable=import-error
from pbraiders.options.parameters import PagePurge  # pylint: disable=import-error
from pbraiders.signin import PageSignin  # pylint: disable=import-error
from pbraiders.signin import sign_in  # pylint: disable=import-error
from pbraiders.user import UserAdminFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/parameters/purge_success.feature')


@scenario('Confirm the deletion')
def test_purge_confirm_deletion():
    """Confirm the deletion."""


@scenario('Cancel the deletion')
def test_purge_cancel_deletion():
    """Cancel the deletion."""


@given('I want to delete old reservations', target_fixture="page_parameters")
def page_parameters(the_browser, the_config, the_database) -> PageParameters:
    """I want to delete old reservations."""
    # Parameters page
    p_page_parameters = PageParameters(browser=the_browser, config=the_config['urls'])
    if p_page_parameters.on_page() is False and p_page_parameters.visit() is False:
        # Signin
        p_page_signin = PageSignin(browser=the_browser, config=the_config['urls'], user=None)
        sign_in(p_page_signin, UserAdminFactory().initialize(the_config["data"]["users"]))
        del p_page_signin
        assert p_page_parameters.visit() is True
    p_page_parameters.purge(str(date.today().year))
    return p_page_parameters


@when('I confirm the deletion')
def confirm_deletion(the_browser, page_parameters) -> None:
    """I confirm the deletion."""
    p_page_confirmation = PagePurge(browser=the_browser, year=str(date.today().year))
    assert p_page_confirmation.on_page() is True
    p_page_confirmation.confirm()


@when('I cancel the deletion')
def cancel_deletion(the_browser, page_parameters) -> None:
    """I cancel the deletion."""
    p_page_confirmation = PagePurge(browser=the_browser, year=str(date.today().year))
    assert p_page_confirmation.on_page() is True
    p_page_confirmation.cancel()


@ then('I should see the success message')
def success_message(page_parameters) -> None:
    """I should see the success message."""
    assert page_parameters.on_page() is True and page_parameters.purge_has_succeeded() is True


@ then('I should not see any message')
def no_message(page_parameters) -> None:
    """I should not see any message."""
    assert page_parameters.on_page() is True and page_parameters.purge_has_succeeded(
    ) is False and page_parameters.purge_has_failed() is False
