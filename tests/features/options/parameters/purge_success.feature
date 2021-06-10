@admin @parameters @purge
Feature: Delete old reservations success cases.
    SMART: ❌

    Background:
        Given I want to delete old reservations

    Scenario: Confirm the deletion
        When I confirm the deletion
        Then I should see the success message

    Scenario: Cancel the deletion
        When I cancel the deletion
        Then I should not see any message
