@contact
Feature: Try to access the new contact page.
    SMART: ✔️

    Scenario Outline: Accessing the new contact page.
        When I am the <type> user
        Then I <permission> access to the new contact page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | can        |
        | deactivated | cannot     |
