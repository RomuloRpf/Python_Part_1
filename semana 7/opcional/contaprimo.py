from math import*

def n_primos(numero):
    contador = 0
    for n in range(2,numero+1):
        primo= True
        raiz = sqrt(n)
        i=2
        while i<=raiz:
            if (n%i)==0:
                primo=False
                break
            i=i+1
        if primo==True:
            contador += 1
    return contador
