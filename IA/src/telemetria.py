"""Módulo de geração de telemetria simulada para ConnectSat."""

import random
from datetime import datetime
from typing import Dict

class TelemetriaConnectSat:
    """Gerencia a telemetria simulada do satélite de telecomunicações."""

    def __init__(self):
        self.satelite_id = "CONNECTSAT-LEO-07"
        self.orbit = "LEO 550km"
        self.regiao_cobertura = "Brasil (principalmente Norte e Nordeste)"

    def gerar_telemetria(self) -> Dict:
        """Gera dados simulados de telemetria."""
        
        # Valores base com pequena variação aleatória
        latencia = round(random.gauss(420, 180), 1)          # ms
        throughput = round(random.gauss(85, 25), 1)          # Mbps
        saude_antena = round(random.gauss(96, 4), 1)         # %
        beam_steering = round(random.gauss(0.02, 0.015), 3)  # graus
        carga_termica = round(random.gauss(48, 12), 1)       # °C
        usuarios_ativos = random.randint(12400, 37800)

        # Ocasionais anomalias
        if random.random() < 0.15:  # 15% chance de anomalia
            latencia = round(latencia * random.uniform(1.8, 2.8), 1)
        if random.random() < 0.12:
            throughput = round(throughput * random.uniform(0.35, 0.65), 1)
        if random.random() < 0.10:
            carga_termica = round(carga_termica * random.uniform(1.4, 1.9), 1)

        telemetria = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "satelite_id": self.satelite_id,
            "orbit": self.orbit,
            "regiao_cobertura": self.regiao_cobertura,
            "latencia_uplink_ms": latencia,
            "throughput_mbps": throughput,
            "saude_antena_phased_array": saude_antena,
            "beam_steering_desvio_graus": beam_steering,
            "carga_termica_transponder_c": carga_termica,
            "usuarios_ativos": usuarios_ativos,
            "status_geral": "OPERACIONAL" if latencia < 700 and throughput > 50 else "DEGRADADO"
        }
        
        return telemetria


def get_telemetria() -> Dict:
    """Função principal para obter telemetria (usada pelo engine)."""
    telemetria = TelemetriaConnectSat()
    return telemetria.gerar_telemetria()