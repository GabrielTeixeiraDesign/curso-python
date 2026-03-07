import os

# 1. Definimos qual pasta queremos organizar
pasta = "icones"

try:
    # 2. Pegamos a lista de todos os arquivos dentro da pasta
    arquivos = os.listdir(pasta)
    print(f"🔍 Encontrei {len(arquivos)} arquivos na pasta.")

    # 3. Loop para renomear um por um
    for nome_antigo in arquivos:
        # Só queremos mexer em arquivos .png (para não renomear pastas por erro)
        if nome_antigo.endswith(".png"):
            
            # Criamos o novo nome (ex: adicionando o prefixo 'ic_')
            novo_nome = nome_antigo.replace("imagem", "asset")
            # Definimos o caminho completo (pasta + nome)
            caminho_antigo = os.path.join(pasta, nome_antigo)
            caminho_novo = os.path.join(pasta, novo_nome)
            
            # A mágica acontece aqui!
            os.rename(caminho_antigo, caminho_novo)
            print(f"✅ {nome_antigo} -> {novo_nome}")

    print("--- Automação concluída com sucesso! ---")

except FileNotFoundError:
    print(f"❌ Erro: A pasta '{pasta}' não foi encontrada.")