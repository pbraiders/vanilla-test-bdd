@contact @onlyone
Feature: Contact creation, success cases
    SMART: ✔️

    Scenario: Create the contact
        Given I am on the new contact page
        And I have a new contact to create
        When I create the contact
        Then I should see the success message
        And It should appear on the contact list
        And I should access to this contact page