@event
Feature: Try to access the events page.
    SMART: ✔️

    Scenario Outline: Accessing the events page.
        When I am the <type> user
        Then I <permission> access to the events page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | can        |
        | deactivated | cannot     |
