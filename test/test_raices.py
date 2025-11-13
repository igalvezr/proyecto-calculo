import pytest

from analisis.Funcion import Funcion
from analisis.analisis import obtener_coeficientes
from analisis.derivación import derivar
from analisis.raices import obtener_raices

@pytest.mark.parametrize("entrada, objetivo", [
    (Funcion(coeficientes={2: 3.0, 1: -6.0, 0: -9.0}), set([-1, 3])),
    (Funcion(coeficientes={3: 1.0, 2: 2.0, 1: -15.0}), set([0, 3, -5]))
])
def test_raices(entrada, objetivo):
    raices = obtener_raices(entrada)
    print(f'En test: función: {entrada.pretty()}, Raices: ', raices)
    assert set(raices) == objetivo