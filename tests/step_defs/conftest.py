"""
This module contains shared fixtures, steps, and hooks.

Fixture scopes
Fixtures are created when first requested by a test, and are destroyed based on their scope:
    function: the default scope, the fixture is destroyed at the end of the test.
    class: the fixture is destroyed during teardown of the last test in the class.
    module: the fixture is destroyed during teardown of the last test in the module.
    package: the fixture is destroyed during teardown of the last test in the package.
    session: the fixture is destroyed at the end of the test session.
"""


import json
import pytest
from splinter import Browser
from types import SimpleNamespace
from pbraiders.login.User import User

CONFIG_PATH = 'config.json'


def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default='chrome',
                     help='driver choices: chrome or firefox')


@pytest.fixture(scope="session")
def theDriver(pytestconfig):
    return pytestconfig.getoption('driver')


@pytest.fixture(scope="module")
def theBrowser(theDriver):
    pBrowser = Browser(theDriver, incognito=True, wait_time=2, headless=False)
    yield pBrowser
    pBrowser.quit()

@pytest.fixture(scope="module")
def theUser():
    pUser = User
    return pUser

@pytest.fixture(scope="session")
def theConfig():
    data = '{}'
    try:
        with open(CONFIG_PATH) as sConfig:
            data = json.load(sConfig)
    except:
        print(f'Something goes wrong when loading data from the config file: {CONFIG_PATH}')
    return data


"""
Hooks
    pytest_bdd_before_scenario(request, feature, scenario) - Called before scenario is executed
    pytest_bdd_after_scenario(request, feature, scenario) - Called after scenario is executed (even if one of steps has failed)
    pytest_bdd_before_step(request, feature, scenario, step, step_func) - Called before step function is executed and it’s arguments evaluated
    pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args) - Called before step function is executed with evaluated arguments
    pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args) - Called after step function is successfully executed
    pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception) - Called when step function failed to execute
    pytest_bdd_step_func_lookup_error(request, feature, scenario, step, exception) - Called when step lookup failed
"""


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
