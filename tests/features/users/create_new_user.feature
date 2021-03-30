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

    Scenario: Confirmed password is mandatory when creating user
        Given I fill the username field
        And I fill the password field
        When I press the send button
        Then I should see the error message

    Scenario: Password is mandatory when creating user
        Given I fill the username field
        And I confirm the password field
        When I press the send button
        Then I should see the error message

    Scenario: Creating a new user
        Given I fill the username field
        And I fill the password field
        And I confirm the password
        When I press the send button
        Then I should see the activated user on the list
        And I should see the success message
