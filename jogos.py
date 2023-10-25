import adivinhacao
import forca

def reprocessamento():
    res = input("\nDeseja continuar jogando(S/N)? ")
    if res.upper() == 'N':
        jogando = False
    else:
        jogando = True
    return jogando
def escolher_jogos():
    jogando = True
    while jogando:
        print("*******************")
        print("Escolha o seu jogo!")
        print("*******************\n")

        print("(1) Adivinhação (2) Forca\n")

        res = int(input("--> "))

        if (res == 1):
            adivinhacao.jogar_adivinhacao()
        elif (res == 2):
            forca.jogar_forca()

        jogando = reprocessamento()

if(__name__ == "__main__"):
    escolher_jogos()
