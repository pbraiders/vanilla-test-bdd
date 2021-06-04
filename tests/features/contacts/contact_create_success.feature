@contact @onlyone
Feature: Contact creation, success cases

    Scenario: Create the contact
        Given I am on the new contact page
        When I create a new contact
        Then I should see the success message
