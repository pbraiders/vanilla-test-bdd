@admin @usermgnt
Feature: Try to access the users page.

    Scenario: Accessing the users page.
        When I am the admin user
        Then I can access to the users page

    Scenario Outline: Not accessing the users page.
        When I am the <type> user
        Then I cannot access to the users page

        Examples: Connecting
        | type        |
        | deactivated |
        | simple      |