"""Motor de análise da Mission Control AI — ConnectSat."""

import os
import json
from pathlib import Path

from dotenv import load_dotenv
from ollama import Client

# Imports corretos (dentro de src/)
from .telemetria import get_telemetria
from .alertas import avaliar_alertas, formatar_alertas_para_ia

load_dotenv()

TRILHA = "connectsat"

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {os.environ.get('OLLAMA_API_KEY', '')}"
    }
)


def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao modelo via Ollama Cloud."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    try:
        response = client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={"num_predict": max_tokens, "temperature": temperature},
            stream=False
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {str(e)}"


def load_system_prompt():
    """Carrega o system prompt."""
    path = Path("prompts/system_prompt.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "Você é um assistente de operações espaciais."


class MissionEngine:
    """Motor principal."""

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()
        self.cenarios = self._carregar_cenarios()

    def _carregar_cenarios(self):
        """Carrega cenários de teste."""
        try:
            path = Path("data/cenarios.json")
            if path.exists():
                with open(path, encoding="utf-8") as f:
                    return json.load(f).get("cenarios", [])
        except:
            pass
        return []

    def is_ready(self):
        return True

    def status_snapshot(self):
        """Retorna snapshot da telemetria."""
        telemetria = get_telemetria()
        alertas = avaliar_alertas(telemetria)
        
        status = (
            "🛰 Mission Control ONLINE\n\n"
            f"Trilha: {self.trilha.upper()}\n"
            f"Satélite: {telemetria['satelite_id']}\n"
            f"Status Geral: {telemetria['status_geral']}\n"
            f"Latência Uplink: {telemetria['latencia_uplink_ms']} ms\n"
            f"Throughput: {telemetria['throughput_mbps']} Mbps\n"
            f"Usuários Ativos: {telemetria['usuarios_ativos']:,}\n"
        )
        if alertas:
            status += f"\n🚨 {len(alertas)} alerta(s) ativo(s)"
        return status

    def about(self):
        """Informações sobre o projeto."""
        return (
            "🚀 **Mission Control AI - ConnectSat**\n\n"
            "Sistema de monitoramento inteligente de satélite LEO para conectividade rural no Brasil.\n"
            "Trilha 3 - Comunicação e Inclusão Digital.\n\n"
            "Tecnologias: Python + Ollama Cloud (gpt-oss:120b) + Rich CLI\n"
            "Objetivo: Transformar telemetria técnica em impacto humano real."
        )

    def analyze(self, pergunta_usuario):
        """Análise completa com telemetria + IA."""
        telemetria = get_telemetria()
        alertas = avaliar_alertas(telemetria)
        contexto = formatar_alertas_para_ia(telemetria, alertas)

        prompt = f"""
{contexto}

---
**Pergunta do operador:**
{pergunta_usuario}
"""

        return llm(prompt=prompt, system=self.system_prompt)