# coding=utf-8
"""Sign in utilities."""

from pbraiders.user import User
from pbraiders.signin import PageSignin


def sign_in(p_page_signin: PageSignin, p_user: User) -> None:
    """Sign in."""
    p_page_signin.set_user(p_user).visit().fill_name().fill_password().click()
    assert p_page_signin.connected() is True
