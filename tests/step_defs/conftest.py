"""
This module contains shared fixtures, steps, and hooks.
"""

import json
import pytest
from splinter import Browser
from types import SimpleNamespace

CONFIG_PATH = 'config.json'


def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default='chrome',
                     help='driver choices: chrome or firefox')


@pytest.fixture(scope="session")
def theDriver(pytestconfig):
    return pytestconfig.getoption('driver')


@pytest.fixture
def theBrowser(theDriver):
    pBrowser = Browser(theDriver, incognito=True, wait_time=2, headless=False)
    yield pBrowser
    pBrowser.quit()


@pytest.fixture(scope="session")
def theConfig():
    with open(CONFIG_PATH) as sConfig:
        data = json.load(sConfig)
    return data


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
