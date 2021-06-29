base = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for i in range(0,altura):
    for j in range(0,base):
        if i == 0 or i == altura-1:
            if j == base-1:
                print("#")
            else:
                print("#", end = '')
        else:
            if j == 0:
                print("#", end = '')
            elif j== base-1:
                print("#")
            else:
                print(" ", end = '')
                
