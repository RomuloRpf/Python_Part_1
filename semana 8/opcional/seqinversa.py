
n = int(input("Digite um número: "))
lista =[]
while n != 0:
    lista.append(n)
    n = int(input("Digite um número: "))

tam = len(lista) - 1
for i in range(tam,-1,-1):
    print(lista[i])
