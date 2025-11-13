from analisis.Funcion import Funcion


def derivar(func: Funcion) -> Funcion:
    derivada = Funcion()

    for expon, coef in func.coeficientes.items():
        if expon == 0:
            continue
        derivada.coeficientes[expon - 1] = coef * expon
    
    return derivada