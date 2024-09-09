import random


def jogar():
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    opcoes = ["pedra", "papel", "tesoura"]

    while True:
        jogador_escolha = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()

        if jogador_escolha == "sair":
            print("Obrigado por jogar! Até a próxima.")
            break

        if jogador_escolha not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        computador_escolha = random.choice(opcoes)
        print(f"O computador escolheu: {computador_escolha}")

        if jogador_escolha == computador_escolha:
            print("Empate!")
        elif (jogador_escolha == "pedra" and computador_escolha == "tesoura") or \
                (jogador_escolha == "papel" and computador_escolha == "pedra") or \
                (jogador_escolha == "tesoura" and computador_escolha == "papel"):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        print()


if __name__ == "__main__":
    jogar()