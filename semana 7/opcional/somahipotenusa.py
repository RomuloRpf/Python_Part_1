def é_hipotenusa(x):
    a = x**2
    for i in range(x-1,0,-1):
        b = i**2
        for j in range(x-1,0,-1):
            c = j**2
            if a == (b + c):
                return True


def soma_hipotenusas(n):
    soma = 0
    for i in range(1,n+1):
        if é_hipotenusa(i):
            soma = soma + i
    return soma

        
        
