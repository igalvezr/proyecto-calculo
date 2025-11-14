from analisis.Funcion import Funcion, TipoPuntos
from analisis.derivación import derivar
from analisis.raices import obtener_raices


def obtener_puntos_criticos(funcion: Funcion) -> tuple[dict[TipoPuntos, list[tuple[float, float]]], Funcion, Funcion]:
    print('### Obtención de puntos críticos de la función ###')
    print('> Teniendo la función f(x) = ', funcion.pretty())

    # Paso 1: Obtener primera y segunda derivada
    print('# Paso 1: Encontrar la primera y segunda derivada')
    print('Primera derivada:')
    derivada_1 = derivar(funcion)
    print('f\'(x) = ', derivada_1.pretty())
    print('Segunda derivada:')
    derivada_2 = derivar(derivada_1)
    print('f\'\'(x) = ', derivada_2.pretty())

    # Paso 2: obtener los máximos y mínimos
    print('\n')
    print('# Paso 2: Obtener las raíces de f\'(x) para conocer los puntos críticos:')
    criticos = obtener_raices(derivada_1)
    print('Las raíces de f\'(x) son: ', [float(crit) for crit in criticos])

    # Paso 3: Determinar la naturaleza de cada punto crítico
    print('# Paso 3: Evaluamos cada resultado en la segunda derivada para conocer la naturaleza de cada punto')
    maximos = list()
    minimos = list()
    for critico in criticos:
        print(f'    para x = {critico}, f\'\'(x) = {derivada_2.evlauar(critico)}')
        if derivada_2.evlauar(critico) < 0:
            print(f'    {derivada_2.evlauar(critico)} < 0 por tanto es un Máximo')
            # Es un máximo
            maximos.append((critico, funcion.evlauar(critico)))
        else:
            print(f'    {derivada_2.evlauar(critico)} >= 0 por tanto es un Mínimo')
            # es un mínimo
            minimos.append((critico, funcion.evlauar(critico)))
    
    # Paso 4: Obtener puntos de inflexión
    print('# Paso 4: Obtener los puntos de inflexión igualando f\'\'(x) a cero')
    inflexion_x = obtener_raices(derivada_2)
    inflexion = [(punto, funcion.evlauar(punto)) for punto in inflexion_x]
    print('Los puntos de inflexión son: ', [float(punto[0]) for punto in inflexion])

    return ({
        TipoPuntos.Maximo: maximos,
        TipoPuntos.Minimo: minimos,
        TipoPuntos.Inflexion: inflexion
    }, derivada_1, derivada_2)