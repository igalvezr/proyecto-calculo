import re

from analisis.Funcion import Funcion


def obtener_coeficientes(s: str) -> Funcion:
    """
    Toma un string representando una función polinómica,
    y retorna un objeto Funcion con los datos
    """

    # deshacerse de los espacios primero
    s = s.replace(' ', '')
    # separar en una lista cada elemento, donde el punto de separación
    # es un número seguido de un signo
    elementos = re.split(r"(?<=\d)?(?=[+-])", s)

    # Tomar solo los elementos válidos, es decir, que no estén vacíos
    elementos = [elem for elem in elementos if elem]

    # Inicializar un contenedor para el coeficiente de cada potencia
    coeficientes: dict[int, float] = dict()

    # Iterar sobre cada uno de los elementos encontrados
    for elem in elementos:
        # Extraer el signo del elemento
        signo = -1 if '-' in elem else 1

        # Eliminar el símbolo del signo
        elem = elem.replace('-', '')
        elem = elem.replace('+', '')
        # analizar el tipo de término que se tiene
        if 'x' in elem:
            # se trata de un término con variable
            if '**' in elem:
                # tiene exponente
                coef_s, exp_s = re.split(r'\*\*', elem)

                # obtener el valor del exponente
                exp = int(exp_s)

                # obtener el valor del coeficiente
                coef_s = coef_s.replace('x', '')
                if not coef_s:
                    coef_s = '1'
                coef = float(coef_s) * signo

                coeficientes[exp] = coef
                continue
            else:
                # tiene grado 1
                elem = elem.replace('x', '')

                # si el string queda vacío, tiene un 1
                coef = 0
                if not elem:
                    coef = 1
                else:
                    coef = float(elem) * signo
                
                # colocar el coeficiente en el mapa
                coeficientes[1] = coef
                continue
        else:
            # es un término independiente
            valor = float(elem) * signo
            coeficientes[0] = valor

    #print('En análisis: ', coeficientes)
    
    return Funcion(coeficientes=coeficientes)


