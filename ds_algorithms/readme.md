# GS2026.1 — Sistema de Monitoramento de Missão Espacial

---

## Explicação da Lógica Utilizada

### 1. Estrutura de Dados — `struct Leitura`

Criamos uma `struct` para agrupar os três dados coletados por cada sensor em uma única unidade:

| Campo          | Tipo    | Descrição                          |
|----------------|---------|------------------------------------|
| `temperatura`  | float   | Temperatura em graus Celsius       |
| `energia`      | float   | Nível de energia (0 a 100%)        |
| `comunicacao`  | int     | Status binário: 1 = ativa, 0 = falha |

Usar uma struct facilita armazenar e passar os dados de cada leitura como um bloco coeso.

---

### 2. Histórico com Vetor — `historico[]`

Um vetor de até 10 posições armazena as leituras feitas pelo usuário. Quando o vetor está cheio, os dados mais antigos são descartados e os mais recentes assumem o lugar — funcionando como uma **fila deslizante** que sempre preserva as últimas 10 leituras.

---

### 3. Menu Interativo com `switch()`

O `switch` controla o fluxo principal do programa, direcionando cada escolha do usuário para a função correspondente:

| Opção | Função chamada        |
|-------|-----------------------|
| 1     | `inserir_dados()`     |
| 2     | `visualizar_status()` |
| 3     | `executar_analise()`  |
| 4     | `ver_historico()`     |
| 0     | Encerra o programa    |

O loop `do-while` mantém o menu ativo até que o usuário escolha a opção `0`.

---

### 4. Verificação Automática com `if/else`

A cada visualização ou análise, o programa classifica os valores lidos usando condicionais:

| Condição              | Resposta do sistema              |
|-----------------------|----------------------------------|
| `temperatura > 80`    | Alerta de superaquecimento       |
| `energia < 20`        | Alerta de economia de energia    |
| `comunicacao == 0`    | Falha de comunicação             |

---

### 5. Análise Estatística com laço `for`

A função `executar_analise()` percorre todo o vetor `historico[]` e calcula:

- Média de temperatura e energia
- Temperatura máxima registrada
- Energia mínima registrada
- Quantidade de alertas de cada tipo

---

### 6. Funções Separadas

Cada funcionalidade do sistema está isolada em sua própria função (`inserir_dados`, `visualizar_status`, `executar_analise`, `ver_historico`), tornando o código organizado, legível e fácil de manter ou expandir.

---

### 7. Bônus — Cores no Terminal

O código original inclui suporte a cores via sequências ANSI, utilizadas para destacar o status visualmente:

- Verde → situação normal
- Amarelo → atenção
- Vermelho → alerta crítico
