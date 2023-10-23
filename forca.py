def jogar_forca():
    print("\n***************************")
    print("Bem vindo ao jogo de forca!")
    print("***************************\n")

    #Define palavra secreta
    palavra_secreta = "paramore"

    #Variáveis
    enforcou = False
    acertou = False
    index = 0

    while((not enforcou) and (not acertou)):
        chute = input("Qual letra?: ")
        for letra in palavra_secreta:
            if letra == chute:
                print("Encontrei a letra \"{}\" na posição \"{}\"".format(chute, index))
                index+=1

        print("Jogando...")

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar_forca()
