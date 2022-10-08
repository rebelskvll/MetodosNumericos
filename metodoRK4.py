from math import *

def test (t, y):
    return y - t**2 + 1

def RK4 (a, b, y0, f, N):
    h = (b - a) / N
    t = a
    w = y0
    print ("ti ---> yi")
    print (t, " ---> ", w)

    for i in range (1, N+1):
        k1 = h * f(t, w)
        k2 = h * f(t + h/2.0, w + k1/2.0)
        k3 = h * f(t + h/2.0, w + k2/2.0)
        k4 = h * f(t + h, w + k3)
        w = w + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        t = i * h
        print (round(t,2), " ---> ", round(w,10))

print ("Método de RK4")
RK4 (0, 2, 0.5, test, 10)
