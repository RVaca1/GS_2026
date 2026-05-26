/*
 * GS2026.1 - Monitoramento de Missao Espacial
 * Linguagem: C
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* ===== CONSTANTES ===== */
#define MAX_HISTORICO 10

/* ===== ESTRUTURA DE DADOS ===== */
typedef struct {
    float temperatura;
    float energia;
    int comunicacao; /* 1 = ativa, 0 = falha */
} Leitura;

/* ===== VARIAVEIS GLOBAIS ===== */
Leitura historico[MAX_HISTORICO];
int total_leituras = 0;

/* ===== FUNCOES AUXILIARES ===== */

void limpar_tela() {
    system("cls");
}

void linha_divisoria() {
    printf("===================================================\n");
}

void cabecalho() {
    linha_divisoria();
    printf("       ** SISTEMA DE MONITORAMENTO ESPACIAL **\n");
    printf("              Missao GS-2026 v1.0\n");
    linha_divisoria();
}

/* ===== 1. CADASTRO DE DADOS ===== */
void inserir_dados() {
    Leitura nova;
    int com;

    limpar_tela();
    cabecalho();
    printf("\n  [INSERCAO DE DADOS DO SENSOR]\n\n");

    printf("  Temperatura atual (graus C): ");
    scanf("%f", &nova.temperatura);

    printf("  Nivel de energia (%%):        ");
    scanf("%f", &nova.energia);

    printf("  Comunicacao (1=Ativa / 0=Falha): ");
    scanf("%d", &com);
    nova.comunicacao = (com == 1) ? 1 : 0;

    if (total_leituras < MAX_HISTORICO) {
        historico[total_leituras] = nova;
        total_leituras++;
    } else {
        for (int i = 0; i < MAX_HISTORICO - 1; i++) {
            historico[i] = historico[i + 1];
        }
        historico[MAX_HISTORICO - 1] = nova;
    }

    printf("\n  >>> Dados registrados com sucesso!\n");
    printf("\n  Pressione ENTER para continuar...");
    getchar(); getchar();
}

/* ===== 2. VISUALIZAR STATUS ===== */
void visualizar_status() {
    limpar_tela();
    cabecalho();

    if (total_leituras == 0) {
        printf("\n  [AVISO] Nenhum dado inserido ainda.\n");
        printf("\n  Pressione ENTER para continuar...");
        getchar(); getchar();
        return;
    }

    Leitura ultima = historico[total_leituras - 1];

    printf("\n  [STATUS ATUAL DA MISSAO]\n\n");
    linha_divisoria();

    /* Temperatura */
    printf("  Temperatura : %.1f graus C", ultima.temperatura);
    if (ultima.temperatura > 80)
        printf("  *** ALERTA: SUPERAQUECIMENTO! ***\n");
    else if (ultima.temperatura > 60)
        printf("  (Atencao)\n");
    else
        printf("  (Normal)\n");

    /* Energia */
    printf("  Energia     : %.1f %%", ultima.energia);
    if (ultima.energia < 20)
        printf("  *** ALERTA: ECONOMIA DE ENERGIA! ***\n");
    else if (ultima.energia < 40)
        printf("  (Atencao)\n");
    else
        printf("  (Normal)\n");

    /* Comunicacao */
    printf("  Comunicacao : ");
    if (ultima.comunicacao == 0)
        printf("FALHA  *** ALERTA: COMUNICACAO PERDIDA! ***\n");
    else
        printf("ATIVA  (OK)\n");

    linha_divisoria();
    printf("\n  Total de leituras armazenadas: %d\n", total_leituras);

    printf("\n  Pressione ENTER para continuar...");
    getchar(); getchar();
}

