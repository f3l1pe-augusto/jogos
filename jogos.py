import adivinhacao
import forca

def escolher_jogos():
    print("*******************")
    print("Escolha o seu jogo!")
    print("*******************\n")

    print("(1) Adivinhação (2) Forca\n")

    res = int(input("--> "))

    if(res == 1):
        adivinhacao.jogar_adivinhacao()
    elif(res == 2):
        forca.jogar_forca()

if(__name__ == "__main__"):
    escolher_jogos()
