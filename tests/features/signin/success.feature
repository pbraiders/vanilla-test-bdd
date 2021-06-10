@signin
Feature: Sign in, success cases
    SMART: ✔️

    Background:
        Given I am on the signin page

    Scenario: Account deactivated
        When I am the deactivated user
        Then I should not be connected

    Scenario Outline: Connecting
        When I am the <type> user
        Then I should be connected

        Examples: Connecting
        | type     |
        | admin    |
        | simple   |