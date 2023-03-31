from behave import *

from pages.calculadora import ConsultarCalculadoraPage


@given('que él usuario tiene un numero para dividir entre cero')
def step_impl(context):
    pass


@when('envía el número del numerador y en denominador 0  {numero_numerador}')
def step_impl(context, numero_numerador):
    division = ConsultarCalculadoraPage(context.driver)
    division.click_digito(numero_numerador)
    division.click_btn_dividir()
    division.click_digito("0")
    division.click_btn_igual()


@then('el usuario debera ver mensaje de error')
def step_impl(context):
    confirmar_resultado = ConsultarCalculadoraPage(context.driver)
    assert confirmar_resultado.get_resultado()
