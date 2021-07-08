Feature: google search checking

  Background: common steps
    Given open browser


  @single
  Scenario: simple google search
    When search element with "Selenium"
    Then back to homepage

  @multi
  Scenario Outline: simple google search
    When search element with "<name>"
    Then back to homepage
    Examples:
      | name       |
      | Selenium   |
      | Python     |
