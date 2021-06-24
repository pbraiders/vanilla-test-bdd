@contact @onlyone
Feature: Contact update, success cases
    SMART: ✔️

    Scenario: Update a contact
        Given I am on a contact page
        When I update data
        Then I should see the success message
        And I should see the update on the contacts list
        And I should see the update on the contact page