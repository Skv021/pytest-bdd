Feature: The dummy feature

  Scenario: Its a dummy scenario
    Given I login app
    When I enter username
    And I enter password
    And I click on Submit
    Then I should be logged in
    And I pass 5 as arg