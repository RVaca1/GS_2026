import os
import time
from datetime import datetime

from dotenv import load_dotenv
from ollama import Client

load_dotenv()

# Configuração Ollama Cloud
client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {os.environ.get('OLLAMA_API_KEY', '')}"
    }
)
api = os.environ.get("OLLAMA_API_KEY")

print(
    "API KEY carregada:",
    "OK" if api else "FALTANDO"
)

def llm(prompt, max_tokens=800, temperature=0.3):
    """Envia prompt ao gpt-oss:120b via Ollama Cloud e retorna texto."""

    try:
        response = client.chat(
            model="gpt-oss:120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "num_predict": max_tokens,
                "temperature": temperature
            },
            stream=False
        )
        
        return response["message"]["content"].strip()

    except Exception as e:
        return f"⚠️ Erro ao consultar IA: {e}"