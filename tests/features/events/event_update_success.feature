@event
Feature: Event update, success cases
    SMART: ✔️

    Scenario: Update an event
        Given I am on an event page
        When I update data
        Then I should see the success message
        And I should see the update on the event page
