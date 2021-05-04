@admin @graphs
Feature: Try to access the graphs page.

    Scenario: Accessing the graphs page.
        When I am the admin user
        Then I can access to the graphs page

    Scenario Outline: Not accessing the graphs page.
        When I am the <type> user
        Then I cannot access to the graphs page

        Examples: Connecting
        | type        |
        | deactivated |
        | simple      |