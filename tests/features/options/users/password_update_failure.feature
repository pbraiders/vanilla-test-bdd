@admin @usermgnt
Feature: Password update, failure cases
    SMART: ✔️

    Background:
        Given I am on the simple user account page

    Scenario: Password is mandatory
        When I send the credential without the password
        Then I should see the error message

    Scenario: Confirmed password is mandatory
        When I send the credential without the confirmed password
        Then I should see the error message

    Scenario: Password and confirmed password must be the same
        When I send the credential with a different confirmed password
        Then I should see the error message
