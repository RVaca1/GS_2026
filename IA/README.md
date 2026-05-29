# 🚀 Mission Control AI — ConnectSat

> Sistema de monitoramento operacional de satélite de telecomunicações LEO com análise por IA generativa, voltado à conectividade rural e inclusão digital no Brasil.

---

## 👥 Integrantes

| Nome Completo | RM | Turma |
|---|---|---|
| [Nome Completo] | RM: XXXXXX | XCCXX |
| [Nome Completo] | RM: XXXXXX | XCCXX |

**Modalidade:** Dupla

---

## 📡 O que o projeto faz

O **ConnectSat Mission Control** é um sistema de monitoramento inteligente de um satélite de telecomunicações em órbita baixa (LEO), similar ao Starlink ou OneWeb. O sistema simula dados de telemetria em tempo real — latência uplink, throughput do feixe, saúde da antena phased-array, beam steering e carga térmica do transponder — e usa IA generativa (via Ollama Cloud) para interpretar anomalias e traduzir cada evento técnico em impacto concreto para comunidades rurais brasileiras que dependem dessa conexão para acesso à saúde, educação e renda.

A interface é uma CLI estilo Claude Code, rodando inteiramente no terminal, sem dependência de internet além da API.

---

## 🎭 Persona atendida

O sistema foi projetado para três personas com necessidades distintas:

- **NOC Engineer da operadora** — precisa de diagnósticos rápidos, alertas com severidade classificada e sugestões de ação corretiva antes que o SLA seja violado.
- **Coordenador de programa de inclusão digital** — precisa entender, em linguagem não técnica, se as escolas e postos de saúde atendidos estão com conexão estável ou sob risco de interrupção.
- **Cliente final em comunidade rural** — beneficiário indireto: uma queda de throughput pode interromper uma teleconsulta médica ou uma aula ao vivo. O sistema articula exatamente esse impacto.

---

## 🛠 Tecnologias utilizadas

