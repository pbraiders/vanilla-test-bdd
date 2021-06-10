@signout
Feature: Sign out, success cases
    SMART: ✔️

    Scenario: Sign out
        Given I am using the app
        When I sign out of the app
        Then I should be disconnected
