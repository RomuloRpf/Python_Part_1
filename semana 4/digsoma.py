n=input("Digite o valor de n: ")

soma=0
tam=len(n)
while tam!=0:
    soma=soma+int(n[tam-1])
    tam=tam-1
print(soma)
