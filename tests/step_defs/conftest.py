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
import pytest
from pbraiders.database.adapter import PyMySQLAdapterFactory
from splinter import Browser

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
    data = '{}'
    try:
        with open(CONFIG_PATH) as s_config:
            data = json.load(s_config)
    except:
        print(f'Something goes wrong when loading data from the config file: {CONFIG_PATH}')
    return data


@pytest.fixture(scope="session")
def the_database(the_config):
    """Loads and initialize the database"""
    p_database = PyMySQLAdapterFactory().initialize(the_config['db'], the_config['data'])
    yield p_database
    p_database.quit()


@pytest.fixture(scope="module")
def the_browser(the_driver):
    """Loads firefox or chrome"""
    p_browser = Browser(the_driver, incognito=True, wait_time=2, headless=False)
    yield p_browser
    p_browser.quit()


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """Called when step function failed to execute"""
    print(f'Step failed: {step}')
