@duckduckgo
Feature: basic search with duckduckgo
  As ...,
  I want to ...,
  So I can ....

  # Web scenarios can be highly declarative, which focuses on behavior.
  # Don't get caught up in button names and layouts at the Gherkin level.
  # Note that these scenarios use Selenium WebDriver to do browser interactions.

  Scenario: Duckduckgo basic search
    Given I visit the duckduckgo homepage
    Then I can do a basic search
