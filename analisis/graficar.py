from math import inf
import matplotlib.pyplot as plt
import numpy as np

from analisis.Funcion import Funcion, TipoPuntos
from analisis.es_cero import es_cercano
from analisis.raices import obtener_raices


def __comparar_intervalos(intervalo: tuple[float, float]):
    if intervalo[0] == -inf:
        return intervalo[1]
    elif tuple[1] == inf:
        return intervalo[0]
    else:
        return (intervalo[1] + intervalo[0]) / 2


def obtener_rango_de_impresion(puntos_notables: dict[TipoPuntos, list[tuple[float, float]]], funcion: Funcion) -> list[tuple[float, float]]:
    # determinar cuales son los mas alejados
    puntos: list[tuple[float, float]] = list()

    # concentrar los puntos en la lista
    for _, lista_puntos in puntos_notables.items():
        for punto in lista_puntos:
            puntos.append(punto)
    
    raices = obtener_raices(funcion)
    for raiz in raices:
        puntos.append((raiz, 0.0))
    
    # determinar los puntos extremos
    minimo: tuple[float, float] = puntos[0]
    
    for indice in range(len(puntos)):
        if puntos[indice][0] < minimo[0]:
            minimo = puntos[indice]
    
    maximo: tuple[float, float] = puntos[0]
    for indice in range(len(puntos)):
        if puntos[indice][0] > maximo[0]:
            maximo = puntos[indice]
    
    # Si los mínimos y máximos son cero, devolvemos un rango de -10 a 10
    
    if es_cercano(minimo[0], 0) and es_cercano(maximo[0], 0):
        minimo = (-10, 0)
        maximo = (10, 0)
    return [minimo, maximo]



def graficar(funcion: Funcion, puntos_notables: dict[TipoPuntos, list[tuple[float, float]]], intervalos: list[tuple[tuple[float, float], int]]):

    fig, ax = plt.subplots()

    # Determinar el rango de numeros para graficar - 30% extra del ancho total de los intervalos
    rango_inf, rango_sup = obtener_rango_de_impresion(puntos_notables, funcion)
    rango = rango_sup[0] - rango_inf[0]

    # obtener los datos en un arreglo numpy
    datos_x = np.linspace(rango_inf[0] - rango * 0.3, rango_sup[0] + rango * 0.3, 100)

    # obtener las imagenes para cada uno
    datos_y = np.vectorize(lambda elem: funcion.evaluar(elem))(datos_x)

    # graficar la función
    ax.plot(datos_x, datos_y, zorder=10)

    # Graficar los puntos máximos
    maximos = puntos_notables[TipoPuntos.Maximo]

    for maximo in maximos:
        ax.scatter(maximo[0], maximo[1], zorder=20, c='green', label=f'Máx - ({maximo[0]:.2f}, {maximo[1]:.2f})')
    
    # Graficar los puntos mínimos
    minimos = puntos_notables[TipoPuntos.Minimo]

    for minimo in minimos:
        ax.scatter(minimo[0], minimo[1], zorder=20, c='red', label=f'Mín - ({minimo[0]:.2f}, {minimo[1]:.2f})')
    
    # Graficar los puntos de inflexión:
    inflexion = puntos_notables[TipoPuntos.Inflexion]

    for punto in inflexion:
        ax.scatter(punto[0], punto[1], zorder=20, c='orange', label=f'Inflx - ({punto[0]:.2f}, {punto[1]:.2f})')
    
    # Detalles estéticos
    ax.axhline(y=0, color='k', linewidth=0.8, linestyle='-')
    ax.axvline(x=0, color='k', linewidth=0.8, linestyle='-')
    fig.suptitle('Gráfica de la función')
    ax.set_title(f'Función: ${funcion.to_latex()}$')
    ax.legend()

    ax.grid(True)
    plt.show()

