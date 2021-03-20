"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers
from selenium.webdriver.common.keys import Keys

DDG_URL = 'https://www.duckduckgo.com'
SEARCH = 'panda'

#scenarios('../features/duckduckgo.feature')

@scenario('../features/duckduckgo.feature', 'Duckduckgo basic search')
def test_scenario_basic_search():
    pass

@given('I visit the duckduckgo homepage')
def visit_homepage(browser):
    browser.get(DDG_URL)

@then('I can do a basic search')
def duckduckgo_basic_search(browser):
  # Find the search input element
  # In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
  search_input = browser.find_element_by_id('search_form_input_homepage')

  # Send a search phrase to the input and hit the RETURN key
  search_input.send_keys(SEARCH + Keys.RETURN)

  # Verify that results appear on the results page
  link_divs = browser.find_elements_by_css_selector('#links > div')
  assert len(link_divs) > 0

  # Verify that at least one search result contains the search phrase
  xpath = f"//div[@id='links']//*[contains(text(), '{SEARCH}')]"
  phrase_results = browser.find_elements_by_xpath(xpath)
  assert len(phrase_results) > 0

  # Verify that the search phrase is the same
  search_input = browser.find_element_by_id('search_form_input')
  assert search_input.get_attribute('value') == SEARCH
