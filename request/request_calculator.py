import requests


def solicitud_operacion(url, payload):
    response = requests.post(url, json=payload)
    print("AAA", response)
    resultado = response.json()["value"]
    return resultado
