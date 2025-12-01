from analisis.Funcion import Funcion

import numpy as np

def obtener_raices(funcion: Funcion) -> list[float]:
    '''
    Devuelve una lista con las raíces reales de la función proveída
    '''

    # Obtener los coeficientes de la función
    coeficientes = funcion.coeficientes

    # Si no hay coeficientes, no se puede proceder
    if not coeficientes:
        raise Exception("Función inválida")
    
    # construir un arreglo de coeficientes
    coefs_arr = list(coeficientes.values())
    # usar numpy para obtener las raíces de la función
    raices_complejas = np.roots(coefs_arr)

    raices_reales = list()
    # Filtrar las raíces complejas, dejar solo las reales
    for raiz in raices_complejas:
        if abs(raiz.imag) < 1e-9:
            raices_reales.append(round(raiz.real, 6))
    
    #print('En obtener_coeficientes, raices de la función: ', raices_reales)
    if len(raices_reales) == 0:
        raise Exception('No tiene raices reales')
    return [float(raiz) for raiz in raices_reales]