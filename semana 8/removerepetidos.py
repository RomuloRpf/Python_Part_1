def remove_repetidos(lista):
    lista.sort()
    tam = len(lista) - 1
    i = 0
    while i < tam:
        if lista[i] == lista[i+1]:
            del lista[i+1]
            tam = len(lista) - 1
        else:
            i +=1
    return lista
