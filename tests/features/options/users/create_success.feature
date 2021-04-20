@admin @usermgnt
Feature: Creating a new user
    administrator tool for creating user.

    Scenario: I successfully created a new user
        Given I am on the users page
        When I send the new credential
        Then I should see the success message

    Scenario: I successfully sign in with a new created user
        Given I am on the users page
        When I successfully create the new user
        Then I can sign in to this new user account