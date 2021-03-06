@contact
Feature: Try to access the contacts page.
    SMART: ✔️

    Scenario Outline: Accessing the contacts page.
        When I am the <type> user
        Then I <permission> access to the contacts page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | can        |
        | deactivated | cannot     |
