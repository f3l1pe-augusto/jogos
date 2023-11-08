import random
def jogar_adivinhacao():
    print("\n*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")

    #parâmetros do jogo
    numero_secreto = random.randrange(1, 101)
    num_pontos = 1000

    print("Escolha o nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil (4) Impossível\n")

    nivel = int(input("--> "))

    if nivel == 1:
        num_tentativas = 7
    elif nivel == 2:
        num_tentativas = 5
    elif nivel == 3:
        num_tentativas = 3
    else:
        num_tentativas = 1

    for rodada in range(1, num_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, num_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1  e 100!\n")
            continue

        print("Você digitou", chute)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!\n".format(num_pontos))
            break
        else:
            num_pontos = num_pontos / 2
            if maior:
                print("Você errou! Seu chute foi maior do que o número secreto.\n")
            elif menor:
                print("Você errou! Seu chute foi menor do que o número secreto.\n")

            if rodada == num_tentativas:
                print("O número secreto era {} e sua pontuação foi de {} pontos".format(numero_secreto, num_pontos))

    print("Fim do jogo!")

if __name__ == "__main__":
    jogar_adivinhacao()
