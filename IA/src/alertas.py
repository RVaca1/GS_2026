"""Sistema de avaliação de alertas para ConnectSat."""

from typing import Dict, List, Tuple

def avaliar_alertas(telemetria: Dict) -> List[Dict]:
    """
    Avalia a telemetria e retorna lista de alertas.
    """
    alertas = []
    
    # 1. Latência
    lat = telemetria["latencia_uplink_ms"]
    if lat > 900:
        alertas.append({
            "parametro": "Latência Uplink",
            "valor": f"{lat} ms",
            "severidade": "CRÍTICO",
            "mensagem": "Latência extremamente alta - risco de interrupção total de serviços"
        })
    elif lat > 650:
        alertas.append({
            "parametro": "Latência Uplink",
            "valor": f"{lat} ms",
            "severidade": "ATENÇÃO",
            "mensagem": "Latência elevada - pode afetar videochamadas e aulas online"
        })

    # 2. Throughput
    tp = telemetria["throughput_mbps"]
    if tp < 35:
        alertas.append({
            "parametro": "Throughput do Feixe",
            "valor": f"{tp} Mbps",
            "severidade": "CRÍTICO",
            "mensagem": "Queda severa de capacidade - múltiplas comunidades sem conexão"
        })
    elif tp < 60:
        alertas.append({
            "parametro": "Throughput do Feixe",
            "valor": f"{tp} Mbps",
            "severidade": "ATENÇÃO",
            "mensagem": "Degradação de capacidade"
        })

    # 3. Carga Térmica
    temp = telemetria["carga_termica_transponder_c"]
    if temp > 72:
        alertas.append({
            "parametro": "Carga Térmica Transponder",
            "valor": f"{temp}°C",
            "severidade": "CRÍTICO",
            "mensagem": "Superaquecimento crítico - risco de shutdown automático"
        })
    elif temp > 58:
        alertas.append({
            "parametro": "Carga Térmica Transponder",
            "valor": f"{temp}°C",
            "severidade": "ATENÇÃO",
            "mensagem": "Temperatura elevada"
        })

    # 4. Beam Steering
    beam = telemetria["beam_steering_desvio_graus"]
    if beam > 0.08:
        alertas.append({
            "parametro": "Beam Steering",
            "valor": f"{beam}°",
            "severidade": "CRÍTICO",
            "mensagem": "Desvio significativo de apontamento - perda de cobertura"
        })

    # 5. Saúde da Antena
    saude = telemetria["saude_antena_phased_array"]
    if saude < 88:
        alertas.append({
            "parametro": "Saúde Antena Phased Array",
            "valor": f"{saude}%",
            "severidade": "ATENÇÃO",
            "mensagem": "Degradação detectada na antena"
        })

    return alertas


def formatar_alertas_para_ia(telemetria: Dict, alertas: List[Dict]) -> str:
    """Formata telemetria + alertas em texto para enviar à IA."""
    linhas = [
        f"🛰 Telemetria ConnectSat - {telemetria['timestamp']}",
        f"Satélite: {telemetria['satelite_id']}",
        f"Região: {telemetria['regiao_cobertura']}\n",
        "📊 PARÂMETROS ATUAIS:",
        f"• Latência Uplink: {telemetria['latencia_uplink_ms']} ms",
        f"• Throughput: {telemetria['throughput_mbps']} Mbps",
        f"• Saúde Antena: {telemetria['saude_antena_phased_array']}%",
        f"• Desvio Beam Steering: {telemetria['beam_steering_desvio_graus']}°",
        f"• Carga Térmica: {telemetria['carga_termica_transponder_c']}°C",
        f"• Usuários Ativos: {telemetria['usuarios_ativos']:,}\n"
    ]

    if alertas:
        linhas.append("🚨 ALERTAS ATIVOS:")
        for a in alertas:
            emoji = "🔴" if a["severidade"] == "CRÍTICO" else "🟠"
            linhas.append(f"{emoji} {a['severidade']} | {a['parametro']}: {a['valor']}")
            linhas.append(f"   → {a['mensagem']}")
    else:
        linhas.append("✅ Nenhum alerta ativo - Operação normal")

    return "\n".join(linhas)