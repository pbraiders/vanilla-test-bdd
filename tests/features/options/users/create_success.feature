@admin @usermgnt
Feature: User creation, success cases
    SMART: ✔️

    Scenario: Create the user
        Given I am on the users page
        When I create a new user
        Then I should see the success message
        And I can sign in to this new user account
