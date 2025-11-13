from analisis.Funcion import Funcion
from analisis.analisis import obtener_coeficientes
from analisis.derivación import derivar
from analisis.raices import obtener_raices


def cli():
    while(True):
        print("Introduce la función:\n>>> ", end='')
        s = input()
        if s=='q':
            break
        coef = obtener_coeficientes(s)
        funcion = Funcion(coef)
        print('f(x)=', funcion.pretty())
        derivada_1 = derivar(funcion)
        print('f\'(x)=', derivada_1.pretty())
        raices_deriv = obtener_raices(derivada_1)
        print('Raices: ', raices_deriv)

if __name__ == '__main__':
    cli()