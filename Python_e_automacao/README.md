# Mission Control AI 🚀

**Sistema Inteligente de Monitoramento de Missão Espacial**

Projeto desenvolvido para a **Global Solution GS2026.1 - Pensamento Computacional e Automação com Python** da FIAP.

---

## 📋 Sobre o Projeto

O **Mission Control AI** é um sistema em Python que simula o monitoramento inteligente de uma missão espacial experimental. 

O programa analisa dados de temperatura, comunicação, bateria, oxigênio e estabilidade ao longo de ciclos de monitoramento, gera alertas automáticos, calcula o nível de risco e produz um relatório final completo.

---

## ✨ Funcionalidades Implementadas

- Análise de **6 ciclos** de monitoramento
- Classificação automática (`NORMAL`, `ATENÇÃO`, `CRÍTICO`) para cada parâmetro
- Cálculo de pontuação de risco por ciclo (0 a 10)
- Classificação do ciclo (`MISSÃO ESTÁVEL`, `MISSÃO EM ATENÇÃO`, `MISSÃO CRÍTICA`)
- Análise de tendência da missão (melhora / piora / estável)
- Identificação da **área mais afetada**
- Geração de recomendações automáticas
- Relatório final detalhado no terminal

---

## 🛠️ Regras de Classificação

### Temperatura (°C)
- **CRÍTICO**: > 35 ou < 18  
- **ATENÇÃO**: 30–35  
- **NORMAL**: 18–30

### Comunicação (%)
- **CRÍTICO**: < 30  
- **ATENÇÃO**: 30–59  
- **NORMAL**: ≥ 60

### Bateria (%)
- **CRÍTICO**: < 20  
- **ATENÇÃO**: 20–49  
- **NORMAL**: ≥ 50

### Oxigênio (%)
- **CRÍTICO**: < 80  
- **ATENÇÃO**: 80–89  
- **NORMAL**: ≥ 90

### Estabilidade (%)
- **CRÍTICO**: < 40  
- **ATENÇÃO**: 40–69  
- **NORMAL**: ≥ 70

**Pontuação:** NORMAL = 0 | ATENÇÃO = 1 | CRÍTICO = 2

---

## 📁 Estrutura do Repositório

mission-control-ai/
├── README.md
├── mission_control.py


---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/RVaca1/GS_2026

# Entre na pasta
cd /Python_e_automacao

# Execute o programa
python mission_control.py