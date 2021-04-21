@admin @usermgnt
Feature: User creation, success cases

    Background:
        Given I am on the users page
        And I have a new user to create

    Scenario: Create the user
        When I send the credential
        Then I should see the success message

    Scenario: Successfully sign in with a new created user
        When I successfully create the new user
        Then I can sign in to this new user account