base = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for i in range(0,altura):
    for j in range(0,base):
        if j == base-1:
            print("#")
        else:
            print("#", end = '')
