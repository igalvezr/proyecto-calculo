import pytest

from analisis.analisis import obtener_coeficientes

@pytest.mark.parametrize("entrada, objetivo", [
    ("5x**2", {2: 5.0}),
    ("-3x", {1: -3.0}),
    ("5x**3 + 4x**2 - 2x +3", {3: 5.0, 2: 4.0, 1: -2.0, 0: 3.0})
])
def test_analizar(entrada, objetivo):
    assert obtener_coeficientes(entrada) == objetivo