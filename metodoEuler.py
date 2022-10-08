from math import *

def test (t, y):
    return t - y

def Euler (a, b, y0, f, N):
    h = (b - a) / N
    t = a
    w = y0
    print ("ti ---> yi")
    print (t, " ---> ", w)

    for i in range (1, N+1):
        k1 = f(t, w)
        w = w + h * k1
        t = i * h
        print (round(t,2), " ---> ", round(w,10))

print ("Método de Euler")
Euler (0, 1, 2, test, 10)
