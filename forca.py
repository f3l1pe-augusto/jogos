def jogar_forca():
    print("\n***************************")
    print("Bem vindo ao jogo de forca!")
    print("***************************\n")

    #define palavra secreta
    palavra_secreta = "corinthians".upper()

    #inicializa e preenche com "_" a lista de palavras acertadas (list comprehension)
    letras_acertadas = ["_" for letra in palavra_secreta]

    #variáveis
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou) and (not acertou):

        chute = input("Qual letra?: ")
        #remove espaços em branco e coloca todas as letras em maiúsculo
        chute = chute.strip().upper()

        #verificação letras acertadas
        if chute in palavra_secreta:
            pos = 0
            for letra in palavra_secreta:
                if letra == chute:
                    letras_acertadas[pos] = letra
                pos += 1
        else:
            print("Você errou!")
            erros += 1
            print("Resta(m) {} tentativa(s)\n".format(len(palavra_secreta) - erros))

        print(letras_acertadas)

        #verificação fim do jogo
        if letras_acertadas.count('_') == 0:
            print("\nVocê ganhou!")
            acertou = True
        if erros == len(palavra_secreta):
            print("\nVocê perdeu!")
            enforcou = True

if __name__ == "__main__":
    jogar_forca()
