from math import *

a=int(input())
b=int(input())
c=int(input())

delta = (b**2) - (4*a*c)

if delta >= 0:
    x1 = (-b + sqrt(delta))/(2*a)
    if delta==0:
        print("a raiz desta equação é", x1)
    else:
        x2 = (-b - sqrt(delta))/(2*a)
        if x1>x2:
            print("as raízes da equação são", x2, "e", x1)
        else:
            print("as raízes da equação são", x1, "e", x2)
else:
    print("esta equação não possui raízes reais")
