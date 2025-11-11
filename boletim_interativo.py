def carregar_alunos():
    alunos = []
    try:
        with open("boletim.txt", "r") as arquivo:
            for linha in arquivo:
                nome, n1, n2, media, situacao = linha.strip().split(";")
                alunos.append([nome, float(n1), float(n2), float(media), situacao])
    except FileNotFoundError:
        print("Arquivo 'boletim.txt' não encontrado. Um novo será criado.")
    return alunos


def salvar_alunos(alunos):
    with open("boletim.txt", "w") as arquivo:
        for aluno in alunos:
            nome, n1, n2, media, situacao = aluno
            arquivo.write(f"{nome};{n1};{n2};{media:.2f};{situacao}\n")


def calcular_situacao(media):
    if media >= 7:
        return "Aprovado ✅"
    elif media >= 5:
        return "Recuperação ⚠️"
    else:
        return "Reprovado ❌"


def mostrar_boletim(alunos):
    print("\n=== Boletim Atual ===")
    print("NOME\t\tMÉDIA\tSITUAÇÃO")
    print("-" * 35)
    for aluno in alunos:
        nome, _, _, media, situacao = aluno
        print(f"{nome:12}\t{media:.2f}\t{situacao}")


def adicionar_aluno(alunos):
    nome = input("Nome do aluno: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2
    situacao = calcular_situacao(media)
    alunos.append([nome, n1, n2, media, situacao])
    print(f"Aluno {nome} adicionado com sucesso!")


def atualizar_aluno(alunos):
    nome = input("Digite o nome do aluno que deseja atualizar: ")
    for aluno in alunos:
        if aluno[0].lower() == nome.lower():
            print(f"Aluno encontrado: {aluno[0]}")
            n1 = float(input("Nova nota 1: "))
            n2 = float(input("Nova nota 2: "))
            media = (n1 + n2) / 2
            situacao = calcular_situacao(media)
            aluno[1], aluno[2], aluno[3], aluno[4] = n1, n2, media, situacao
            print("Dados atualizados com sucesso!")
            return
    print("Aluno não encontrado.")


def excluir_aluno(alunos):
    nome = input("Digite o nome do aluno que deseja excluir: ")
    for aluno in alunos:
        if aluno[0].lower() == nome.lower():
            alunos.remove(aluno)
            print(f"Aluno {nome} removido com sucesso!")
            return
    print("Aluno não encontrado.")


# ===================== PROGRAMA PRINCIPAL =====================

alunos = carregar_alunos()

while True:
    print("\n=== MENU ===")
    print("1. Mostrar boletim")
    print("2. Adicionar aluno")
    print("3. Atualizar aluno")
    print("4. Excluir aluno")
    print("5. Salvar e sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_boletim(alunos)
    elif opcao == "2":
        adicionar_aluno(alunos)
    elif opcao == "3":
        atualizar_aluno(alunos)
    elif opcao == "4":
        excluir_aluno(alunos)
    elif opcao == "5":
        salvar_alunos(alunos)
        print("Alterações salvas! Até logo 👋")
        break
    else:
        print("Opção inválida. Tente novamente.")
