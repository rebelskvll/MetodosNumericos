#!/usr/bin/python3

"""
Script de python que calcula la derivada de una función, la cual será utilizada
en el script del método de Newton. hay que tener
en cuenta que este calculo de la derivada puede contener errores, por lo cual
se recomienda realizar la derivación de forma manual. Al momento de probar, 
el cálculo de la derivada funcionó bien con el ejemplo suministado en los 
scripts del módulo.

Código tomado de https://www.delftstack.com/es/howto/python/python-derivative/
"""


from sympy import *

x = Symbol('x')
y = (2**-x) -x

yprime = y.diff(x)
print(yprime)

