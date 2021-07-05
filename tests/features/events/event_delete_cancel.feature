@event
Feature: Event delete, cancel cases
    SMART: ✔️

    Scenario: Not deleting an event
        Given I am on a event page
        When I cancel the deletion of the event
        Then I should still access into the event page
