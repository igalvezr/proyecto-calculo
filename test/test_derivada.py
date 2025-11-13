import pytest

from analisis.Funcion import Funcion
from analisis.analisis import obtener_coeficientes
from analisis.derivación import derivar

@pytest.mark.parametrize("entrada, objetivo", [
    (Funcion(coeficientes={2: 3.0, 1: -2.0, 0: 5}), {1: 6.0, 0: -2.0})
])
def test_analizar(entrada, objetivo):
    derivada = derivar(entrada)
    #print('Derivada: ', derivada)
    assert derivada.coeficientes == objetivo