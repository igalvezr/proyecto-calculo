from analisis.Funcion import Funcion, TipoPuntos
from analisis.raices import obtener_raices

from colores import *


def obtener_puntos_criticos(funcion: Funcion, derivada_1: Funcion, derivada_2: Funcion) -> dict[TipoPuntos, list[tuple[float, float]]]:
    '''
    Determina los puntos máximos, mínimos y de inflexión de la función proveída, usando la primera y segunda derivadas.
    '''

    # Paso 2: obtener los máximos y mínimos
    print_green('\n# Paso 2: Obtener las raíces de f\'(x) para conocer los puntos críticos:')
    criticos: list[float] = []
    try:
        criticos = obtener_raices(derivada_1)
        print('Las raíces de f\'(x) son: ', [float(crit) for crit in criticos])
    except:
        print('-> La segunda derivada no tiene raices reales. Por tanto, no hay máximos ni mínimos.')
        pass

    # Paso 3: Determinar la naturaleza de cada punto crítico
    print_green('\n# Paso 3: Evaluamos cada resultado en la segunda derivada para conocer la naturaleza de cada punto')
    maximos: list[tuple[float, float]] = list()
    minimos: list[tuple[float, float]] = list()
    if len(criticos) == 0:
        print('-> Por lo anterior, no podemos evaluar ningún punto.')
    
    for critico in criticos:
        print(f'    -> para x = {critico}, ', end='')
        print_red(f'f\'\'(x) = {derivada_2.evaluar(critico):.4f}')
        if derivada_2.evaluar(critico) < 0:
            print(f'        {derivada_2.evaluar(critico):.4f} < 0 por tanto es un ', end='')
            print_blue('Máximo')
            # Es un máximo
            maximos.append((critico, funcion.evaluar(critico)))
        else:
            print(f'        {derivada_2.evaluar(critico):.4f} >= 0 por tanto es un ', end='')
            print_magenta('Mínimo')
            # es un mínimo
            minimos.append((critico, funcion.evaluar(critico)))
    
    # Imprimir los mínimos y máximos
    if len(criticos) != 0:
        titulos = ['Tipo de punto', 'Coord x', 'Coord y']
        print(f'\n|{titulos[0]:13s}|{titulos[1]:10s}|{titulos[2]:10s}|')
        print(f' {"-"*13} {"-"*10} {"-"*10}')
        for maximo in maximos:
            print(f'|\033[34m{"Máximo":13s}\033[0m|{maximo[0]:10.4f}|{maximo[1]:10.4f}|')
        for minimo in minimos:
            print(f'|\033[35m{"Mínimo":13s}\033[0m|{minimo[0]:10.4f}|{minimo[1]:10.4f}|')
        print('')

    # Paso 4: Obtener puntos de inflexión
    print_green('\n# Paso 4: Obtener los puntos de inflexión igualando f\'\'(x) a cero')
    inflexion_x: list[float] = []
    try:
        inflexion_x = obtener_raices(derivada_2)
    except:
        print('    -> La segunda derivada no tiene raíces reales.')
        # en este caso, se trata de una función de segundo grado.
        # se toma el punto mínimo o máximo
        if len(maximos) == 1:
            inflexion_x = [maximos[0][0]]
        elif len(minimos):
            inflexion_x = [minimos[0][0]]
        else:
            raise Exception('La función no tiene máximos ni mínimos')
    inflexion = [(punto, funcion.evaluar(punto)) for punto in inflexion_x]
    print('Los puntos de inflexión son:')
    for punto in inflexion:
        print(f'    * x = {punto[0]:.4f}; y = {funcion.evaluar(punto[0]):.4f}')

    return {
        TipoPuntos.Maximo: maximos,
        TipoPuntos.Minimo: minimos,
        TipoPuntos.Inflexion: inflexion
    }