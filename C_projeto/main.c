#include <stdio.h>
#include <string.h>

#define MAX_LEITURAS 10

struct Missao {
	float temperatura;
	int energia;
	int comunicacao;
};

int read_int(const char *prompt, int min, int max)
{
	char buf[64];
	int v;
	for (;;) {
		printf("%s", prompt);
		if (!fgets(buf, sizeof buf, stdin))
			continue;
		if (sscanf(buf, "%d", &v) == 1 && v >= min && v <= max)
			return v;
		printf("Valor invalido! Digite um inteiro entre %d e %d.\n", min, max);
	}
}

float read_float(const char *prompt, float min, float max)
{
	char buf[64];
	float f;
	for (;;) {
		printf("%s", prompt);
		if (!fgets(buf, sizeof buf, stdin))
			continue;
		if (sscanf(buf, "%f", &f) == 1 && f >= min && f <= max)
			return f;
		printf("Valor invalido! Digite um numero entre %.2f e %.2f.\n", min, max);
	}
}

void inserirDados(struct Missao *m)
{
	printf("\n=== INSERIR DADOS DA MISSAO ===\n");
	m->temperatura = read_float("Temperatura da nave: ", -200.0f, 500.0f);
	m->energia = read_int("Nivel de energia (0 a 100): ", 0, 100);
	m->comunicacao = read_int("Status da comunicacao (1 = OK / 0 = FALHA): ", 0, 1);
	printf("\nDados registrados com sucesso!\n");
}

void visualizarStatus(struct Missao m)
{
	printf("\n=== STATUS ATUAL DA MISSAO ===\n");
	printf("Temperatura: %.2f C\n", m.temperatura);
	printf("Energia: %d%%\n", m.energia);
	printf("Comunicacao: %s\n", m.comunicacao == 1 ? "[OK]" : "[FALHA]");
}

void analisarMissao(struct Missao m)
{
	printf("\n=== ANALISE DA MISSAO ===\n");

	if (m.temperatura > 100)
		printf("ALERTA CRITICO: Temperatura extremamente alta!\n");
	else if (m.temperatura > 80)
		printf("ALERTA: Superaquecimento detectado!\n");
	else
		printf("Temperatura dentro do normal.\n");

	if (m.energia <= 5)
		printf("ALERTA CRITICO: Energia extremamente baixa!\n");
	else if (m.energia < 20)
		printf("ALERTA: Economia de energia ativada!\n");
	else
		printf("Nivel de energia adequado.\n");

	if (m.comunicacao == 0)
		printf("ALERTA: Falha de comunicacao!\n");
	else
		printf("Comunicacao funcionando normalmente.\n");

	if (m.temperatura <= 80 && m.energia >= 20 && m.comunicacao == 1)
		printf("\nSTATUS GERAL: OPERACIONAL\n");
	else
		printf("\nSTATUS GERAL: ATENCAO NECESSARIA\n");
}

void mostrarHistorico(struct Missao historico[], int total)
{
	int i;
	printf("\n=== HISTORICO DE LEITURAS ===\n");
	if (total == 0) {
		printf("Nenhuma leitura registrada.\n");
		return;
	}
	for (i = 0; i < total; i++) {
		printf("\nLeitura %d\n", i + 1);
		printf("Temperatura: %.2f C\n", historico[i].temperatura);
		printf("Energia: %d%%\n", historico[i].energia);
		printf("Comunicacao: %s\n", historico[i].comunicacao == 1 ? "[OK]" : "[FALHA]");
	}
}

int main(void)
{
	struct Missao missaoAtual = {0.0f, 100, 1};
	struct Missao historico[MAX_LEITURAS];
	int opcao;
	int totalLeituras = 0;
	int dadosInseridos = 0;

	do {
		printf("\n=================================\n");
		printf(" SISTEMA DE MONITORAMENTO ESPACIAL\n");
		printf("=================================\n");
		printf("1 - Inserir dados\n");
		printf("2 - Visualizar status\n");
		printf("3 - Executar analise\n");
		printf("4 - Mostrar historico\n");
		printf("0 - Encerrar sistema\n");

		opcao = read_int("\nEscolha uma opcao: ", 0, 4);

		switch (opcao) {
		case 1:
			inserirDados(&missaoAtual);
			dadosInseridos = 1;
			if (totalLeituras < MAX_LEITURAS) {
				historico[totalLeituras] = missaoAtual;
				totalLeituras++;
			} else {
				printf("\nHistorico cheio! Nao e possivel salvar mais leituras.\n");
			}
			break;
		case 2:
			if (!dadosInseridos) {
				printf("\nNenhum dado foi inserido ainda!\nUse a opcao 1 primeiro.\n");
			} else {
				visualizarStatus(missaoAtual);
			}
			break;
		case 3:
			if (!dadosInseridos) {
				printf("\nNenhum dado foi inserido ainda!\nUse a opcao 1 primeiro.\n");
			} else {
				analisarMissao(missaoAtual);
			}
			break;
		case 4:
			if (!dadosInseridos) {
				printf("\nNenhum dado foi inserido ainda!\nUse a opcao 1 primeiro.\n");
			} else {
				mostrarHistorico(historico, totalLeituras);
			}
			break;
		case 0:
			printf("\nEncerrando sistema...\n");
			break;
		default:
			printf("\nOpcao invalida!\n");
		}

	} while (opcao != 0);

	return 0;
}