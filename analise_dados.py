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
# 4. Filtrando projetos lucrativos (Faturamento > 3000)
# É como se disséssemos: "Mostre-me apenas as linhas onde o faturamento total é maior que 3000"
projetos_lucrativos = df[df["faturamento_total"] > 3000]

print("\n💎 Projetos Altamente Lucrativos (> R$ 3.000):")
if not projetos_lucrativos.empty:
    print(projetos_lucrativos[["projeto", "faturamento_total"]])
else:
    print("Nenhum projeto atingiu essa meta ainda.")

# 5. Salvando apenas o resultado filtrado em um novo arquivo
projetos_lucrativos.to_csv("relatorio_vip.csv", index=False)
print("\n✅ Arquivo 'relatorio_vip.csv' gerado com sucesso!")    
import matplotlib.pyplot as plt

# --- Criando a Visualização ---
print("\n📊 Gerando gráfico de faturamento...")

# 1. Definimos o que vai no eixo X (Projetos) e no eixo Y (Faturamento)
plt.bar(df["projeto"], df["faturamento_total"], color='skyblue')

# 2. Adicionamos títulos e legendas (Importante para o UX da informação!)
plt.title("Faturamento por Projeto de Design")
plt.xlabel("Projetos")
plt.ylabel("Valor em R$")

# 3. Salva o gráfico como uma imagem para você usar no seu portfólio
plt.savefig("grafico_faturamento.png")

print("✅ Gráfico salvo como 'grafico_faturamento.png'!")

# 4. Mostra o gráfico na tela (opcional)
plt.show()