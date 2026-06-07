# =============================================================================
# ANÁLISE ESTATÍSTICA — Near-Earth Objects (NEO) Dataset
# Atividade Avaliativa — Estatística Descritiva
# Dataset: neo.csv (NASA — Near-Earth Objects)
# =============================================================================
# INSTRUÇÕES PARA GOOGLE COLAB:
# 1. Faça upload do arquivo neo.csv clicando no ícone de pasta à esquerda
# 2. Execute cada célula sequencialmente (Shift + Enter)
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats

# =============================================================================
# CARREGAMENTO DOS DADOS
# =============================================================================
# No Google Colab, ajuste o caminho conforme necessário:
# df = pd.read_csv('/content/neo.csv')   # se fizer upload pelo Colab
df = pd.read_csv('neo.csv')  # Ajuste o caminho conforme necessário

print("=" * 60)
print("DATASET: Near-Earth Objects (NEO) — NASA")
print("=" * 60)
print(f"Total de registros: {len(df):,}")
print(f"Colunas: {list(df.columns)}")
print()
print(df.head())

# =============================================================================
# QUESTÃO 2 — GRÁFICO 1: Histograma — Velocidade Relativa (km/h)
# Variável Quantitativa Contínua
# =============================================================================
fig, ax = plt.subplots(figsize=(12, 6))

n, bins, patches = ax.hist(
    df['relative_velocity'],
    bins=30,
    color='#2E75B6',
    edgecolor='white',
    linewidth=0.8,
    alpha=0.9
)

# Linha de média e mediana
media_vel = df['relative_velocity'].mean()
mediana_vel = df['relative_velocity'].median()
ax.axvline(media_vel, color='#C00000', linewidth=2, linestyle='--', label=f'Média: {media_vel:,.0f} km/h')
ax.axvline(mediana_vel, color='#FF8C00', linewidth=2, linestyle='-.', label=f'Mediana: {mediana_vel:,.0f} km/h')

ax.set_title(
    'Distribuição da Velocidade Relativa dos Asteroides NEO\n(Near-Earth Objects — NASA)',
    fontsize=14, fontweight='bold', pad=15
)
ax.set_xlabel('Velocidade Relativa (km/h)', fontsize=12, labelpad=10)
ax.set_ylabel('Frequência Absoluta (Nº de Asteroides)', fontsize=12, labelpad=10)
ax.legend(fontsize=11, framealpha=0.9)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.set_facecolor('#F8F9FA')
fig.patch.set_facecolor('white')

plt.tight_layout()
plt.savefig('grafico1_histograma_velocidade.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico 1 salvo: grafico1_histograma_velocidade.png")

# =============================================================================
# QUESTÃO 2 — GRÁFICO 2: Gráfico de Barras — Asteroides Perigosos vs Não Perigosos
# Variável Qualitativa / Discreta
# =============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

hazard_counts = df['hazardous'].value_counts()
labels = ['Não Perigoso', 'Perigoso']
values = [hazard_counts[False], hazard_counts[True]]
colors = ['#2E75B6', '#C00000']
pct = [v / len(df) * 100 for v in values]

# Barras
bars = axes[0].bar(labels, values, color=colors, edgecolor='white', linewidth=1.5, width=0.5)
axes[0].set_title('Classificação de Asteroides NEO\npor Nível de Periculosidade', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Classificação', fontsize=11, labelpad=8)
axes[0].set_ylabel('Número de Asteroides', fontsize=11, labelpad=8)
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))
axes[0].set_facecolor('#F8F9FA')
for bar, p, v in zip(bars, pct, values):
    axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 500,
                 f'{v:,}\n({p:.1f}%)', ha='center', va='bottom', fontsize=11, fontweight='bold')
axes[0].grid(axis='y', linestyle='--', alpha=0.5)
axes[0].set_ylim(0, max(values) * 1.15)

# Pizza
wedges, texts, autotexts = axes[1].pie(
    values, labels=labels, colors=colors, autopct='%1.1f%%',
    startangle=90, pctdistance=0.75,
    wedgeprops=dict(edgecolor='white', linewidth=2)
)
for at in autotexts:
    at.set_fontsize(12)
    at.set_fontweight('bold')
    at.set_color('white')
axes[1].set_title('Proporção de Asteroides\nPotencialmente Perigosos (PHA)', fontsize=13, fontweight='bold')

