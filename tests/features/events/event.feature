@event
Feature: Try to access an event page.
    SMART: ✔️

    Background:
        Given One today's event

    Scenario Outline: Accessing an event page.
        When I am the <type> user
        Then I <permission> access to an event page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | can        |
        | deactivated | cannot     |
