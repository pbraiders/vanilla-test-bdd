@contact
Feature: Contact creation, failure cases
    SMART: ✔️

    Background:
        Given I am on the new contact page

    Scenario: Lastname is mandatory
        When I send the data without the lastname
        Then I should see the error message

    Scenario: Firstname is mandatory
        When I send the data without the firstname
        Then I should see the error message

    Scenario: Phone number is mandatory
        When I send the data without the phone number
        Then I should see the error message
