from math import *

"""
Esta función corresponde a la transformación de la función que se quiere
evaluar.
"""
def g(x):
    return pow(2.0,-x)

def puntofijo (f, p0, tolerancia, iteraciones):

    i=1
    while i<= iteraciones:
        p = f(p0)
        print ("iter=","%03d" % i, "; p=", "%.14f" %p)
        if abs (p-p0) < tolerancia:
            return p
        p0=p
        i+=1

    print ("Iteraciones agotadas, error")
    return

print ("Método de punto fijo")

puntofijo (g, 0.5, 1e-8, 100)