- Python 3.10+
- [Ollama Cloud API](https://ollama.com) — modelo `gpt-oss:120b`
- `ollama` — cliente oficial Python para Ollama Cloud
- `python-dotenv` — carregamento seguro de credenciais via `.env`
- `rich` — renderização de painéis, tabelas e formatação no terminal
- `prompt-toolkit` — input editável com histórico e estilo Claude Code
- `pyfiglet` — banner ASCII art

---

## ▶️ Como executar

### Pré-requisitos

- Python 3.10 ou superior instalado
- Conta gratuita no [Ollama Cloud](https://ollama.com) com API Key gerada

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/usuario/mission-control-ai.git
cd mission-control-ai

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# ou
.venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as credenciais
cp .env.example .env
# Abra o .env e preencha com sua chave:
# OLLAMA_API_KEY=sua_chave_aqui

# 5. Execute o sistema
python main.py
```

## 🌐 Interface Web (Bônus) - Streamlit

Além da CLI, o projeto também conta com uma interface web simples usando **Streamlit**.

### Como executar o Streamlit:

```bash
# Certifique-se de que as dependências estão instaladas
pip install -r requirements.txt

# Execute o Streamlit
streamlit run app.py


### Comandos disponíveis na CLI

| Comando | Descrição |
|---|---|
| `/help` | Lista todos os comandos disponíveis |
| `/status` | Exibe snapshot atual da telemetria do satélite |
| `/clear` | Limpa o terminal e reexibe o banner |
| `/about` | Informações sobre o sistema e a trilha ConnectSat |
| `/exit` | Encerra a CLI |
| `[qualquer pergunta]` | Envia para análise da IA com dados da telemetria atual |

---

## 🖼️ Demonstração

### Banner inicial e status da missão

![Banner ASCII e painel de status inicial do ConnectSat](assets/screenshot_banner.png)

### Alerta crítico com análise da IA

![Análise em tempo real de anomalia no transponder com impacto traduzido para comunidades](assets/screenshot_analise.png)

---

## 🧠 System Prompt

O system prompt completo está em [`prompts/system_prompt.md`](prompts/system_prompt.md).

Em resumo, o modelo é instruído a atuar como **analista sênior de operações do segmento espacial ConnectSat**, com as seguintes diretrizes:

- Sempre contextualizar análises técnicas com o impacto terrestre concreto (ex: "latência acima de 800ms interrompe teleconsultas em andamento na UBS de Altamira-PA")
- Classificar cada evento em severidade: `NORMAL`, `ATENÇÃO` ou `CRÍTICO`
- Propor ações corretivas claras e ordenadas por prioridade
- Adaptar o tom conforme a pergunta: técnico para NOC engineers, acessível para coordenadores de inclusão digital
- Nunca inventar dados — usar apenas os valores injetados dinamicamente no prompt

---

## 🧪 Cenários de teste demonstrados

1. **Operação normal** — todos os 5 parâmetros dentro dos ranges esperados; IA confirma saúde da missão e estima cobertura ativa.
2. **Latência crítica no uplink** — latência > 900ms detectada; alerta CRÍTICO gerado; IA descreve impacto em teleconsultas e sessões de EAD em andamento.
3. **Degradação de throughput** — feixe caindo abaixo de 40% da capacidade nominal; IA estima número de usuários afetados e sugere redistribuição de beam.
4. **Superaquecimento do transponder** — carga térmica acima do threshold; resposta automatizada ativa modo de proteção; IA explica risco de shutdown e janela de recuperação.
5. **Falha de beam steering** — desvio de apontamento acima de 0.05°; IA correlaciona com perda de cobertura em área geográfica específica.

---

## ⚠️ Limitações conhecidas

- A telemetria é **simulada** — os dados são gerados por funções Python com aleatoriedade controlada, não provenientes de um satélite real.
- O sistema não possui **persistência entre sessões** — o histórico de telemetria é reiniciado a cada execução de `python main.py`.
- A latência das respostas da IA depende da disponibilidade e carga da **Ollama Cloud API** — em horários de pico pode haver demora de 5–15 segundos por chamada.
- O modelo `gpt-oss:120b` é **não-determinístico**: respostas para o mesmo cenário podem variar entre execuções. O system prompt foi calibrado para minimizar essa variação, mas não eliminá-la.
- A interface é exclusivamente **CLI** — não há dashboard web ou visualização gráfica nesta versão.

---

## 💼 Proposta de valor / Modelo de negócio

### 1. Qual o problema real terrestre que esta missão resolve?

Aproximadamente **40 milhões de brasileiros** vivem em áreas rurais e periurbanas sem acesso à internet de qualidade. Escolas no interior do Pará, postos de saúde no Pantanal e pequenos produtores no semiárido nordestino dependem de conectividade satellite para acessar serviços essenciais. Uma interrupção de sinal de 2 horas pode cancelar 12 teleconsultas agendadas, derrubar aulas ao vivo de 300 alunos e impedir que agricultores acessem a plataforma de monitoramento de irrigação. O ConnectSat monitora proativamente o satélite que viabiliza essas conexões — e garante que anomalias sejam detectadas e corrigidas antes de virarem interrupção.

### 2. Quem paga pela solução?

Modelo **híbrido público-privado**:
- **Setor público** (MEC, Ministério da Saúde, estados): contrata cobertura para escolas e UBSs via programas como Conecta Brasil e Prontuário Eletrônico do Cidadão.
- **Setor privado** (operadoras de telecomunicações, cooperativas agrícolas, fintechs rurais): paga por SLA de disponibilidade e analytics de desempenho de feixe.
- O sistema de monitoramento é vendido como SaaS para a operadora do satélite, que repassa o custo diluído nas assinaturas dos contratos institucionais.

### 3. Métrica de impacto

Se o satélite operar 100% saudável por 1 ano com o ConnectSat ativo:

- **~1.200 escolas rurais** mantêm conectividade ininterrupta para aulas ao vivo
- **~80.000 teleconsultas** realizadas sem interrupção por queda de sinal
- **~15.000 pequenos produtores** mantêm acesso contínuo a plataformas de agricultura de precisão
- Redução estimada de **~35% no tempo médio de resolução** de incidentes de satélite (de 4h para 2,6h), por detecção antecipada via alertas do sistema

### 4. Modelo de negócio

**SaaS B2B** com duas camadas:

- **Tier Operacional** (NOC Engineers): assinatura mensal por satélite monitorado, com dashboard em tempo real, alertas por severidade e histórico de incidentes. Preço baseado em número de feixes ativos.
- **Tier Estratégico** (gestores de programas governamentais): relatórios mensais de disponibilidade por município, correlacionados com impacto em indicadores educacionais e de saúde. Vendido como dado-como-serviço (DaaS) para secretarias estaduais e ministérios.

---

## 🎬 Vídeo de demonstração

🔗 [Assistir demonstração no YouTube](https://www.youtube.com/watch?v=SEU_ID_AQUI)

> Configurado como "Não listado" no YouTube. Duração: ~3 minutos.

---

## 📁 Estrutura do projeto

```
mission-control-ai/
│
├── README.md
├── main.py
├── banner_ascii.py
├── requirements.txt
├── .env.example
├── .env                    ← NÃO commitado (.gitignore)
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── ui.py
│   ├── engine.py
│   ├── telemetria.py
│   └── alertas.py
│
├── prompts/
│   └── system_prompt.md
│
├── data/
│   └── cenarios.json
│
└── assets/
    ├── screenshot_banner.png
    └── screenshot_analise.png
```

---

*FIAP · Ciência da Computação · Global Solution 2026.1 · Disciplina: Prompt Engineering and Artificial Intelligence*
