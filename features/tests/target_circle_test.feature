# Created by SSCOTT at 2/26/2024
Feature: Vaildate benefit boxes for Target Circle
  # Enter feature description here


  Scenario: Verify the 5 benefit boxes on target circle page
    Given Open Target Circle page
    When Search the benefit boxes
    Then Verify header has {expected_count} boxes