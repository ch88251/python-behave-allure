Feature: Repeated String

  Scenario Outline: Find the number of occurrences of the letter "a" in a repeating string

    Given a string <s> that can repeat indefinitely, and an integer <n> for the number of letters to evaluate
    When I execute the repeated_string function
    Then the repeated_string function should return the value <count>

    Examples:
      |s            |n | count |
      |abcac        |10| 4     |
      |abc          |10| 4     |
      |bcba         |10| 2     |
