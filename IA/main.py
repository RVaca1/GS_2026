"""Mission Control AI — ponto de entrada do sistema."""
from src.ui import run_cli
from src.engine import MissionEngine
if __name__ == "__main__":   # ← Correto (dois underscores antes e depois)
    engine = MissionEngine()
    run_cli(engine)