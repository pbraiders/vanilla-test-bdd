@admin @parameters @purge
Feature: Delete old reservations failure cases.
    SMART: ✔️

    Background:
        Given I want to delete old reservations

    Scenario: No year
        When I do not enter a year
        Then I should see the error message

    Scenario Outline: Delete with an invalid year
        When I enter the <year>
        Then I should see the error message

        Examples: Deleting
        | year   |
        | 1999   |
        | future |
