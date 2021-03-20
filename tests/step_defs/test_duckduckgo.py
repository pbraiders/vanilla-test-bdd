"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

import pytest
from pytest_bdd import scenarios, scenario, given, when, then, parsers
#from selenium.webdriver.common.keys import Keys
# + Keys.RETURN

DDG_URL = 'https://www.duckduckgo.com'
SEARCH = 'splinter - python acceptance testing for web applications'

#scenarios('../features/duckduckgo.feature')

@scenario('duckduckgo.feature', 'Duckduckgo basic search')
def test_scenario_basic_search():
    pass

@given('I visit the duckduckgo homepage')
def visit_homepage(theBrowser):
    theBrowser.visit(DDG_URL)

@then('I can do a basic search')
def duckduckgo_basic_search(theBrowser):
    try:
        theBrowser.fill('q', SEARCH)
        theBrowser.click_link_by_id('search_button_homepage')
        assert theBrowser.is_text_present(SEARCH) == 1
        assert theBrowser.is_element_present_by_xpath(f"//div[@id='links']//*[contains(text(), 'splinter')]") == 1

        # Verify that the search phrase is the same
        assert theBrowser.find_by_id('search_form_input').first.value == SEARCH

    except e:
        print ("Oops, I failed with the status code %s and reason %s" % (e.status_code, e.reason))
