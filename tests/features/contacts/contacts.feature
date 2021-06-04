@contact @onlyone
Feature: Try to access the contact pages.

    Scenario Outline: Accessing the contacts page.
        When I am the <type> user
        Then I <permission> access to the contacts page

        Examples: Connecting
        | type        | permission |
        | admin       | can        |
        | simple      | can        |
        | deactivated | cannot     |
