import pandas as pd

try:
    # 1. Carregando os dados
    df = pd.read_csv("freelas.csv")
    
    # 2. Criando uma nova coluna calculada
    # (Horas multiplicadas pelo Valor da Hora)
    df["faturamento_total"] = df["horas"] * df["valor_hora"]
    
    print("--- Relatório de Projetos ---")
    print(df)
    
    # 3. Fazendo uma análise rápida
    total_geral = df["faturamento_total"].sum()
    media_horas = df["horas"].mean()
    
    print(f"\n💰 Faturamento total previsto: R$ {total_geral}")
    print(f"⏱️ Média de horas por projeto: {media_horas}h")

except FileNotFoundError:
    print("❌ Erro: Arquivo 'freelas.csv' não encontrado!")