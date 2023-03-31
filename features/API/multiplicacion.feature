Feature: operaciones aritmeticas
  Scenario Outline: multiplicacion de dos números

    Given un usuario requiere realizar una "multiplicacion"
    When envia dos números <numero1>, <numero2>
    Then el resultado será <resultado>
    Examples:
      |numero1  | numero2  | resultado|
      |14       | 15       | 210 |
      |0.2      | 0.5      | 0.1 |
      |1        | 1        | 1|