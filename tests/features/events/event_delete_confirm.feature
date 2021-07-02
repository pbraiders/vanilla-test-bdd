@event @onlyone
Feature: Event delete, confirm cases
    SMART: ✔️

    Scenario: Delete an event
        Given I am on a event page
        When I delete the event
        Then I should see the success message
        And I should not access into the event page anymore
