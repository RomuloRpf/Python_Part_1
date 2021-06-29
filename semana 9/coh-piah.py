import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def lista_palavras(texto, parada):
    frase = []
    palavras = []
    sentenca = separa_sentencas(texto)
    for i in sentenca:
        frase = frase + separa_frases(i)
    if parada == True:
        return frase
    for j in frase:
        palavras = palavras + separa_palavras(j)
    
    return palavras

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma_tracos = 0
    for i in range(0,6):
        soma_tracos = soma_tracos + abs(as_a[i] - as_b[i])
        
    return (soma_tracos/6)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []
    palavras = lista_palavras(texto, False)
    frase = lista_palavras(texto, True)
    sentenca = separa_sentencas(texto)
    
    assinatura.append(tam_med_palavra(palavras))
    assinatura.append(R_Type_Token(palavras))
    assinatura.append(R_Hapax_Legomana(palavras))
    assinatura.append(tam_med_sentenca(sentenca))
    assinatura.append(complexidade_sentenca(sentenca,frase))
    assinatura.append(tam_med_frase(frase))
    
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor_grau_sim = 100.00
    posicao = 1
    tam = len(textos)
    for i in range(0,tam):
        assinatura = calcula_assinatura(textos[i])
        grau_sim = compara_assinatura(assinatura,ass_cp)
        if grau_sim < menor_grau_sim:
            menor_grau_sim = grau_sim
            posicao = (i + 1)
            
    return posicao

def tam_med_palavra(palavras):
    soma_tam_palavras = 0
    for i in palavras:
        soma_tam_palavras = soma_tam_palavras + len(i)
    
    return (soma_tam_palavras/len(palavras))

def R_Type_Token(palavras):
    
    return (n_palavras_diferentes(palavras)/len(palavras))

def R_Hapax_Legomana(palavras):
    
    return (n_palavras_unicas(palavras)/len(palavras))

def tam_med_sentenca(sentenca):
    soma_tam_sentenca = 0
    for i in sentenca:
        soma_tam_sentenca = soma_tam_sentenca + len(i)

    return (soma_tam_sentenca/len(sentenca))

def complexidade_sentenca(sentenca,frase):

    return (len(frase)/len(sentenca))

def tam_med_frase(frase):
    soma_tam_frase = 0
    for i in frase:
        soma_tam_frase = soma_tam_frase + len(i)

    return (soma_tam_frase/len(frase))

def  main():
    ass_cp = le_assinatura()
    textos = le_textos()
    numero_texto = avalia_textos(textos, ass_cp)
    print("O autor do texto ", numero_texto ," está infectado com COH-PIAH")

main()


    
