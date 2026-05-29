"""Interface CLI estilo Claude Code — aprimorada."""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import pyfiglet
from datetime import datetime

console = Console()

session = PromptSession(
    style=Style.from_dict({
        "prompt": "#06B6D4 bold"
    })
)


def show_banner():
    """Banner melhorado."""
    banner = pyfiglet.figlet_format("Mission Control", font="ansi_shadow")
    console.print(Text(banner, style="bold #06B6D4"))

    console.print(
        Panel.fit(
            "🚀 ConnectSat — Monitoramento de Satélite LEO\n"
            "Conectividade Rural no Brasil • IA Generativa\n"
            "Use /help para comandos • /exit para sair",
            title="◆ MISSION CONTROL AI",
            border_style="#06B6D4",
            padding=(1, 2)
        )
    )


def show_response(text):
    """Mostra resposta com timestamp."""
    now = datetime.now().strftime("%H:%M:%S")
    console.print(
        Panel(
            text,
            title="◆ Mission Control",
            subtitle=f"{now} • ConnectSat",
            border_style="#06B6D4",
            padding=(1, 2)
        )
    )


def run_cli(engine):
    """Loop principal da CLI."""
    show_banner()

    if not engine.is_ready():
        console.print("⚠️ Engine não está pronto!", style="red")

    while True:
        try:
            user_input = session.prompt("❯ ").strip()

            if not user_input:
                continue

            if user_input == "/exit":
                console.print("👋 Encerrando Mission Control...", style="yellow")
                break

            if user_input == "/help":
                console.print(
                    Panel(
                        "/help   → Mostra este menu\n"
                        "/status → Telemetria atual\n"
                        "/about  → Sobre o projeto\n"
                        "/clear  → Limpa tela\n"
                        "/exit   → Sair",
                        title="Comandos Disponíveis",
                        border_style="blue"
                    )
                )
                continue

            if user_input == "/status":
                show_response(engine.status_snapshot())
                continue

            if user_input == "/about":
                show_response(engine.about())
                continue

            if user_input == "/clear":
                console.clear()
                show_banner()
                continue

            # Análise com IA
            with console.status("Analisando com IA...", spinner="dots"):
                resposta = engine.analyze(user_input)
            show_response(resposta)

        except (KeyboardInterrupt, EOFError):
            break