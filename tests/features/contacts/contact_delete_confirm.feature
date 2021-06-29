@contact
Feature: Contact delete, confirm cases
    SMART: ✔️

    Scenario: Delete a contact
        Given I am on a contact page
        When I delete the contact
        Then I should see the success message
        And I should not access into the contact page
