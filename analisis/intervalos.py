from math import inf
from analisis.Funcion import Funcion, TipoPuntos


def obtener_intervalos(primera_derivada: Funcion, puntos_criticos: list[tuple[float, float]]) -> list[tuple[tuple[float, float], int]]:
    '''
    Determina los intervalos donde la función es creciente o decreciente
    '''

    # Paso 1: determinar los intervalos
    # Ordenar los puntos críticos
    puntos_ordenados = [punto[0] for punto in puntos_criticos]
    puntos_ordenados = sorted(puntos_ordenados)
    #print('* En intervalos, puntos x: ', puntos_ordenados)
    intervalos = list()

    # Si se tiene un solo punto, se tienen dos intervalos solamente
    if len(puntos_ordenados) == 1:
        intervalos.append((-inf, puntos_ordenados[0]))
        intervalos.append((puntos_ordenados[0], inf))
    else:
        # Determinar la naturaleza de la función entre cada par de puntos críticos
        for index in range(len(puntos_ordenados)):
            # Si es el primer punto, entonces el intervalo es de menos infinito
            # al punto actual
            if index == 0:
                intervalos.append((-inf, puntos_ordenados[index]))
                continue
            intervalos.append((puntos_ordenados[index - 1], puntos_ordenados[index]))

            # Si es el último punto, el intervalo es desde el punto actual hasta infinito
            if index == len(puntos_ordenados) - 1:
                intervalos.append((puntos_ordenados[index], inf))
    
    print('Intervalos: ', intervalos)

    # Paso 2: Determinar la naturaleza de cada intervalo
    tipo_intervalo = list()
    # Iterar sobre los intervalos
    # -1 significa que es decreciente
    # 1 significa que es creciente
    for intervalo in intervalos:
        if intervalo[0] == -inf:
            # es el primero, se evalúa en x - 1
            if primera_derivada.evaluar(intervalo[1] - 1) < 0:
                tipo_intervalo.append((intervalo, -1))
            else:
                tipo_intervalo.append((intervalo, 1))
            continue

        if intervalo[1] == inf:
            # es el último, se evalúa en x + 1
            if primera_derivada.evaluar(intervalo[0] + 1) < 0:
                tipo_intervalo.append((intervalo, -1))
            else:
                tipo_intervalo.append((intervalo, 1))
            continue

        # intervalos normales, se evalúa en el punto medio entre ambos
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

    return tipo_intervalo
