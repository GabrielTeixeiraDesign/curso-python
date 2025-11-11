opcao = 0  # começa com 0 só pra entrar no loop

while opcao != 4:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Somar dois números")
    print("2 - Subtrair dois números")
    print("3 - Multiplicar dois números")
    print("4 - Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da soma: {n1 + n2}")

    elif opcao == 2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da subtração: {n1 - n2}")

    elif opcao == 3:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print(f"Resultado da multiplicação: {n1 * n2}")

    elif opcao == 4:
        print("Saindo do programa... 👋")

    else:
        print("Opção inválida! Tente novamente.")
