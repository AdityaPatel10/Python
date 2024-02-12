def func(x):
    return x*x*x - 5*x + 1
def Secant(x1, x2):
    n=0
    xm=0
    x0=0
    c=0
    if(func(x1) * func(x2) < 0):
        while True:
            x0 = ((x1 * func(x2) - func(x1) * x2)/(func(x2) - func(x1)))
            c = func(x1) * func(x0)
            x1 = x2
            x2 = x0
            if(c==0):
                break
            xm = ((x1 * func(x2) - func(x1) * x2)/(func(x2) - func(x1)))
            if(abs(xm-x0) < 0.0001):
                break
        print("Root is: ", round(x0, 6))
x1=0
x2=1
Secant(x1, x2)