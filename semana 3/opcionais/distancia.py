from math import*

x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

distancia = sqrt(((x1-x2)**2)+((y1-y2)**2))

if distancia >= 10:
    print("longe")
else:
    print("perto")


