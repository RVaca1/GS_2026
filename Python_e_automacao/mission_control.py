# =========================================================
# MISSION CONTROL AI - FIAP GS2026.1
# =========================================================

missao = "Orion Test Alpha"
equipe = "Equipe Apollo"

# Matriz principal (mínimo 6 ciclos)
dados_missao = [
    [24, 92, 88, 96, 90],   # Ciclo 1 - Estável
    [27, 80, 72, 94, 85],   # Ciclo 2
    [31, 65, 58, 91, 70],   # Ciclo 3
    [36, 42, 38, 87, 55],   # Ciclo 4
    [39, 28, 19, 78, 35],   # Ciclo 5 - Crítico
    [34, 55, 32, 82, 50]    # Ciclo 6
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

# =========================================================
# FUNÇÕES DE ANÁLISE (Conforme PDF)
# =========================================================

def analisar_temperatura(v):
    if v > 35:
        return "CRÍTICO", "Risco de superaquecimento"
    elif v > 30:
        return "ATENÇÃO", "Temperatura elevada"
    elif v < 18:
        return "ATENÇÃO", "Temperatura muito baixa"
    else:
        return "NORMAL", "Temperatura estável"


def analisar_comunicacao(v):
    if v < 30:
        return "CRÍTICO", "Comunicação com a base em nível crítico"
    elif v < 60:
        return "ATENÇÃO", "Comunicação instável"
    else:
        return "NORMAL", "Comunicação estável"


def analisar_bateria(v):
    if v < 20:
        return "CRÍTICO", "Bateria em nível crítico"
    elif v < 50:
        return "ATENÇÃO", "Bateria abaixo do recomendado"
    else:
        return "NORMAL", "Energia estável"


def analisar_oxigenio(v):
    if v < 80:
        return "CRÍTICO", "Oxigênio em nível crítico"
    elif v < 90:
        return "ATENÇÃO", "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", "Oxigênio adequado"


def analisar_estabilidade(v):
    if v < 40:
        return "CRÍTICO", "Estabilidade operacional crítica"
    elif v < 70:
        return "ATENÇÃO", "Estabilidade operacional reduzida"
    else:
        return "NORMAL", "Estabilidade operacional adequada"


def pontuacao_risco(classificacao):
    if classificacao == "CRÍTICO":
        return 2
    elif classificacao == "ATENÇÃO":
        return 1
    return 0


def classificar_ciclo(risco_total):
    if risco_total <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco_total <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(risco_total, ciclo_class):
    if risco_total == 0:
        return "Manter operação normal e continuar monitoramento."
    elif risco_total <= 2:
        return "Verificar sistemas em atenção."
    elif risco_total <= 5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "ATIVAR PROTOCOLO DE EMERGÊNCIA: priorizar suporte à vida, energia e comunicação."


# =========================================================
# PROCESSAMENTO DOS CICLOS
# =========================================================

riscos_ciclos = []
pontuacao_areas = [0] * 5

print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {missao}")
print(f"Equipe: {equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

for i, ciclo in enumerate(dados_missao):
    temp, com, bat, oxi, est = ciclo

    clas_t, msg_t = analisar_temperatura(temp)
    clas_c, msg_c = analisar_comunicacao(com)
    clas_b, msg_b = analisar_bateria(bat)
    clas_o, msg_o = analisar_oxigenio(oxi)
    clas_e, msg_e = analisar_estabilidade(est)

    risco = (pontuacao_risco(clas_t) + pontuacao_risco(clas_c) +
             pontuacao_risco(clas_b) + pontuacao_risco(clas_o) +
             pontuacao_risco(clas_e))

    riscos_ciclos.append(risco)
    pontuacao_areas[0] += pontuacao_risco(clas_t)
    pontuacao_areas[1] += pontuacao_risco(clas_c)
    pontuacao_areas[2] += pontuacao_risco(clas_b)
    pontuacao_areas[3] += pontuacao_risco(clas_o)
    pontuacao_areas[4] += pontuacao_risco(clas_e)

    print(f"\nCICLO {i+1}")
    print("-" * 50)
    print(f"Temperatura: {temp} °C | {clas_t} | {msg_t}")
    print(f"Comunicação: {com}% | {clas_c} | {msg_c}")
    print(f"Bateria: {bat}% | {clas_b} | {msg_b}")
    print(f"Oxigênio: {oxi}% | {clas_o} | {msg_o}")
    print(f"Estabilidade: {est}% | {clas_e} | {msg_e}")
    print(f"Pontuação de risco do ciclo: {risco}")
    print(f"Classificação do ciclo: {classificar_ciclo(risco)}")
    print(f"Recomendação: {gerar_recomendacao(risco, classificar_ciclo(risco))}")


# =========================================================
# FUNÇÕES DE ANÁLISE FINAL
# =========================================================

def calcular_media(valores):
    return sum(valores) / len(valores)

def analisar_tendencia():
    if riscos_ciclos[-1] > riscos_ciclos[0]:
        return "A missão apresentou tendência de piora."
    elif riscos_ciclos[-1] < riscos_ciclos[0]:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada():
    max_pontos = max(pontuacao_areas)
    indice = pontuacao_areas.index(max_pontos)
    return areas_monitoradas[indice], max_pontos


# =========================================================
# RELATÓRIO FINAL
# =========================================================

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print(f"Missão: {missao} | Equipe: {equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}\n")

medias = [
    calcular_media([c[0] for c in dados_missao]),
    calcular_media([c[1] for c in dados_missao]),
    calcular_media([c[2] for c in dados_missao]),
    calcular_media([c[3] for c in dados_missao]),
    calcular_media([c[4] for c in dados_missao])
]

print("MÉDIAS DOS SISTEMAS:")
print(f"Temperatura: {medias[0]:.2f} °C")
print(f"Comunicação: {medias[1]:.2f}%")
print(f"Bateria: {medias[2]:.2f}%")
print(f"Oxigênio: {medias[3]:.2f}%")
print(f"Estabilidade: {medias[4]:.2f}%\n")

print(f"Risco médio da missão: {calcular_media(riscos_ciclos):.2f}")
print(f"Ciclo mais crítico: Ciclo {riscos_ciclos.index(max(riscos_ciclos)) + 1}")
print(f"Quantidade de ciclos críticos: {sum(1 for r in riscos_ciclos if r >= 6)}\n")

print("Tendência da missão:")
print(analisar_tendencia())

print("\nPontuação acumulada por área:")
for area, pontos in zip(areas_monitoradas, pontuacao_areas):
    print(f"{area}: {pontos} pontos")

area_afetada, pontos = identificar_area_mais_afetada()
print(f"\nÁrea mais afetada: {area_afetada}")

print(f"\nClassificação final da missão: {classificar_ciclo(calcular_media(riscos_ciclos))}")

print("\nConclusão:")
print("A missão apresentou instabilidade relevante durante a operação. "
      "A equipe deve manter o plano de contingência ativo.")