from math import*
def trig(x):
    return 2*sin(x)-x
def trigprima(x):
    return 2*cos(x)-1
def newton(f, fprima, p0, tol, n):
    i=1
    while 1<=n:
        p=p0-f(p0)/fprima(p0)
        print("Inter", "%03d" % i , "; p=", "%.14f" %p)
        if abs(p-p0)<tol:
            return p
        p0=p
        i+=1
    print("Interacciones agotadas: Error")
    return
print("\n"+r"Metodo de la Newton para la ecuacion 2sen(x)-x=0:"+"\n")
newton(trig,trigprima, 1, 1e-10, 100)
