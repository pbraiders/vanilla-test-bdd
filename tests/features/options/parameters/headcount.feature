@admin @parameters @headcount
Feature: Update the maximum headcount per month.
    SMART: ✔️

    Background:
        Given I want to update the headcount per month

    Scenario: Updating the headcounts
        When I update the headcounts
        Then I should see the success message
        And The update should be permanent

    Scenario: Not using a valid value
        When I update the headcounts with a non valid value
        Then I should see the error message