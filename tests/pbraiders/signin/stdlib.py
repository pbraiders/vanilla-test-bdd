# coding=utf-8
"""Sign in utilities."""

from pbraiders.user import User
from pbraiders.signin import PageSignin


def sign_in(p_page_signin: PageSignin, p_user: User) -> None:
    """Sign in."""
    assert p_page_signin.visit() is True
    p_page_signin.set_user(p_user).fill_credential().click()
    assert p_page_signin.connected() is True
