from analisis import puntos_criticos
from analisis.graficar import graficar
from analisis.intervalos import obtener_intervalos
from analisis.Funcion import Funcion, TipoPuntos
from analisis.analisis import obtener_coeficientes
from analisis.derivación import derivar
from analisis.puntos_criticos import obtener_puntos_criticos
from analisis.raices import obtener_raices

from colores import *

def cli():
    # Ayuda para el formato
    print(">>>\tAnálisis de funciones\t<<<")
    print("Instrucciones: Ingresa la función con la forma 'ax**n + bx ** (n-1) + ... + c'")
    print("Por ejemplo: 5x**3 -3x**2 + 2")
    print("* No importan los espacios, ni saltar términos")
    print("* Tanto los coeficientes como los exponentes deben ser enteros")
    print("* Escribe 'q' para salir cuando esté el prompt (>>>)")
    print("-"*30)
    while(True):
        print("Introduce la función:\n", end='')
        print_blue('>>> ', end='')
        s = input()
        if s=='q':
            break

        # Descomponer la función en sus coeficientes
        funcion = obtener_coeficientes(s)
        # Obtener los puntos críticos de la función
        print('> Teniendo la función f(x) = ', end='')
        print_yellow(funcion.pretty())

        # Paso 1: Obtener primera y segunda derivada
        print_green('\n# Paso 1: Encontrar la primera y segunda derivada')
        print('Primera derivada: ', end='')
        derivada_1 = derivar(funcion)
        print('f\'(x) = ', end='')
        print_red(derivada_1.pretty())
        print('Segunda derivada: ', end='')
        derivada_2 = derivar(derivada_1)
        print('f\'\'(x) = ', end='')
        print_red(derivada_2.pretty())

        
        puntos = obtener_puntos_criticos(funcion, derivada_1, derivada_2)

        puntos_relevantes = puntos[TipoPuntos.Maximo] + puntos[TipoPuntos.Minimo]

        intervalos = obtener_intervalos(derivada_1, puntos_relevantes)
        
        graficar(funcion, puntos, intervalos)

        print('\n***\n')

if __name__ == '__main__':
    cli()