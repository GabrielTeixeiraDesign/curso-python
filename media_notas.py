notas = []  # lista vazia para guardar as notas

print("=== Cálculo de Média ===")
nome = input("Digite o nome do aluno: ")

# Coleta 3 notas
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

# Calcula média
media = sum(notas) / len(notas)

print(f"\nAluno: {nome}")
print(f"Notas: {notas}")
print(f"Média: {media:.2f}")

# Mostra situação
if media >= 7:
    print("Situação: Aprovado 🎉")
elif media >= 5:
    print("Situação: Recuperação ⚠️")
else:
    print("Situação: Reprovado ❌")
