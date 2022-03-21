Feature: Min-Max-Sum Problem

  Given five positive integers, find the minimum and maximum values that can be 
  calculated by summing exactly four of the five integers. Then print the 
  respective minimum and maximum values as a single line of two space-separated 
  long integers.

  Scenario: Array contains [1, 3, 5, 7, 9]

    Given I have an array with integers 1, 3, 5, 7 and 9
    When I calculate the minimum sum of 4 numbers
    Then I should get a result of 16
    When I calculate the maximum sum of 4 numbers
    Then I should get a result of 24
