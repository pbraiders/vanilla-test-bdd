@admin @logs
Feature: Try to access the logs page.
    SMART: ✔️

    Scenario Outline: Accessing the logs page.
        When I am the <type> user
        Then I <permission> access to the logs page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | cannot     |
        | deactivated | cannot     |