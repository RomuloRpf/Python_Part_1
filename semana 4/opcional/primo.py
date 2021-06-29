from math import*

n=int(input("Digite um número inteiro: "))

primo= True
raiz = sqrt(n)
i=2
while i<=raiz:
    if (n%i)==0:
        print("não primo")
        primo=False
        break
    i=i+1
if primo==True:
    print("primo")
