def Argu(*N):
    for x in N:
        print(x)
Argu(1, 2, 3, "six")  #Arbitrary Positional Arguments


def Arguuu(**N):
    for key, value in N.items():  #Arbitrary Keyword Arguments
        print(key,":", value)
Arguuu(Name="Aditya", Age= 19, Uid= 543)   