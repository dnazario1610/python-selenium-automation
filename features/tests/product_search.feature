Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car Table into search field
    And Click on search icon
    Then Verify search result is correct