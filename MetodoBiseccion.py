from math import*
def f(x):
    return 10*x**4-3*x*exp(x)-3*exp(x)
def biseccion(f, a, b, tol, n):
    i=1
    while i<n:
        p=a+(b-a)/2.0
        print("Inter", "%03d" % i , "; p=", "%.14f" %p)
        if abs(f(p))<=1e-15 or (b-a)/2.0<tol:
            return p
        i+=1
        if f(a)*f(p) > 0:
            a=p
        else:
            b=p
    print("Interacciones agotadas: Error")
    return
print("\n"+r"Metodo de la Biseccion:"+"\n")
biseccion(f,-1.0, -0.25, 1e-4, 100)



