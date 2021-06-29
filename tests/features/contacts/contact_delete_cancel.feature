@contact
Feature: Contact delete, cancel cases
    SMART: ✔️

    Scenario: Not deleting a contact
        Given I am on a contact page
        When I cancel the deletion of the contact
        Then I should still access into the contact page
