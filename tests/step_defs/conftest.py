"""
This module contains shared fixtures, steps, and hooks.
"""

import pytest
#from selenium.webdriver import Chrome
from splinter import Browser


@pytest.fixture
def theBrowser():
  # Initialize ChromeDriver
  #driver = Browser('chrome', headless=True)
  pBrowser = Browser('chrome')
  #driver.maximize_window()
  # Wait implicitly for elements to be ready before attempting interactions
  #pBrowser.implicitly_wait(10)
  # Return the driver object at the end of setup
  yield pBrowser
  # For cleanup, quit the driver
  pBrowser.quit()



#def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
#    print(f'Step failed: {step}')
