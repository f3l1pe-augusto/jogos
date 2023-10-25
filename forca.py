def jogar_forca():
    print("\n***************************")
    print("Bem vindo ao jogo de forca!")
    print("***************************\n")

    #define palavra secreta
    palavra_secreta = "paramore"

    #variáveis
    enforcou = False
    acertou = False

    while((not enforcou) and (not acertou)):

        chute = input("Qual letra?: ")
        #remove espaços em branco
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if letra.upper() == chute.upper():
                print("Encontrei a letra \"{}\" na posição \"{}\"".format(chute, index))
            index+=1

        print("Jogando...")

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar_forca()
