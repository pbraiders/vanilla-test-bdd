"""
This module contains shared fixtures, steps, and hooks.

Fixture scopes
Fixtures are created when first requested by a test, and are destroyed based on their scope:
    function: the default scope, the fixture is destroyed at the end of the test.
    class: the fixture is destroyed during teardown of the last test in the class.
    module: the fixture is destroyed during teardown of the last test in the module.
    package: the fixture is destroyed during teardown of the last test in the package.
    session: the fixture is destroyed at the end of the test session.

Hooks
    pytest_bdd_before_scenario(request, feature, scenario) - Called before scenario is executed
    pytest_bdd_after_scenario(request, feature, scenario) - Called after scenario is executed (even if one of steps has failed)
    pytest_bdd_before_step(request, feature, scenario, step, step_func) - Called before step function is executed and it’s arguments evaluated
    pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args) - Called before step function is executed with evaluated arguments
    pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args) - Called after step function is successfully executed
    pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception) - Called when step function failed to execute
    pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception) - Called when step lookup failed
"""

import json
import random
import pytest
from faker import Faker
from faker.providers import person
from faker.providers import address
from faker.providers import internet
from faker.providers import phone_number
from faker.providers import lorem
from splinter import Browser
from pbraiders.contact import Contact  # pylint: disable=import-error
from pbraiders.database.adapter import PyMySQLAdapterFactory  # pylint: disable=import-error
from pbraiders.user import User  # pylint: disable=import-error

CONFIG_PATH = 'config.json'


def pytest_addoption(parser):
    """Loads the command line args"""
    parser.addoption('--driver', action='store', default='chrome',
                     help='driver choices: chrome or firefox')


@pytest.fixture(scope="session")
def the_driver(pytestconfig):
    """Set the user defined driver"""
    return pytestconfig.getoption('driver')


@pytest.fixture(scope="session")
def the_config():
    """Loads the config file"""
    try:
        with open(CONFIG_PATH) as s_config:
            data = json.load(s_config)
    except OSError as err:
        print("OS error: {0}".format(err))
        raise
    return data


@pytest.fixture(scope="session")
def the_database(the_config):
    """Loads and initialize the database"""
    p_database = PyMySQLAdapterFactory().initialize(the_config['db'], the_config['data'])
    yield p_database
    p_database.quit()


@pytest.fixture(scope="session")
def the_browser(the_driver):
    """Loads firefox or chrome"""
    p_browser = Browser(the_driver, incognito=True, wait_time=3, headless=True)
    yield p_browser
    p_browser.quit()


@pytest.fixture(scope="module")
def the_faker() -> Faker:
    """Loads the faker"""
    # I do not use the default faker fixtures because it does not work. I can't do what I want to do
    # And if I follow the doc I've got many:
    #   NotImplementedError: Proxying calls to `add_provider` is not implemented in multiple locale mode.
    #   or any_non_session_scope' is not defined ...
    # Locale choice
    d_locales = {0: "fr_FR", 1: "ja_JP", 2: "ru_RU"}
    s_local = d_locales[random.randint(0, 2)]
    print(' \u2592 Faker locale choice:' + s_local)
    # Faker
    p_faker = Faker(s_local)
    p_faker.add_provider(lorem)
    p_faker.add_provider(person)
    p_faker.add_provider(address)
    p_faker.add_provider(internet)
    p_faker.add_provider(phone_number)
    p_faker.seed_instance(random.randint(0, 999))
    return p_faker


@pytest.fixture(scope="function")
def new_user(the_faker) -> User:
    """Generates user data."""
    s_name = the_faker.first_name()
    s_passwd = s_name + 'password'
    print('\u2592 Faker firstname:' + s_name)
    return User(login=s_name, password=s_passwd, passwordc=s_passwd)


@pytest.fixture(scope="function")
def new_contact(the_faker) -> Contact:
    """Generates contact data."""
    return Contact(
        lastname=the_faker.last_name(),
        firstname=the_faker.first_name(),
        tel=the_faker.phone_number(),
        email=the_faker.email(),
        address=the_faker.street_address(),
        address_more=the_faker.country(),
        city=the_faker.city(),
        zip=the_faker.postcode(),
        comment=the_faker.text())


def pytest_bdd_step_error(
        request,
        feature,
        scenario,
        step,
        step_func,
        step_func_args,
        exception) -> None:
    """Called when step function failed to execute"""
    print(f'Step failed: {step}')
