from analisis.intervalos import obtener_intervalos
from analisis.Funcion import Funcion, TipoPuntos
from analisis.analisis import obtener_coeficientes
from analisis.derivación import derivar
from analisis.puntos_criticos import obtener_puntos_criticos
from analisis.raices import obtener_raices


def cli():
    while(True):
        print("Introduce la función:\n>>> ", end='')
        s = input()
        if s=='q':
            break
        coef = obtener_coeficientes(s)
        funcion = Funcion(coef)
        puntos, derivada_1, derivada_2 = obtener_puntos_criticos(funcion)
        puntos_relevantes = puntos[TipoPuntos.Maximo] + puntos[TipoPuntos.Minimo]
        obtener_intervalos(derivada_1, puntos_relevantes)

if __name__ == '__main__':
    cli()