from analisis.Funcion import Funcion

import numpy as np

def obtener_raices(funcion: Funcion) -> list[float]:
    coeficientes = funcion.coeficientes
    #print('En obtener_racies, coeficientes raw: ', coeficientes)

    if not coeficientes:
        raise Exception("Función inválida")
    
    # construir un arreglo de coeficinetes
    coefs_arr = list(coeficientes.values())
    #print ('En obtener_coeficientes, coeficientes de la función: ', coefs_arr)
    raices_complejas = np.roots(coefs_arr)

    #print('En obtener_coeficientes, raices C de la función: ', raices_complejas)
    raices_reales = list()
    for raiz in raices_complejas:
        if abs(raiz.imag) < 1e-9:
            raices_reales.append(round(raiz.real, 6))
    
    #print('En obtener_coeficientes, raices de la función: ', raices_reales)
    if len(raices_reales) == 0:
        raise Exception('No tiene raices reales')
    return [float(raiz) for raiz in raices_reales]