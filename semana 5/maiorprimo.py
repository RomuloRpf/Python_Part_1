from math import*

def maior_primo(x):
    while x>1:
        primo= True
        raiz = sqrt(x)
        i=2
        while i<=raiz:
            if (x%i)==0:
                primo=False
                break
            i=i+1
        if primo==True:
            return x
        else:
            x = x-1
