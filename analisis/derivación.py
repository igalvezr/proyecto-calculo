from analisis.es_cero import es_cero
from analisis.Funcion import Funcion


def derivar(func: Funcion) -> Funcion:
    '''
    Devuelve un objeto Funcion representando la derivada de
    la función proveída
    '''

    # Inicializar el objeto de la derivada
    derivada = Funcion()

    # Iterar por cada coeficiente de cada potencia
    for expon, coef in func.coeficientes.items():
        # Ignorar el término independiente
        if expon == 0:
            continue
        # El coeficiente menor es igual a la potencia por el coeficiente actual
        derivada.coeficientes[expon - 1] = coef * expon
    
    # Ordenar los coeficientes
    return derivada