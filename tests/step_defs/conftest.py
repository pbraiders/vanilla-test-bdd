"""
This module contains shared fixtures, steps, and hooks.
"""

import pytest
from selenium.webdriver import Chrome



@pytest.fixture
def browser():
  # Initialize ChromeDriver
  driver = Chrome()
  # Wait implicitly for elements to be ready before attempting interactions
  driver.implicitly_wait(10)
  # Return the driver object at the end of setup
  yield driver
  # For cleanup, quit the driver
  driver.quit()



#def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
#    print(f'Step failed: {step}')
