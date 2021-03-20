"""
This module contains shared fixtures, steps, and hooks.
"""

import pytest
from splinter import Browser

def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default='chrome', help='drivers choice: chrome or firefox')

@pytest.fixture(scope="session", autouse=True)
def driver(pytestconfig):
    yield pytestconfig.getoption('driver')

@pytest.fixture
def theBrowser(driver):
  #driver = Browser('driver', headless=True)
  pBrowser = Browser(driver)
  yield pBrowser
  pBrowser.quit()

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
