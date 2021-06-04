@admin @parameters
Feature: Try to access the parameters page.

    Scenario Outline: Accessing the parameters page.
        When I am the <type> user
        Then I <permission> access to the parameters page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | cannot     |
        | deactivated | cannot     |