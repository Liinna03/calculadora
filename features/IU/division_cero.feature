Feature: operaciones aritmeticas

  Scenario Outline: dividir entre cero
    Given que él usuario tiene un numero para dividir entre cero
    When envía el número del numerador y en denominador 0  <numero_numerador>
    Then el usuario debera ver mensaje de error

    Examples:
    |numero_numerador|
    |7|