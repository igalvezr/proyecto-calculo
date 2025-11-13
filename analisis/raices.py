from analisis.Funcion import Funcion

def es_entero(num: float, tolerancia = 1e-9):
    return abs(num - round(num)) < tolerancia

def obtener_raices(funcion: Funcion) -> list[float]:
    # método de raices racionales

    print('Previo, func original: ', funcion.coeficientes)
    # Previo: verificar que los coeficientes sean enteros
    coeficientes_f: dict[int, float] = funcion.coeficientes.copy()
    coeficientes: dict[int, int] = dict()

    for expon, coef in coeficientes_f.items():
        if not es_entero(coef):
            raise Exception("Coeficientes no enteros para raices racionales")
        coeficientes[expon] = round(coef)

    print('Paso 0, coeficientes enteros: ', coeficientes)
    # Paso 1: asegurar el término independiente
    raices_nulas = 0

    menor_grado = min(funcion.coeficientes.keys())

    if menor_grado > 0:
        # hay que factorizar x
        raices_nulas = min(funcion.coeficientes.keys())
        for expon in sorted(coeficientes.keys()):
            coeficientes[expon - raices_nulas] = coeficientes[expon]
        # eliminar el valor para el exponente mas grande
        coeficientes.pop(max(coeficientes.keys()))
    
    print(f'Paso 1, nulas: {raices_nulas}')

    # Paso 2: encontrar los divisores para el término de mayor grado y el independiente
    divisores_n = list()
    divisores_0 = list()

    # para el término del grado mayor
    coef_mayor = coeficientes[max(coeficientes.keys())]
    for i in range(1, coef_mayor + 1):
        if abs(coef_mayor) % i == 0:
            divisores_n.append(i)
            divisores_n.append(-i)
    
    print('Paso 2.1, divisores de n: ', divisores_n)
    # para el término independiente
    coef_independiente = abs(coeficientes[0])
    for i in range(1, coef_independiente + 1):
        #print(f'# Verificando {coef_independiente} / {i}')
        if coef_independiente % i == 0:
            #print('Si es')
            divisores_0.append(i)
            divisores_0.append(-i)
        #else:
            #print('No es')
    
    print('Paso 2.2, divisores de 0: ', divisores_0)
    # encontrar los divisores
    divisores = set()
    for i in divisores_0:
        for j in divisores_n:
            divisores.add(i/j)
    
    print('Paso 2.3, divisores: ', divisores)

    # verificar si son raíz
    raices = list()
    for divisor in divisores:
        print(f'Verificando posible raíz: {divisor:.2f}')
        resto = 0
        for expon, coef in coeficientes.items():
            resto += divisor ** expon * coef
        print(f'Resultado de eval: {resto}')
        if resto == 0:
            raices.append(divisor)
    
    # añadir raices nulas
    for i in range(raices_nulas):
        raices.append(0)

    return raices

