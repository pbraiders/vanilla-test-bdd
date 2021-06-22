# coding=utf-8
"""Users utilities."""

from splinter.driver import DriverAPI
from pbraiders.user import User
from pbraiders.pages.options.users import UsersPage
from pbraiders.pages.options.users.actions import CreateUserAction
from pbraiders.pages.options.users.actions import FillUserAction


def new_account(driver: DriverAPI, config: dict, user: User) -> bool:
    """Creates an user.
       config=config['urls']"""

    # Visit the users page
    p_page = UsersPage(_driver=driver, _config=config)
    assert p_page.visit() is True

    # Fill the fields
    p_page.set_user(user)
    p_action = FillUserAction(_page=p_page)
    p_action.fill_name() \
            .fill_password() \
            .confirm_password()
    del p_action

    # Create
    p_action = CreateUserAction(_page=p_page)
    p_action.click()

    return p_action.has_succeeded() is True and p_page.is_on_list() is True
