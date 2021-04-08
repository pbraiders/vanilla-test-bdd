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
from pbraiders.signin.UserFactories import AdminFactory
from pbraiders.users.PageUsers import PageUsers

scenario = partial(scenario, 'users/create_new_user.feature')


@scenario('Name is mandatory when creating user')
def test_name_is_mandatory():
    """Name is mandatory when creating user."""


@given('I am on the users page', target_fixture="users_page")
def users_page(theBrowser, theConfig):
    """I am logged in as the administrator."""
    #pPage = PageSignin(browser=theBrowser, config=theConfig['urls'], user=AdminFactory().initialize(theConfig))
    # if pPage.connected() == False:
    #    pPage.connectSuccess()
    #del pPage
    #pPage = PageUsers(browser=theBrowser, config=theConfig['urls'])
    # pPage.goTo()
    pUser = AdminFactory().initialize(theConfig)
    theBrowser.visit('http://www.pbraiders.local/login.php')
    assert theBrowser.title == 'PBRaiders - Connexion'
    theBrowser.find_by_id('loginusr').first.fill(str(pUser.login))
    theBrowser.find_by_id('loginpwd').first.fill(str(pUser.password))
    theBrowser.find_by_name('login').first.click()
    assert theBrowser.is_text_present('Connecté en tant que {}'.format(pUser.login), wait_time=2) == True
    theBrowser.visit('https://www.pbraiders.local/users.php')
    #assert theBrowser.title == 'PBRaiders - Utilisateurs'
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
