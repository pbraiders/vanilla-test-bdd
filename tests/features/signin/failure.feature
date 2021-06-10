@signin
Feature: Sign in, failure cases
    SMART: ✔️

    Background:
        Given I am on the signin page

    Scenario: Credential is mandatory
        When I send no credential
        Then I should see the error message

    Scenario: Name is mandatory
        When I send the credential without the name
        Then I should see the error message

    Scenario: Password is mandatory
        When I send the credential without the password
        Then I should see the error message

    Scenario: Right password is mandatory
        When I send the credential with a wrong password
        Then I should see the error message
