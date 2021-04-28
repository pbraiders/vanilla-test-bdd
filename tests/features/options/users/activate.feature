@admin @usermgnt @onlyone
Feature: Activate deactivate user.

    Scenario: Deactivate an user
        Given I am on an activated user account page
        When I deactivate this user
        Then I cannot sign in to this account

    Scenario: Activate an user
        When I activate the simple user account
        Then I can sign in to this account