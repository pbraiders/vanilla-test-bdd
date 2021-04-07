@admin @usermgnt
Feature: Creating a new user
    administrator tool.

    Background:
        Given I am logged in as the administrator
        And I am on the users page

    Scenario: Name is mandatory when creating user
        Given I fill the password field
        And I confirm the password
        When I press the send button
        Then I should see the error message
