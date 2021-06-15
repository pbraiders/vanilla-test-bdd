@contact
Feature: Contact delete, success cases
    SMART: ✔️

    Scenario: Delete a contact
        Given I am on a contact page
        When I delete the contact
        Then I should see the success message
        And I should not see the contact on the list anymore
