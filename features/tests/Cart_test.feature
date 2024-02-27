# Created by SSCOTT at 2/26/2024
Feature: Target.com cart and verify sign
  # Enter feature description here

  Scenario: Your cart empty
  Given Open Target main page
  When click on the cart icon
  Then Verify 'Your cart is empty' message is displayed

  Scenario: Sign in
  Given Open Target main page
  When locate sign in
  Then click sign in
    # Enter steps here