from enum import Enum


class TipoPuntos(Enum):
    Maximo = 1
    Minimo = 2
    Inflexion = 3

class Funcion:
    coeficientes: dict[int, float]
    puntos_criticos: list[tuple[TipoPuntos, float]]
    raices: list[float]

    def __init__(self, coeficientes: dict[int, float] = {}):
        if len(coeficientes) == 0:
            self.coeficientes = dict()
        else:
            self.coeficientes = coeficientes

        self.puntos_criticos = list()
        self.raices = list()

    def evlauar(self, x: float) -> float:
        resultado = 0
        for expon, coef in self.coeficientes.items():
            resultado += x**expon * coef
        return resultado
    
    def __str__(self) -> str:
        return f'función: [Coeficientes: {self.coeficientes}, raices: {len(self.raices)}]'
    
    def pretty(self) -> str:
        symbol = ''

        for expon, coef in self.coeficientes.items():
            if expon == 0:
                symbol += str(coef)
            else:
                symbol += f'{"+" if coef >= 0 else ""}{coef}x^{expon} '
        
        return symbol