plt.suptitle('Análise de Periculosidade — Near-Earth Objects (NEO)', fontsize=14, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig('grafico2_periculosidade.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico 2 salvo: grafico2_periculosidade.png")

# =============================================================================
# QUESTÃO 3 — ANÁLISE UNIVARIADA 1: Velocidade Relativa (km/h) — Contínua
# =============================================================================
print("\n" + "=" * 60)
print("ANÁLISE UNIVARIADA 1 — VELOCIDADE RELATIVA (km/h)")
print("=" * 60)

vel = df['relative_velocity'].dropna()

# a) Medidas de Tendência Central
media = vel.mean()
mediana = vel.median()
moda_result = stats.mode(vel.round(-2), keepdims=True)
moda = moda_result.mode[0]

print("\n📌 MEDIDAS DE TENDÊNCIA CENTRAL")
print(f"  Média:   {media:>15,.2f} km/h")
print(f"  Mediana: {mediana:>15,.2f} km/h")
print(f"  Moda:    {moda:>15,.2f} km/h (aproximada por arredondamento)")

# b) Medidas de Dispersão
minimo = vel.min()
maximo = vel.max()
amplitude = maximo - minimo
variancia = vel.var(ddof=1)
desvio_padrao = vel.std(ddof=1)
cv = (desvio_padrao / media) * 100

print("\n📌 MEDIDAS DE DISPERSÃO")
print(f"  Mínimo:         {minimo:>15,.2f} km/h")
print(f"  Máximo:         {maximo:>15,.2f} km/h")
print(f"  Amplitude:      {amplitude:>15,.2f} km/h")
print(f"  Variância:      {variancia:>15,.2f}")
print(f"  Desvio Padrão:  {desvio_padrao:>15,.2f} km/h")
print(f"  Coef. Variação: {cv:>14,.2f}%")

# c) Medidas Separatrizes
q1 = vel.quantile(0.25)
q2 = vel.quantile(0.50)
q3 = vel.quantile(0.75)
iqr = q3 - q1
p10 = vel.quantile(0.10)
p90 = vel.quantile(0.90)

print("\n📌 MEDIDAS SEPARATRIZES (Quartis e Percentis)")
print(f"  Q1 (25%):  {q1:>15,.2f} km/h")
print(f"  Q2 (50%):  {q2:>15,.2f} km/h")
print(f"  Q3 (75%):  {q3:>15,.2f} km/h")
print(f"  IQR:       {iqr:>15,.2f} km/h")
print(f"  P10:       {p10:>15,.2f} km/h")
print(f"  P90:       {p90:>15,.2f} km/h")

# Box plot complementar
fig, ax = plt.subplots(figsize=(10, 5))
bp = ax.boxplot(vel, vert=False, patch_artist=True, widths=0.5,
                boxprops=dict(facecolor='#D6E4F0', color='#1F4E79'),
                medianprops=dict(color='#C00000', linewidth=2),
                whiskerprops=dict(color='#1F4E79'),
                capprops=dict(color='#1F4E79'),
                flierprops=dict(marker='o', color='#C00000', alpha=0.3, markersize=3))
ax.set_title('Box Plot — Velocidade Relativa dos Asteroides NEO', fontsize=13, fontweight='bold')
ax.set_xlabel('Velocidade Relativa (km/h)', fontsize=11)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:,.0f}'))
ax.set_facecolor('#F8F9FA')
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafico3_boxplot_velocidade.png', dpi=150, bbox_inches='tight')
plt.show()

# =============================================================================
# QUESTÃO 3 — ANÁLISE UNIVARIADA 2: Magnitude Absoluta (H) — Discreta
# =============================================================================
print("\n" + "=" * 60)
print("ANÁLISE UNIVARIADA 2 — MAGNITUDE ABSOLUTA (H)")
print("=" * 60)

mag = df['absolute_magnitude'].dropna()

# a) Medidas de Tendência Central
media_m = mag.mean()
mediana_m = mag.median()
moda_m = stats.mode(mag.round(1), keepdims=True).mode[0]

print("\n📌 MEDIDAS DE TENDÊNCIA CENTRAL")
print(f"  Média:   {media_m:>10.4f}")
print(f"  Mediana: {mediana_m:>10.4f}")
print(f"  Moda:    {moda_m:>10.4f} (arredondada a 1 casa decimal)")

# b) Medidas de Dispersão
minimo_m = mag.min()
maximo_m = mag.max()
amplitude_m = maximo_m - minimo_m
variancia_m = mag.var(ddof=1)
desvio_m = mag.std(ddof=1)
cv_m = (desvio_m / media_m) * 100

print("\n📌 MEDIDAS DE DISPERSÃO")
print(f"  Mínimo:         {minimo_m:>10.4f}")
print(f"  Máximo:         {maximo_m:>10.4f}")
print(f"  Amplitude:      {amplitude_m:>10.4f}")
print(f"  Variância:      {variancia_m:>10.4f}")
print(f"  Desvio Padrão:  {desvio_m:>10.4f}")
print(f"  Coef. Variação: {cv_m:>9.2f}%")

# c) Quartis
q1_m = mag.quantile(0.25)
q2_m = mag.quantile(0.50)
q3_m = mag.quantile(0.75)
iqr_m = q3_m - q1_m

print("\n📌 MEDIDAS SEPARATRIZES (Quartis)")
print(f"  Q1 (25%):  {q1_m:>10.4f}")
print(f"  Q2 (50%):  {q2_m:>10.4f}")
print(f"  Q3 (75%):  {q3_m:>10.4f}")
print(f"  IQR:       {iqr_m:>10.4f}")

# =============================================================================
# QUESTÃO 5 — REGRESSÃO LINEAR SIMPLES
# Prever: Diâmetro Máximo Estimado (est_diameter_max)
# Preditor: Magnitude Absoluta (absolute_magnitude)
# =============================================================================
print("\n" + "=" * 60)
print("QUESTÃO 5 — REGRESSÃO LINEAR SIMPLES")
print("Variável Dependente (Y): Diâmetro Máximo Estimado (km)")
print("Variável Independente (X): Magnitude Absoluta (H)")
print("=" * 60)

# Amostra para viabilidade de visualização
sample = df[['absolute_magnitude', 'est_diameter_max']].dropna().sample(5000, random_state=42)
X = sample['absolute_magnitude']
Y = sample['est_diameter_max']

slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
r2 = r_value ** 2

print(f"\n  Intercepto (β₀):       {intercept:>10.6f}")
print(f"  Coeficiente (β₁):      {slope:>10.6f}")
print(f"  Coeficiente de Corr. r: {r_value:>9.4f}")
print(f"  Coef. Determinação R²:  {r2:>9.4f} ({r2*100:.2f}%)")
print(f"  p-valor:                {p_value:.2e}")
print(f"\n  Equação: Diâmetro_max = {intercept:.4f} + ({slope:.4f}) × Magnitude")

# Exemplo de predição
for mag_val in [18, 22, 26, 30]:
    pred = intercept + slope * mag_val
    print(f"  Magnitude H={mag_val}: diâmetro previsto = {max(pred,0):.4f} km")

# Gráfico de Regressão
fig, ax = plt.subplots(figsize=(11, 6))
ax.scatter(X, Y, alpha=0.15, color='#2E75B6', s=10, label='Observações (amostra 5.000)')
x_line = np.linspace(X.min(), X.max(), 200)
y_line = intercept + slope * x_line
ax.plot(x_line, y_line, color='#C00000', linewidth=2.5, label=f'Reta de Regressão\nŷ = {intercept:.3f} + ({slope:.4f})x')
ax.set_title(
    'Regressão Linear Simples\nDiâmetro Máximo Estimado × Magnitude Absoluta (NEO)',
    fontsize=13, fontweight='bold', pad=12
)
ax.set_xlabel('Magnitude Absoluta (H)', fontsize=11, labelpad=8)
ax.set_ylabel('Diâmetro Máximo Estimado (km)', fontsize=11, labelpad=8)
ax.legend(fontsize=10, framealpha=0.9)
ax.set_ylim(-0.5, 8)
ax.set_facecolor('#F8F9FA')
ax.grid(linestyle='--', alpha=0.4)

text_box = f'R² = {r2:.4f}\nr = {r_value:.4f}\np-valor < 0.001'
ax.text(0.02, 0.95, text_box, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('grafico4_regressao_linear.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nGráfico 4 salvo: grafico4_regressao_linear.png")
print("\n✅ Todas as análises concluídas com sucesso!")
