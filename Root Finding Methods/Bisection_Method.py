def func(x):
    return x*x*x - x - 1
def bisection(a, b):
    if(func(a)*func(b)>=0):
        print("Value of a and b is not correct\n")
        return
    c=a
    while((b-a)>=0.01):
        c=(a+b)/2
        if(func(c)==0):
            break
        if(func(c)*func(a)<0):
            b=c
        else:
            a=c
    print("The root value is: ", c)
a=1
b=2
bisection(a, b)