from math import inf
from analisis.Funcion import Funcion, TipoPuntos


def obtener_intervalos(primera_derivada: Funcion, puntos_criticos: list[tuple[float, float]]) -> dict[int, tuple[float, float]]:
    # Paso 1: determinar los intervalos
    puntos_ordenados = [punto[0] for punto in puntos_criticos]
    puntos_ordenados = sorted(puntos_ordenados)
    intervalos = list()

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
            if primera_derivada.evlauar(intervalo[1] - 1) < 0:
                tipo_intervalo.append((intervalo, -1))
            else:
                tipo_intervalo.append((intervalo, 1))
            continue

        if intervalo[1] == inf:
            # es el último
            if primera_derivada.evlauar(intervalo[0] + 1) < 0:
                tipo_intervalo.append((intervalo, -1))
            else:
                tipo_intervalo.append((intervalo, 1))
            continue

        if primera_derivada.evlauar((intervalo[0] + intervalo[1]) / 2) < 0:
            tipo_intervalo.append((intervalo, -1))
        else:
            tipo_intervalo.append((intervalo, 1))
        
    for intervalo, tipo in tipo_intervalo:
        print(f'- {intervalo} -> {"Creciente" if tipo==1 else "Decreciente"}')


    return {}
