"""
This module contains shared fixtures, steps, and hooks.
"""

import pytest
from splinter import Browser

@pytest.fixture
def theBrowser():
  #driver = Browser('chrome', headless=True)
  pBrowser = Browser('chrome')
  yield pBrowser
  pBrowser.quit()


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
