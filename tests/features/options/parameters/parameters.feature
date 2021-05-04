@admin @parameters
Feature: Try to access the parameters page.

    Scenario: Accessing the parameters page.
        When I am the admin user
        Then I can access to the parameters page

    Scenario Outline: Not accessing the parameters page.
        When I am the <type> user
        Then I cannot access to the parameters page

        Examples: Connecting
        | type        |
        | deactivated |
        | simple      |