@admin @usermgnt
Feature: Try to access the users page.
    SMART: ✔️
    
    Scenario Outline: Accessing the users page.
        When I am the <type> user
        Then I <permission> access to the users page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | cannot     |
        | deactivated | cannot     |