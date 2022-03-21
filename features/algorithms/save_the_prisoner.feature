Feature: Save The Prisoner

  Scenario Outline: 5 prisoners, 2 sweets, starting with chair 1

    Given there are <prisoners> prisoners, <sweets> sweets and I start with chair <start_chair>
    When the prison guard distributes the sweets
    Then the prisoner at chair <end_chair> will receive the bad sweet

    Examples:
      |prisoners|sweets|start_chair|end_chair|
      |5        |2     |1          |2        |
      |5        |2     |2          |3        |
