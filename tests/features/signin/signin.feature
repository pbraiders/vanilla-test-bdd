@admin @signin
Feature: Signin error tests
    Signin error tests.

    Background:
        Given I am on the signin page

    Scenario: I have no credentials
        When I press the connect button
        Then I should see the error message

    Scenario: I have no username
        Given I fill the password field
        When I press the connect button
        Then I should see the error message

    Scenario: I have no password
        Given I fill the username field
        When I press the connect button
        Then I should see the error message