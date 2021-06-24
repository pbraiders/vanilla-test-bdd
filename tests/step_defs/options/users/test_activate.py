# coding=utf-8
"""Activate deactivate user feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    parsers,
    scenario,
    then,
    when,
)
from pbraiders.pages.users_utilities import new_account  # pylint: disable=import-error
from pbraiders.pages.users_utilities import new_deactivated_account  # pylint: disable=import-error
from pbraiders.pages.signin_utilities import sign_in  # pylint: disable=import-error
from pbraiders.pages.options.users import UserPage  # pylint: disable=import-error
from pbraiders.pages.options.users.actions import UpdateUserAction  # pylint: disable=import-error
from pbraiders.user import UserFakerFactory  # pylint: disable=import-error

scenario = partial(scenario, 'options/users/activate.feature')


@scenario('Deactivate an user')
def test_deactivate():
    """Deactivate an user."""


@scenario('Activate an user')
def test_activate():
    """Activate an user."""


@given(parsers.parse('I am on the {status} user account page'), target_fixture="page_user")
def page_user(the_config, the_browser, the_database, the_faker, new_user, status) -> UserPage:
    """I am on an activated/deactivated user account page"""
    # Sign in as admin
    assert sign_in(driver=the_browser, config=the_config, user="admin") is True
    p_user = UserFakerFactory(_faker=the_faker).initialize(the_config["data"]["users"])
    # p_user = new_user

    # New account
    if "activated" == status:
        # Create an account
        assert new_account(driver=the_browser,
                           config=the_config['urls'],
                           user=p_user)
    else:
        # Create a deactivated account
        assert new_deactivated_account(driver=the_browser,
                                       config=the_config['urls'],
                                       user=p_user)

    # Go to this new user account page
    p_page = UserPage(_driver=the_browser,
                      _config=the_config['urls'],
                      _user=p_user)
    assert p_page.visit() is True

    # Chech the status
    if "activated" == status:
        assert p_page.checked() is True

    else:
        assert p_page.checked() is False

    return p_page


@when(parsers.parse('I {action} this user account'))
def change_status(page_user, action) -> None:
    """I activate/deactivate this user account."""
    p_action = UpdateUserAction(_page=page_user)

    if "deactivate" == action:
        p_action.uncheck()
    else:
        p_action.check()

    p_action.update()

    assert p_action.has_succeeded() is True


@then('I can sign in to this account again')
def can_sign_in(the_config, the_browser, page_user) -> None:
    """I can sign in to this account again."""
    assert sign_in(driver=the_browser, config=the_config, user=page_user.user.login, password=page_user.user.password) is True


@then('I cannot sign in to this account anymore')
def cannot_sign_in(the_config, the_browser, page_user) -> None:
    """I cannot sign in to this account anymore."""
    assert sign_in(driver=the_browser, config=the_config, user=page_user.user.login, password=page_user.user.password) is False
