Feature: Initial Verdict Functionality

  Scenario: Verify guilty verdict functionality
    Given the user opens the url
    And the user clicks the start button
    And the user clicks a case study
    And the user is ready to judge
    And the user selects guilty
    When the user votes
    Then the verdict modal should display with the result "Guilty" via text on the modal.

  Scenario: Verify Not Guilty verdict functionality
    Given the user opens the url
    And the user clicks the start button
    And the user clicks a case study
    And the user is ready to judge
    And the user selects not guilty
    When the user votes
    Then the verdict modal should display with the result "Not Guilty" via text on the modal.

  Scenario: Verify Vote button is disabled until the user selects a verdict from the radio buttons
    Given the user opens the url
    And the user clicks the start button
    And the user clicks a case study
    And the user is ready to judge
    Then the vote button is disabled

  Scenario: Verify Vote button is enabled when the user selects a verdict from the radio buttons
    Given the user opens the url
    And the user clicks the start button
    And the user clicks a case study
    And the user is ready to judge
    Then the vote button is disabled
    Given the user selects not guilty
    Then the vote button is enabled
