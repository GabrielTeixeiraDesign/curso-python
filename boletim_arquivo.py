print("=== Boletim com Arquivo ===")

# Abre o arquivo em modo de escrita ('w' cria ou sobrescreve)
arquivo = open("boletim.txt", "w")

while True:
    nome = input("\nNome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break

    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    media = (nota1 + nota2) / 2

    if media >= 7:
        situacao = "Aprovado ✅"
    elif media >= 5:
        situacao = "Recuperação ⚠️"
    else:
        situacao = "Reprovado ❌"

    # Escreve no arquivo
    arquivo.write(f"{nome};{nota1};{nota2};{media:.2f};{situacao}\n")

# Fecha o arquivo após terminar
arquivo.close()

print("\nBoletim salvo com sucesso no arquivo 'boletim.txt'!")

# Agora vamos ler e mostrar o conteúdo
print("\n=== Conteúdo do arquivo ===")

with open("boletim.txt", "r") as arquivo:
    for linha in arquivo:
        nome, n1, n2, media, situacao = linha.strip().split(";")
        print(f"{nome:10} | Média: {media} | {situacao}")
