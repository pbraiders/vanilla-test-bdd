@admin @graphs
Feature: Try to access the graphs page.
    SMART: ✔️
    
    Scenario Outline: Accessing the graphs page.
        When I am the <type> user
        Then I <permission> access to the graphs page

        Examples: Accessing
        | type        | permission |
        | admin       | can        |
        | simple      | cannot     |
        | deactivated | cannot     |