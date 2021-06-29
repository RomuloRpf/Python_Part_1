def computador_escolhe_jogada(n,m):
    for i in range(1,m):
        if (n-i)%(m+1) == 0:
            return i
    return m

def usuario_escolhe_jogada(n,m):
    while True:
        numpecas = int(input("Quantas peças você vai tirar? "))
        if numpecas > m or numpecas <=0:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        elif numpecas > n:
            print("\nOops! Jogada inválida! Tente de novo.\n")
        else:
            return numpecas
        
def partida():
    proximo = False
    pecas = int(input("Quantas peças? "))
    limite= int(input("Limite de peças por jogada? "))
    if pecas%(limite+1) == 0:
        print("\nVocê começa!\n")
    else:
        print("\nComputador começa!\n")
        proximo = True
    while pecas > 0:
        if proximo == False:
            removidas = usuario_escolhe_jogada(pecas,limite)
            print("Você tirou ", removidas," peça.")
            proximo = True
        else:
            removidas = computador_escolhe_jogada(pecas,limite)
            print("O computador tirou ", removidas," peça.")
            proximo = False
        pecas = pecas - removidas
        if pecas != 0:
            print("Agora restam ", pecas ," peças no tabuleiro.\n")
    if proximo == True:
        print("Fim do jogo! Você ganhou!\n")
    else:
        print("Fim do jogo! O computador ganhou!\n")
    return proximo

def campeonato():
    computadorvence = 0
    vencedorpartida = True 
    for i in range(1,4):
        print("**** Rodada ", i ," ****\n")
        vencedorpartida = partida()
        if vencedorpartida == False:
            computadorvence += 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você ", 3 - computadorvence ," X ", computadorvence," Computador")

def main():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    print('')
    escolha=input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
    if escolha=="1":
        print("\nVocê escolheu partida isolada!\n")
        partida()
    else:
        if escolha=="2":
            print("\nVocê escolheu um campeonato!\n")
            campeonato()

main()
