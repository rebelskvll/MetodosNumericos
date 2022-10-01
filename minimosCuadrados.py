#!/usr/bin/python3

from sympy import Symbol, poly_from_expr
import cargarDatos as cd

"""
Este script ha sido modificado del libro Métodos numéricos con Python.
En un comienzo el script no mostraba información relevante, únicamente la 
evaluación de x=1 en la recta trazada, esto para MI, no tiene sentido alguno,
en cambio se modificó para que mostrara el polinomio encontrado y con ayuda de 
algún graficador se pueda hacer un análisis más amplio. 
Se suprimió también la función del error relativo, ya que dentro del script no
se estaba utilizando y con los cambios que se realizaron, por el momento no es
posible calcularlo en este script.
"""

def RectaMinSq(datos):

    X = sum([p[0] for p in datos])
    Y = sum([p[1] for p in datos])
    XX = sum([(p[0])**2 for p in datos])
    XY = sum([p[0]*p[1] for p in datos])
    m = len(datos)
    a0 = (Y*XX - X*XY)/(m*XX - X**2)
    a1 = (m*XY - X*Y)/(m*XX - X**2)
    x = Symbol('x')
    ecuacion = a0 + a1*x
    
    return poly_from_expr(ecuacion)

def main():  
    datos = cd.cargarDatos()
    f = RectaMinSq(datos)
    print (f[0].args)

if __name__ == '__main__':
    main()