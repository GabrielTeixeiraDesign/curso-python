import random  # biblioteca que gera números aleatórios

numero_secreto = random.randint(1, 100)  # número entre 1 e 100
tentativas = 0
acertou = False

print("🎮 Bem-vindo ao jogo: Adivinhe o Número!")
print("Tente adivinhar o número secreto entre 1 e 100.\n")

while not acertou:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas!")
        acertou = True
    elif palpite < numero_secreto:
        print("📉 O número secreto é MAIOR.")
    else:
        print("📈 O número secreto é MENOR.")

