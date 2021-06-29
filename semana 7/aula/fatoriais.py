def fatorial(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)

def main():
    n = int(input("Digite um numero inteiro: "))
    while n>=0:
        fatorial(n)
        n = int(input("Digite um numero inteiro: "))

main()
