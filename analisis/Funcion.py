from enum import Enum

from analisis.es_cero import es_cercano, es_cero


class TipoPuntos(Enum):
    Maximo = 1
    Minimo = 2
    Inflexion = 3

class Funcion:
    coeficientes: dict[int, float]
    puntos_criticos: list[tuple[TipoPuntos, float]]
    raices: list[float]

    def __init__(self, coeficientes: dict[int, float] = {}):
        self.coeficientes = dict()

        self.puntos_criticos = list()
        self.raices = list()

        self.establecer_coeficientes(coeficientes)
    
    def establecer_coeficientes(self, coeficientes: dict[int, float] = {}):
        self.coeficientes = coeficientes

        # Normalizar los coeficientes
        if len(self.coeficientes) > 0:
            coef_max = max(self.coeficientes.keys())
            for exp in range(0, coef_max + 1):
                if exp not in self.coeficientes:
                    self.coeficientes[exp] = 0.0
        
        # Ordenar los valores
        self.coeficientes = dict(sorted(self.coeficientes.items(), reverse=True))
    
    def evaluar(self, x: float) -> float:
        resultado = 0
        for expon, coef in self.coeficientes.items():
            resultado += x**expon * coef
        return resultado
    
    def __str__(self) -> str:
        return f'función: [Coeficientes: {self.coeficientes}, raices: {len(self.raices)}]'
    
    def pretty(self) -> str:
        symbol = ''

        for expon, coef in self.coeficientes.items():
            if es_cero(coef):
                continue
            if expon == 0:
                symbol += str(coef) if not es_cercano(coef, 1) else ''
            else:
                symbol += f'{"+" if coef >= 0 else ""}{coef if not es_cercano(coef, 1) else ''}x^{expon} '
        
        return symbol
    
    def obtener_coeficientes_no_nulos(self):
        coef_no_nulos = dict()
        for exp, coef in self.coeficientes.items():
            if not es_cero(coef):
                coef_no_nulos[exp] = coef
        
        return coef_no_nulos
    
    def to_latex(self) -> str:
        # Retornar un string con sintaxis LaTeX válida
        simbolo = ''

        for expon, coef in self.coeficientes.items():
            if es_cercano(coef, 0):
                continue
            if expon == 0:
                simbolo += f'{"-" if coef < 0 else "+"}{abs(coef)}'
                continue
            if es_cercano(coef, 1):
                simbolo += f'+x^{{{expon}}}'
                continue
            if es_cercano(coef, -1):
                simbolo += f'{"-" if coef < 0 else "+"}x^{{{expon}}}'
                continue
            simbolo += f'{"-" if coef < 0 else "+"}{abs(coef)}x^{{{expon}}}'
        
        #print('En funcion, LaTeX: ', simbolo)
        return simbolo