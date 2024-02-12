def func(x):
    return x*x*x - 3*x -5
def derivfunc(x):
    return 3*(x*x) - 3
def NewtonRaphson(x):
    h = func(x) / derivfunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivfunc(x)    
        # x(i+1) = x(i) - f(x) / f'(x)
        x=x-h
    print("The root value is: ", x)
x0= -2
NewtonRaphson(x0) 