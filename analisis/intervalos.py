from math import inf
from analisis.Funcion import Funcion, TipoPuntos


def obtener_intervalos(primera_derivada: Funcion, puntos_criticos: list[tuple[float, float]]) -> list[tuple[tuple[float, float], int]]:
    # Paso 1: determinar los intervalos
    puntos_ordenados = [punto[0] for punto in puntos_criticos]
    puntos_ordenados = sorted(puntos_ordenados)
    #print('* En intervalos, puntos x: ', puntos_ordenados)
    intervalos = list()

    if len(puntos_ordenados) == 1:
        intervalos.append((-inf, puntos_ordenados[0]))
        intervalos.append((puntos_ordenados[0], inf))
    else:
        for index in range(len(puntos_ordenados)):
            if index == 0:
                intervalos.append((-inf, puntos_ordenados[index]))
                continue
            intervalos.append((puntos_ordenados[index - 1], puntos_ordenados[index]))
            if index == len(puntos_ordenados) - 1:
                intervalos.append((puntos_ordenados[index], inf))
    
    print('Intervalos: ', intervalos)

    # Paso 2: Determinar la naturaleza de cada intervalo
    tipo_intervalo = list()
    for intervalo in intervalos:
        if intervalo[0] == -inf:
            # es el primero
            if primera_derivada.evaluar(intervalo[1] - 1) < 0:
                tipo_intervalo.append((intervalo, -1))
            else:
                tipo_intervalo.append((intervalo, 1))
            continue

        if intervalo[1] == inf:
            # es el último
            if primera_derivada.evaluar(intervalo[0] + 1) < 0:
                tipo_intervalo.append((intervalo, -1))
            else:
                tipo_intervalo.append((intervalo, 1))
            continue

        if primera_derivada.evaluar((intervalo[0] + intervalo[1]) / 2) < 0:
            tipo_intervalo.append((intervalo, -1))
        else:
            tipo_intervalo.append((intervalo, 1))
    
    # Imprimir la tabla
    titulos = ['T. de intervalo', 'Intervalo']
    print(f'\n| {titulos[0]} | {titulos[1]} ')
    print(f' -{"-" * 15}- {"-" * 15}')
    if len(intervalos) == 0:
        # significa que no hay intervalos
        if primera_derivada.evaluar(0) > 0:
            print(f'| {"Creciente":15s} | (-inf, inf) ')
        else:
            print(f'| {"Decreciente":15s} | (-inf, inf) ')
    else:
        for intervalo, tipo in tipo_intervalo:
            print(f'| {("Creciente" if tipo==1 else "Decreciente"):15s} | ({intervalo[0]:.4f}, {intervalo[1]:.4f})')
    '''
    if len(intervalos) == 0:
        # significa que no hay intervalos
        if primera_derivada.evaluar(0) > 0:
            print(' - (-inf, inf) -> Creciente')
        else:
            print(' - (-inf, inf) -> Decreciente')
    else:
        for intervalo, tipo in tipo_intervalo:
            print(f'- {intervalo} -> {"Creciente" if tipo==1 else "Decreciente"}')
    '''


    return tipo_intervalo
