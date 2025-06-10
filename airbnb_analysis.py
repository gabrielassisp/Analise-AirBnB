import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# 📥 Carregar base
df = pd.read_csv(r'C:\Users\Gabriel\Downloads\listings.csv')

# 🧹 Limpeza e renomeação
df = df[df['price'] > 0]
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

df.rename(columns={
    'neighbourhood_group': 'regiao',
    'neighbourhood': 'bairro',
    'room_type': 'tipo_quarto',
    'price': 'preco',
    'minimum_nights': 'min_noites',
    'number_of_reviews': 'n_reviews',
    'reviews_per_month': 'reviews_por_mes',
    'availability_365': 'dias_disponiveis'
}, inplace=True)

# --- PERGUNTA 1: Bairros com maiores e menores preços ---
bairros_mais_caros = df.groupby('bairro')['preco'].mean().sort_values(ascending=False).head(10)
bairros_mais_baratos = df.groupby('bairro')['preco'].mean().sort_values().head(10)

# Gráfico 1 – Bairros mais caros
plt.style.use('tableau-colorblind10')
plt.figure()
ax = sns.barplot(x=bairros_mais_caros.values, y=bairros_mais_caros.index, palette='magma')
plt.title("Top 10 Bairros com Maior Preço Médio")
plt.xlabel("Preço Médio (R$)")
plt.ylabel("Bairro")

for i, v in enumerate(bairros_mais_caros.values):
    ax.text(v + 5, i, f"R${v:.0f}", va='center')

plt.show()

# Gráfico 2 – Bairros mais baratos
plt.figure()
ax = sns.barplot(x=bairros_mais_baratos.values, y=bairros_mais_baratos.index, palette='crest')
plt.title("Top 10 Bairros com Menor Preço Médio")
plt.xlabel("Preço Médio (R$)")
plt.ylabel("Bairro")

for i, v in enumerate(bairros_mais_baratos.values):
    ax.text(v + 2, i, f"R${v:.0f}", va='center')

plt.show()

# --- PERGUNTA 2: Correlação entre preço e avaliação (proxy: número de reviews) ---
correlacao = df[['preco', 'n_reviews', 'reviews_por_mes']].corr()
print("\nCorrelação entre Preço, Número de Reviews e Reviews por Mês:")
print(correlacao)

# Gráfico 3 – Dispersão
plt.figure()
ax = sns.scatterplot(data=df, x='n_reviews', y='preco', alpha=0.3)
plt.title("Correlação entre Preço e Número de Avaliações")
plt.xlabel("Número de Reviews")
plt.ylabel("Preço (R$)")
plt.show()

# --- PERGUNTA 3: Distribuição da disponibilidade ---
plt.figure()
ax = sns.histplot(data=df, x='dias_disponiveis', bins=30, kde=True, color='skyblue')
plt.title("Distribuição da Disponibilidade Anual dos Imóveis")
plt.xlabel("Dias disponíveis no ano")
plt.ylabel("Quantidade de imóveis")
plt.show()

# --- PERGUNTA 4: Imóveis mais caros oferecem diferenciais? ---
top_5p = df['preco'].quantile(0.95)
mais_caros = df[df['preco'] >= top_5p]

print("\nMédia de reviews por mês dos imóveis mais caros:", mais_caros['reviews_por_mes'].mean())
print("Média de dias disponíveis dos imóveis mais caros:", mais_caros['dias_disponiveis'].mean())

# Gráfico 4 – Disponibilidade dos mais caros
plt.figure()
ax = sns.boxplot(data=mais_caros, y='dias_disponiveis', color='orange')
plt.title("Disponibilidade dos Imóveis Mais Caros")
plt.ylabel("Dias Disponíveis")
plt.show()

# --- PERGUNTA 5: Tipo de acomodação ---
plt.figure()
ax = sns.countplot(data=df, x='tipo_quarto', palette='viridis')
plt.title("Distribuição de Imóveis por Tipo de Acomodação")
plt.xlabel("Tipo de Quarto")
plt.ylabel("Quantidade de Imóveis")

# Adiciona rótulos nas barras
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2., height + 10, f'{int(height)}', ha="center")

plt.show()

# ✅ Fim da análise
print("\n✅ Análise com rótulos concluída.")
