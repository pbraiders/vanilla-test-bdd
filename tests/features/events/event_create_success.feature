@event @onlyone
Feature: Event creation, success cases
    SMART: ✔️

    Background:
        Given I am on the new event page

    Scenario: Create the event for a new contact
        When I create an event for a new contact
        Then I should see the success message
        And the event should appear on the event list
        And I should access to this event page
        And the contact should appear on the contact list
        And I should access to the contact page