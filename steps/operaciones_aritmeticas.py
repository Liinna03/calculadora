import requests
from behave import *

from request.request_calculator import solicitud_operacion

resultado_operacion = 0
url = ''


@given('un usuario requiere realizar una "{text}"')
def step_impl(context, text):
    global url
    if text == "suma":
        url = context.config.userdata.get("endpoint_suma")
    elif text == "resta":
        url = context.config.userdata.get("endpoint_resta")
    elif text == "multiplicacion":
        url = context.config.userdata.get("endpoint_multiplicacion")
    elif text == "division":
        url = context.config.userdata.get("endpoint_division")


@when('envia dos números {numero1}, {numero2}')
def step_impl(context, numero1, numero2):
    global resultado_operacion, url
    payload = {'firstDecimal': numero1, 'secondDecimal': numero2}
    resultado_operacion = solicitud_operacion(url, payload)


@then('el resultado será {resultado}')
def step_impl(context, resultado):
    assert resultado == str(resultado_operacion)
