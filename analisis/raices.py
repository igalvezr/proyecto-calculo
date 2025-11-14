from analisis.Funcion import Funcion

import numpy as np

def obtener_raices(funcion: Funcion) -> list[float]:
    coeficientes = funcion.coeficientes.copy()

    if not coeficientes:
        raise Exception("Función inválida")
    
    # construir un arreglo de coeficinetes
    grado_max = max(coeficientes.keys())
    coefs_arr = [coeficientes.get(i, 0) for i in range(grado_max, -1, -1)]
    raices_complejas = np.roots(coefs_arr)

    raices_reales = list()
    for raiz in raices_complejas:
        if abs(raiz.imag) < 1e-9:
            raices_reales.append(round(raiz.real, 6))
    
    return [float(raiz) for raiz in raices_reales]