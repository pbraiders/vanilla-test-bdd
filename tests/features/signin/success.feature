@signin
Feature: Sign in, success cases
    SMART: ✔️

    Scenario Outline: Sign in
        Given I am the <type> user
        When I sign in to the app
        Then I <permission> access to the main page

        Examples: Connecting
        | type        | permission |
        | admin       | can        |
        | simple      | can        |
        | deactivated | cannot     |