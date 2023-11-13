import random

def jogar_forca():

    imprime_mensagem_bem_vindo()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_lista_letras_acertadas(palavra_secreta)

    # mostra a quantidade de letras que a palavra secreta tem
    print(letras_acertadas)

    #variáveis
    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou) and (not acertou):

        chute = pede_chute()

        #verificação letras acertadas
        if chute in palavra_secreta:
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros = chute_incorreto(erros, palavra_secreta)
            desenha_forca(erros)

        print(letras_acertadas)

        #verificação fim do jogo
        if letras_acertadas.count('_') == 0:
            imprime_mensagem_vencedor()
            acertou = True
        if erros == 7:
            imprime_mensagem_perdedor(palavra_secreta)
            enforcou = True

def imprime_mensagem_bem_vindo():
    print("\n***********************************")
    print("Bem vindo ao jogo da forca!")
    print("Dica: todas as palavras são bandas.")
    print("***********************************\n")

def carrega_palavra_secreta():
    # abertura e fechamento do arquivo e inicialização da lista de possíveis palavras secretas
    with open("palavras.txt") as arquivo:
        palavras = []

        # adição das possíveis palavras secretas à lista
        for linha in arquivo:
            linha = linha.strip().upper()
            palavras.append(linha)

    # escolha aleatória para a palavra do jogo
    pos = random.randrange(0, len(palavras))
    palavra_secreta = palavras[pos]

    return palavra_secreta

def inicializa_lista_letras_acertadas(palavra):
    # inicializa e preenche com "_" a lista de palavras acertadas (list comprehension)
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?: ")
    # remove espaços em branco e coloca todas as letras em maiúsculo
    return chute.strip().upper()

def chute_correto(palavra, chute, letras_acertadas):
    pos = 0
    for letra in palavra:
        if letra == chute:
            letras_acertadas[pos] = letra
        pos += 1

def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def chute_incorreto(erros, palavra):
    print("Você errou!")
    erros += 1
    print("Resta(m) {} tentativa(s)\n".format(7 - erros))

    return erros

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar_forca()
