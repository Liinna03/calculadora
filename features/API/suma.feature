Feature: operaciones aritmeticas
  Scenario Outline: resta de dos números

    Given un usuario requiere realizar una "suma"
    When envia dos números <numero1>, <numero2>
    Then el resultado será <resultado>
    Examples:
      |numero1  | numero2  | resultado |
      |14       | 15         | 29 |
      |0.2      | 0.5       | 0.7 |
      |1        | 1         | 2 |