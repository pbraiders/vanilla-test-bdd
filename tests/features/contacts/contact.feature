@contact
Feature: Try to access the contact page.
    SMART: ✔️

    Scenario Outline: Accessing the contact page.
        When I am the <type> user
        Then I <permission> access to the contact page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | can        |
        | deactivated | cannot     |
