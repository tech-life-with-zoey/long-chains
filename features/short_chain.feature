Feature: Calculate Short Chains

   As an introduction to serverless design and Alexa skill development, an integer is provided, the square should be calculated.

  Scenario Outline: Square an Integer
    Given a <number>
    When the short chain is computed
    Then the expected product <product> of the number and itself should be returned

    Examples: Simple Integers
    | number | product |
    | 1 | 1 |
    | 2 | 4 |
    | 3 | 9 |
    | 4 | 16 |
    | 5 | 25 |
    | 6 | 36 |
    | 7 | 49 |
    | 8 | 64 |
    | 9 | 81 |
    | 10 | 100 |
