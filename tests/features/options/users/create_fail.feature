@admin @usermgnt
Feature: Fail to create a new user
    administrator tool for creating user.

    Background:
        Given I am on the users page

    Scenario: Name is mandatory when creating user
        Given I enter the credential but not the name
        When I press the send button
        Then I should see the error message

    Scenario: Password is mandatory when creating user
        Given I enter the credential but not the password
        When I press the send button
        Then I should see the error message

    Scenario: Confirmed password is mandatory when creating user
        Given I enter the credential but not the confirmed password
        When I press the send button
        Then I should see the error message
