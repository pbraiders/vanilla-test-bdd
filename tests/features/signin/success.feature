@signin
Feature: Successful Signin tests
    Successful Signin tests

    Scenario: Connect deactivated
        Given I am the deactivated user
        When I fill the credentials
        Then I should not be connected

    Scenario Outline: Connecting
        Given I am the <type> user
        When I fill the credentials
        Then I should be connected

        Examples: Connecting
        | type     |
        | admin    |
        | simple   |