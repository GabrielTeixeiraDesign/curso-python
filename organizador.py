import os

# Tentamos o caminho normal
try:
    with open("projetos.txt", "r") as arquivo:
        lista_projetos = arquivo.readlines()
    print("✅ Sucesso: Lista de projetos carregada!")

# Se o arquivo não existir, o Python executa este bloco em vez de quebrar
except FileNotFoundError:
    print("⚠️ Aviso: O arquivo 'projetos.txt' não foi encontrado.")
    print("Usando lista de backup temporária...")
    lista_projetos = ["Projeto_Emergencia_1", "Projeto_Emergencia_2"]

# O restante do código (criação de pastas) continua igual
pastas_padrao = ["01_Assets", "02_Design", "03_Final"]

for projeto in lista_projetos:
    nome_limpo = projeto.strip()
    if not nome_limpo:
        continue
        
    print(f"📁 Criando estrutura para: {nome_limpo}")
    for subpasta in pastas_padrao:
        caminho = os.path.join(nome_limpo, subpasta)
        if not os.path.exists(caminho):
            os.makedirs(caminho)