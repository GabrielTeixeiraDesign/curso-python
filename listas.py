# Aula 12 - Listas em Python

# Criando uma lista
nomes = ["Gabriel", "Maria", "Lucas", "Ana"]
idades = [24, 18, 32, 15]

# Acessando elementos
print("Primeiro nome:", nomes[0])
print("Último nome:", nomes[-1])

# Modificando um item
nomes[1] = "Mariana"
print("Lista atualizada:", nomes)

# Adicionando itens
nomes.append("João")
print("Depois de adicionar:", nomes)

# Inserindo em uma posição específica
nomes.insert(2, "Pedro")
print("Depois de inserir Pedro:", nomes)

# Removendo itens
nomes.remove("Lucas")
print("Depois de remover Lucas:", nomes)

# Remover último item
nomes.pop()
print("Depois do pop:", nomes)

# Tamanho da lista
print("Quantidade de nomes:", len(nomes))

# Percorrendo a lista
print("\nLista de nomes:")
for nome in nomes:
    print("-", nome)
