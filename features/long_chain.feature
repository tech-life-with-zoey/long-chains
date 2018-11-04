Feature: Calculate Long Chains

   As an introduction to serverless design and Alexa skill development, an integer is provided, the cubed value should be calculated.

  Scenario Outline: Cube an Integer
    Given a <number>
    When the long chain is computed
    Then the expected result <cube> is the cube created when each side is the number and should be returned

    Examples: Simple Integers
    | number | cube |
    | 1 | 1 |
    | 2 | 8 |
    | 3 | 27 |
    | 4 | 64 |
    | 5 | 125 |
    | 6 | 216 |
    | 7 | 343 |
    | 8 | 512 |
    | 9 | 729 |
    | 10 | 1000 |
