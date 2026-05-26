Explicação da Lógica Utilizada
1. Estrutura de Dados (struct Leitura)
Criamos uma estrutura (struct) para agrupar os três dados de cada sensor:

temperatura (float): aceita valores decimais
energia (float): percentual de 0 a 100
comunicacao (int): valor binário — 1 (ativa) ou 0 (falha)

Isso facilita armazenar e manipular os dados de cada leitura como uma unidade.
2. Histórico com Vetor (historico[])
Um vetor de até 10 leituras armazena o histórico. Quando o vetor está cheio, os dados mais antigos são descartados (fila deslizante), garantindo sempre as últimas 10 leituras.
3. Menu Interativo com switch()
O switch controla o fluxo principal do programa:

case 1 → chama inserir_dados()
case 2 → chama visualizar_status()
case 3 → chama executar_analise()
case 4 → chama ver_historico()
case 0 → encerra o programa

O loop do-while mantém o menu ativo enquanto o usuário não escolher a opção 0.
4. Verificação Automática com Condicionais
A análise usa if/else para classificar cada valor:
CondiçãoRespostatemperatura > 80Alerta de superaquecimentoenergia < 20Alerta de economia de energiacomunicacao == 0Falha de comunicação
5. Análise com Laço for
A função executar_analise() percorre todo o vetor historico[] com um laço for, calculando:

Média de temperatura e energia
Temperatura máxima registrada
Energia mínima registrada
Quantidade de alertas de cada tipo

6. Funções Separadas
Cada funcionalidade está em uma função distinta (inserir_dados, visualizar_status, executar_analise, ver_historico), tornando o código organizado, legível e fácil de manter.
7. Cores no Terminal (bônus)
Utilizamos sequências ANSI para colorir o terminal:

🟢 Verde = normal/ok
🟡 Amarelo = atenção
🔴 Vermelho = alerta crítico