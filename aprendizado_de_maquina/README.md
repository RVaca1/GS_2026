# 🌌 Análise Estatística — Near-Earth Objects (NEO) NASA

> Atividade Avaliativa — Estatística Descritiva  
> Curso: Análise e Desenvolvimento de Sistemas | FIAP  
> Turma: **1CCPH** | Modalidade: **Dupla**

---

## 👥 Integrantes

| Nome Completo | RM | Turma |
|---|---|---|
| Ricardo Tunes Vaca | RM: 555919 | 1CCPH |
| Guilherme de Lucena Fontes | RM: 569658 | 1CCPH |

---

## 📌 Sobre o Projeto

Este projeto aplica conceitos de **Estatística Descritiva** sobre o dataset público da NASA contendo dados de **Near-Earth Objects (NEOs)** — asteroides e cometas com órbitas próximas à Terra.

O dataset conta com **90.836 registros** de asteroides catalogados, com atributos como velocidade relativa, diâmetro estimado, distância de passagem, magnitude absoluta e classificação de periculosidade.

---

## 🗂️ Estrutura do Repositório

```
📦 neo-estatistica/
├── 📄 README.md                        ← Este arquivo
├── 📊 neo.csv                          ← Base de dados (NASA — Kaggle)
├── 📊 neo_v2.csv                       ← Base de dados versão 2
├── 📋 tabela_frequencias_NEO.xlsx      ← Tabelas de distribuição de frequências
├── 🐍 analise_NEO.py                   ← Script Python (Google Colab)
└── 📝 relatorio_estatistico_NEO.pdf    ← Relatório estatístico completo
```

---

## 📂 Descrição dos Entregáveis

### `neo.csv` / `neo_v2.csv`
Base de dados original obtida via [Kaggle — NASA NEO Dataset](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects).

| Variável | Tipo | Descrição |
|---|---|---|
| `id` | Discreto | Identificador único do asteroide |
| `name` | Qualitativo | Nome/designação do asteroide |
| `est_diameter_min` | Contínuo | Diâmetro mínimo estimado (km) |
| `est_diameter_max` | Contínuo | Diâmetro máximo estimado (km) |
| `relative_velocity` | Contínuo | Velocidade relativa à Terra (km/h) |
| `miss_distance` | Contínuo | Distância de passagem (km) |
| `absolute_magnitude` | Discreto* | Magnitude absoluta (brilho intrínseco — H) |
| `hazardous` | Booleano | Se é potencialmente perigoso (True/False) |

---

### `tabela_frequencias_NEO.xlsx`
Planilha Excel com duas abas contendo tabelas de distribuição de frequências completas:

- **Aba 1 — Var. Discreta:** Magnitude Absoluta (H) com 24 classes
  - Frequência absoluta (fi), relativa (fri), percentual (%), acumulada (Fi) e relativa acumulada (Fri%)
- **Aba 2 — Var. Contínua:** Velocidade Relativa (km/h) com 8 classes de igual amplitude
  - Inclui ponto médio (xi), fi, fri, %, Fi e Fri%

---

### `analise_NEO.py`
Script Python completo desenvolvido para execução no **Google Colab**. Cobre todas as questões da atividade:

**Q2 — Gráficos:**
- Histograma da Velocidade Relativa (com linhas de média e mediana)
- Gráfico de Barras + Pizza — Classificação por Periculosidade

**Q3 — Estatística Descritiva Univariada (2 variáveis):**
- Medidas de tendência central: média, mediana e moda
- Medidas de dispersão: mínimo, máximo, amplitude, variância e desvio padrão
- Medidas separatrizes: Q1, Q2, Q3, IQR, P10 e P90
- Box Plot visual

**Q5 — Regressão Linear Simples:**
- Variável dependente (Y): Diâmetro Máximo Estimado
- Variável independente (X): Magnitude Absoluta (H)
- Equação, R², correlação, p-valor e gráfico

#### Como executar no Google Colab:

```python
# 1. Faça upload do arquivo neo.csv no Colab (ícone de pasta à esquerda)
# 2. Ajuste a linha de leitura:
df = pd.read_csv('/content/neo.csv')

# 3. Execute todas as células (Runtime > Run All)
```

---

### `relatorio_estatistico_NEO.pdf`
Relatório estatístico completo em PDF com as seguintes seções:

1. **Introdução** — Contexto dos NEOs e objetivo da análise
2. **Descrição do Dataset** — Variáveis e tipos
3. **Tabelas de Frequência** — Discreta (magnitude) e contínua (velocidade)
4. **Análise Gráfica** — 4 gráficos com interpretações
5. **Estatística Descritiva Univariada** — Todas as medidas solicitadas
6. **Regressão Linear Simples** — Teoria, modelo, equação e previsões
7. **Conclusões e Insights** — Principais descobertas da análise

---

## 📊 Principais Resultados

### Velocidade Relativa (km/h)
| Medida | Valor |
|---|---|
| Média | 48.066,92 km/h |
| Mediana | 44.190,12 km/h |
| Desvio Padrão | 25.293,30 km/h |
| Coef. de Variação | 52,62% |
| Q1 / Q3 | 28.619 / 62.924 km/h |

### Magnitude Absoluta (H)
| Medida | Valor |
|---|---|
| Média | 23,53 |
| Mediana | 23,70 |
| Desvio Padrão | 2,89 |
| Q1 / Q3 | 21,34 / 25,70 |

### Periculosidade
| Classificação | Qtd | % |
|---|---|---|
| Não Perigosos | 81.996 | 90,3% |
| Potencialmente Perigosos (PHA) | 8.840 | 9,7% |

### Regressão Linear — Diâmetro × Magnitude
```
Diâmetro_max = 4,0547 + (-0,1593) × Magnitude_H
R² = 0,1584 | r = -0,3980 | p-valor < 0,001
```

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)
![SciPy](https://img.shields.io/badge/SciPy-1.x-blue)
![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?logo=googlecolab&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-xlsx-217346?logo=microsoftexcel)

---

## 🔗 Fonte dos Dados

- **NASA CNEOS:** https://cneos.jpl.nasa.gov/
- **Kaggle Dataset:** https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects

---

## 📎 Link do Repositório GitHub

> _https://github.com/RVaca1/GS_2026/tree/main/aprendizado_de_maquina_

---

<p align="center">
  Desenvolvido por <strong>Ricardo Tunes Vaca</strong> & <strong>Guilherme de Lucena Fontes</strong> · FIAP 1CCPH · 2025
</p>
