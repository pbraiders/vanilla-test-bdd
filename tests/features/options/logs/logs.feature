@admin @logs
Feature: Try to access the logs page.

    Scenario: Accessing the logs page.
        When I am the admin user
        Then I can access to the logs page

    Scenario Outline: Not accessing the logs page.
        When I am the <type> user
        Then I cannot access to the logs page

        Examples: Connecting
        | type        |
        | deactivated |
        | simple      |