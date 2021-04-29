@admin @usermgnt
Feature: Activate deactivate user.

    Scenario: Deactivate an user
        Given I am on the activated user account page
        When I deactivate this user account
        Then I cannot sign in to this account anymore

    Scenario: Activate an user
        Given I am on the deactivated user account page
        When I activate this user account
        Then I can sign in to this account again