@admin @usermgnt
Feature: User creation, failure cases
    SMART: ✔️

    Background:
        Given I am on the users page

    Scenario: Name is mandatory
        When I send the credential without the name
        Then I should see the error message

    Scenario: Password is mandatory
        When I send the credential without the password
        Then I should see the error message

    Scenario: Confirmed password is mandatory
        When I send the credential without the confirmed password
        Then I should see the error message

    Scenario: User already exists
        When I send the credential of an already existing user
        Then I should see the already exist error message
