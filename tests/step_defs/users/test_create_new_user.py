# coding=utf-8
"""Creating a new user feature tests."""

from functools import partial
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from pbraiders.signin.PageSignin import PageSignin
from pbraiders.signin.UserFactories import AdminUserFactory
from pbraiders.users.PageUsers import PageUsers
from pbraiders.parameters.PageParameters import PageParameters

scenario = partial(scenario, 'users/create_new_user.feature')


@scenario('Name is mandatory when creating user')
def test_name_is_mandatory():
    """Name is mandatory when creating user."""


@given('I am on the users page', target_fixture="users_page")
def users_page(theConfig, theBrowser):
    """I am logged in as the administrator."""
    pPage = PageSignin(browser=theBrowser, config=theConfig['urls'], user=AdminUserFactory().initialize(theConfig))
    pPage.connectSuccess()
    del pPage
    #pPage = PageParameters(browser=theBrowser, config=theConfig['urls'])
    # pPage.goTo()
    #del pPage
    pPage = PageUsers(browser=theBrowser, config=theConfig['urls'])
    pPage.goTo()
    # theBrowser.visit('http://www.pbraiders.local/login.php')
    # session_browser.visit('https://www.pbraiders.fr/login.php')
    # session_browser.find_by_id('loginusr').first.fill(str(pUser.login))
    # session_browser.find_by_id('loginpwd').first.fill(str(pUser.password))
    # session_browser.find_by_name('login').first.click()
    # session_browser.visit('https://www.pbraiders.fr/users.php')
    #assert theBrowser.title == 'PBRaiders - Connexion'
    # theBrowser.find_by_id('loginusr').first.fill(str(pUser.login))
    # theBrowser.find_by_id('loginpwd').first.fill(str(pUser.password))
    # theBrowser.find_by_name('login').first.click()
    #assert theBrowser.is_text_present('Connecté en tant que {}'.format(pUser.login), wait_time=2) == True
    # theBrowser.visit('https://www.pbraiders.local/users.php')
    assert theBrowser.title == 'PBRaiders - Utilisateurs'
    # return pPage


@given('I confirm the password')
def confirm_password():
    """I confirm the password."""
    raise NotImplementedError


@given('I fill the password field')
def i_fill_the_password_field():
    """I fill the password field."""
    raise NotImplementedError


@when('I press the send button')
def i_press_the_send_button():
    """I press the send button."""
    raise NotImplementedError


@then('I should see the error message')
def i_should_see_the_error_message():
    """I should see the error message."""
    raise NotImplementedError
