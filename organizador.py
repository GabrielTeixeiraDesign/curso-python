import os

# 1. Definimos o nome do projeto e as pastas que queremos
nome_projeto = "Projeto_Novo_Cliente"
pastas = ["01_Assets", "02_Design_Framer", "03_Prints_Aprovacao", "04_Final_Entrega"]

print(f"--- Iniciando automação para o projeto: {nome_projeto} ---")

# 2. O Loop que cria as pastas automaticamente
for pasta in pastas:
    caminho = os.path.join(nome_projeto, pasta)
    
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"✅ Pasta criada: {pasta}")
    else:
        print(f"⚠️ A pasta {pasta} já existe.")

print("--- Tudo pronto! Boa sorte no design! ---")
import os
