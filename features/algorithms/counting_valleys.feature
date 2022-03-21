Feature: Counting Valleys

  Scenario Outline: A hiker follows a sequence of steps

    Given a hiker follows the sequence "<sequence>" with <steps> steps
    When the hiker follows the steps
    Then the total number of valleys crossed is <valleys>

    Examples:
      |steps|sequence|valleys|
      |8  |UDDDUDUU    |1|
      |12 |DDUUDDUDUUUD|2|
