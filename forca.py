def jogar_forca():
    print("\n***************************")
    print("Bem vindo ao jogo de forca!")
    print("***************************\n")

    #define palavra secreta e tamanho da palavra
    palavra_secreta = "paramore"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_", "_"]

    #variáveis
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while((not enforcou) and (not acertou)):

        chute = input("Qual letra?: ")
        #remove espaços em branco
        chute = chute.strip()

        pos = 0

        for letra in palavra_secreta:
            if letra.upper() == chute.upper():
                letras_acertadas[pos] = letra
            pos+=1

        print(letras_acertadas)

        if (letras_acertadas.count('_') == 0):
            acertou = True

    print("\nFim do jogo!")

if(__name__ == "__main__"):
    jogar_forca()
