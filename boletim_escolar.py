alunos = []  # lista principal

print("=== Sistema de Boletim Escolar ===")

while True:
    nome = input("\nNome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    media = (nota1 + nota2) / 2

    # adiciona [nome, média] na lista principal
    alunos.append([nome, media])

# Exibe o boletim completo
print("\n=== Boletim Final ===")
print("NOME\t\tMÉDIA\tSITUAÇÃO")
print("-" * 30)

for aluno in alunos:
    nome, media = aluno
    if media >= 7:
        situacao = "Aprovado ✅"
    elif media >= 5:
        situacao = "Recuperação ⚠️"
    else:
        situacao = "Reprovado ❌"
    
    print(f"{nome}\t\t{media:.2f}\t{situacao}")

print("\nPrograma encerrado. 👋")
