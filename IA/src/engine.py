"""Motor de análise da Mission Control AI."""

import os
from pathlib import Path

from dotenv import load_dotenv
from ollama import Client

load_dotenv()

# Identificação da trilha
# "agrosat" | "envirosat" | "connectsat" | "mobilitysat"
TRILHA = "envirosat"

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {os.environ.get('OLLAMA_API_KEY', '')}"
    }
)


def llm(prompt, system=None, max_tokens=800, temperature=0.3):
    """Envia prompt ao gpt-oss:120b via Ollama Cloud."""

    messages = []

    if system:
        messages.append({
            "role": "system",
            "content": system
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        response = client.chat(
            model="gpt-oss:120b",
            messages=messages,
            options={
                "num_predict": max_tokens,
                "temperature": temperature
            },
            stream=False
        )

        return response["message"]["content"].strip()

    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"


def load_system_prompt():
    """Lê o system prompt do arquivo prompts/system_prompt.md."""

    path = Path("prompts/system_prompt.md")

    if path.exists():
        return path.read_text(encoding="utf-8")

    return "Você é um assistente."


class MissionEngine:
    """Motor de análise principal."""

    def __init__(self):
        self.trilha = TRILHA
        self.system_prompt = load_system_prompt()

    def is_ready(self):
        """Indica se o motor está operacional."""
        return True

    def status_snapshot(self):
        """Retorna resumo do estado atual."""

        return (
            "🛰 Mission Control ONLINE\n\n"
            f"Trilha ativa: {self.trilha}\n"
            "Modelo: gpt-oss:120b\n"
            "Status IA: operacional\n"
            "Telemetria: aguardando integração\n"
        )

    def analyze(self, pergunta_usuario):
        """
        Analisa a pergunta com IA.
        Futuramente:
        1. Coletar telemetria
        2. Avaliar alertas
        3. Montar contexto
        4. Consultar IA
        """

        prompt = f"""
Você está operando a Mission Control AI.

Trilha ativa: {self.trilha}

Pergunta do operador:
{pergunta_usuario}
"""

        return llm(
            prompt=prompt,
            system=self.system_prompt
        )