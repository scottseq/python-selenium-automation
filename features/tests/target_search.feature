# Created by SSCOTT at 2/16/2024
Feature: Product search on Target.com
  # Enter feature description here

  Scenario: User can search for a product on target
    Given Open Target main page
    When Search for coffee
    Then Search results for coffee are shown
  