/* ===== 3. ANALISE COMPLETA ===== */
void executar_analise() {
    limpar_tela();
    cabecalho();

    if (total_leituras == 0) {
        printf("\n  [AVISO] Nenhum dado para analisar.\n");
        printf("\n  Pressione ENTER para continuar...");
        getchar(); getchar();
        return;
    }

    printf("\n  [ANALISE DO HISTORICO DE LEITURAS]\n\n");
    linha_divisoria();

    float soma_temp = 0, soma_energia = 0;
    float max_temp = historico[0].temperatura;
    float min_energia = historico[0].energia;
    int falhas_com = 0;
    int alertas_temp = 0;
    int alertas_energia = 0;

    for (int i = 0; i < total_leituras; i++) {
        soma_temp    += historico[i].temperatura;
        soma_energia += historico[i].energia;

        if (historico[i].temperatura > max_temp)
            max_temp = historico[i].temperatura;
        if (historico[i].energia < min_energia)
            min_energia = historico[i].energia;
        if (historico[i].comunicacao == 0)
            falhas_com++;
        if (historico[i].temperatura > 80)
            alertas_temp++;
        if (historico[i].energia < 20)
            alertas_energia++;
    }

    printf("  Temperatura media    : %.1f graus C\n", soma_temp / total_leituras);
    printf("  Temperatura maxima   : %.1f graus C\n", max_temp);
    printf("  Energia minima       : %.1f %%\n", min_energia);
    printf("  Falhas de comunicacao: %d / %d leituras\n", falhas_com, total_leituras);

    linha_divisoria();
    printf("\n  ALERTAS DETECTADOS:\n");

    if (alertas_temp > 0)
        printf("  [!] Superaquecimento em %d leitura(s)!\n", alertas_temp);
    else
        printf("  [OK] Temperatura: sem alertas\n");

    if (alertas_energia > 0)
        printf("  [!] Energia critica em %d leitura(s)!\n", alertas_energia);
    else
        printf("  [OK] Energia: sem alertas\n");

    if (falhas_com > 0)
        printf("  [!] Comunicacao falhou em %d leitura(s)!\n", falhas_com);
    else
        printf("  [OK] Comunicacao: sem alertas\n");

    linha_divisoria();
    if (alertas_temp == 0 && alertas_energia == 0 && falhas_com == 0)
        printf("\n  STATUS GERAL: MISSAO OPERACIONAL\n");
    else
        printf("\n  STATUS GERAL: ATENCAO NECESSARIA\n");

    printf("\n  Pressione ENTER para continuar...");
    getchar(); getchar();
}

/* ===== HISTORICO DE LEITURAS ===== */
void ver_historico() {
    limpar_tela();
    cabecalho();
    printf("\n  [HISTORICO DE LEITURAS]\n\n");
    linha_divisoria();

    if (total_leituras == 0) {
        printf("  Nenhuma leitura registrada.\n");
    } else {
        printf("  %-5s %-14s %-14s %-15s\n", "No.", "Temp(graus C)", "Energia(%)", "Comunicacao");
        linha_divisoria();
        for (int i = 0; i < total_leituras; i++) {
            const char *com_str = (historico[i].comunicacao == 1) ? "ATIVA" : "FALHA";
            printf("  %-5d %-14.1f %-14.1f %-15s\n",
                i + 1,
                historico[i].temperatura,
                historico[i].energia,
                com_str);
        }
    }

    linha_divisoria();
    printf("\n  Pressione ENTER para continuar...");
    getchar(); getchar();
}

/* ===== MENU PRINCIPAL ===== */
int main() {
    int opcao;

    do {
        limpar_tela();
        cabecalho();

        printf("\n  MENU PRINCIPAL\n\n");
        printf("  [1] Inserir dados dos sensores\n");
        printf("  [2] Visualizar status atual\n");
        printf("  [3] Executar analise completa\n");
        printf("  [4] Ver historico de leituras\n");
        printf("  [0] Encerrar sistema\n");

        linha_divisoria();
        printf("  Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1: inserir_dados();     break;
            case 2: visualizar_status(); break;
            case 3: executar_analise();  break;
            case 4: ver_historico();     break;
            case 0:
                limpar_tela();
                cabecalho();
                printf("\n  Sistema encerrado. Boa missao!\n\n");
                break;
            default:
                printf("\n  Opcao invalida! Tente novamente.\n");
                getchar(); getchar();
        }

    } while (opcao != 0);

    return 0;
}