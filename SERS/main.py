import os
import time
import random
import threading
import csv
from datetime import datetime


class SpaceEnergyMonitor:
    def __init__(self):
        self.solar = 85.0
        self.battery = 78.0
        self.temp = 24.5
        self.comm = 96.0
        self.consumption = 48.0

        self.running = True
        self.paused = False

        self.lock = threading.Lock()

        self.logs = []
        self.total_alerts = 0

        self.log_file = "mission_logs.csv"

        self.initialize_log_file()

    def initialize_log_file(self):
        if not os.path.exists(self.log_file):
            with open(
                self.log_file,
                "w",
                newline="",
                encoding="utf-8-sig"
            ) as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Timestamp",
                    "Solar",
                    "Battery",
                    "Temp",
                    "Comm",
                    "Consumption",
                    "Status",
                    "Event"
                ])

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def get_status(self):
        if (
            self.battery < 25
            or self.temp > 45
            or self.solar < 30
            or self.comm < 80
        ):
            return "CRÍTICO", "\033[91m"

        elif (
            self.battery < 50
            or self.temp > 35
            or self.comm < 90
        ):
            return "ATENÇÃO", "\033[93m"

        return "NORMAL", "\033[92m"

    def print_header(self):
        self.clear_screen()

        print("=" * 75)
        print("🌌 MISSÃO ESPACIAL - SISTEMA DE MONITORAMENTO ENERGÉTICO")
        print("🔋 FOCO: ENERGIAS RENOVÁVEIS E SUSTENTABILIDADE")
        print("=" * 75)

        print(
            f"Hora da Simulação: "
            f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        )

    def print_status(self):
        with self.lock:
            status, color = self.get_status()

            print(f"Status da Missão: {color}{status}\033[0m\n")

            print(
                f"☀️  Painéis Solares     : {self.solar:6.1f}%"
            )
            print(
                f"🔋  Bateria             : {self.battery:6.1f}%"
            )
            print(
                f"🌡️  Temperatura         : {self.temp:6.1f}°C"
            )
            print(
                f"📡  Comunicação         : {self.comm:6.1f}%"
            )
            print(
                f"⚡  Consumo Atual       : {self.consumption:6.1f} kW"
            )

            print("-" * 75)

    def add_log(self, message):
        status, _ = self.get_status()

        self.logs.append(message)

        if len(self.logs) > 15:
            self.logs.pop(0)

        self.total_alerts += 1

        try:
            with open(
                self.log_file,
                "a",
                newline="",
                encoding="utf-8-sig"
            ) as f:
                writer = csv.writer(f)

                writer.writerow([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    round(self.solar, 1),
                    round(self.battery, 1),
                    round(self.temp, 1),
                    round(self.comm, 1),
                    round(self.consumption, 1),
                    status,
                    message
                ])

        except Exception as e:
            print(f"Erro ao gravar log: {e}")

    def print_logs(self):
        print("📜 LOG DE ALERTAS E DECISÕES")
        print("-" * 75)

        for log in self.logs[-7:]:
            print(log)

        print("-" * 75)

    def check_alerts(self):
        timestamp = datetime.now().strftime("%H:%M:%S")

        if self.battery < 25:
            self.add_log(
                f"[{timestamp}] 🔥 ALERTA CRÍTICO: "
                f"Bateria em nível crítico!"
            )

        if self.temp > 42:
            self.add_log(
                f"[{timestamp}] 🔥 ALERTA: "
                f"Sobreaquecimento detectado!"
            )

        if self.solar < 35:
            self.add_log(
                f"[{timestamp}] ☀️ ALERTA: "
                f"Baixa eficiência solar"
            )

        if self.comm < 85:
            self.add_log(
                f"[{timestamp}] 📡 ALERTA: "
                f"Comunicação instável"
            )

    def take_decision(self):
        timestamp = datetime.now().strftime("%H:%M:%S")

        if self.battery < 30:
            self.consumption = max(
                20,
                self.consumption * 0.75
            )

            self.add_log(
                f"[{timestamp}] 🤖 DECISÃO: "
                f"Modo Economia Ativado"
            )

        if self.temp > 40:
            self.add_log(
                f"[{timestamp}] 🤖 DECISÃO: "
                f"Reduzindo carga térmica"
            )

        if self.solar < 40 and self.battery > 50:
            self.add_log(
                f"[{timestamp}] 🤖 DECISÃO: "
                f"Otimizando painéis solares"
            )

    def simulate_data(self):
        while self.running:

            if self.paused:
                time.sleep(1)
                continue

            with self.lock:
                self.solar = max(
                    10,
                    min(
                        100,
                        self.solar + random.uniform(-7, 8)
                    )
                )

                self.battery = max(
                    5,
                    min(
                        100,
                        self.battery - 0.5 + (self.solar * 0.03)
                    )
                )

                self.temp = max(
                    15,
                    min(
                        55,
                        self.temp + random.uniform(-1.8, 2.8)
                    )
                )

                self.comm = max(
                    70,
                    min(
                        100,
                        self.comm + random.uniform(-5, 4)
                    )
                )

                self.consumption = max(
                    25,
                    min(
                        75,
                        self.consumption + random.uniform(-6, 7)
                    )
                )

                self.check_alerts()
                self.take_decision()

            time.sleep(2)

    def manual_input(self):
        try:
            print("\n--- Inserir Dados Manualmente ---")

            solar = float(input("☀️ Solar (%): "))
            battery = float(input("🔋 Bateria (%): "))
            temp = float(input("🌡️ Temperatura (°C): "))
            comm = float(input("📡 Comunicação (%): "))
            consumption = float(input("⚡ Consumo (kW): "))

            with self.lock:
                self.solar = max(0, min(100, solar))
                self.battery = max(0, min(100, battery))
                self.temp = max(-50, min(100, temp))
                self.comm = max(0, min(100, comm))
                self.consumption = max(0, consumption)

            self.add_log(
                f"[{datetime.now().strftime('%H:%M:%S')}] "
                f"Dados atualizados manualmente."
            )

            print("✅ Dados atualizados!")

        except ValueError:
            print("❌ Digite apenas números.")

    def emergency_mode(self):
        with self.lock:
            self.battery = 98.0
            self.temp = 21.0
            self.solar = 96.0
            self.comm = 99.5
            self.consumption = 20.0

        self.add_log(
            f"[{datetime.now().strftime('%H:%M:%S')}] "
            f"🚨 MODO DE EMERGÊNCIA ATIVADO"
        )

        print("✅ Sistemas estabilizados!")

    def save_report(self):
        filename = (
            f"relatorio_missao_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                "RELATÓRIO FINAL - MISSÃO ESPACIAL\n"
            )

            f.write("=" * 50 + "\n")

            f.write(
                f"Data: "
                f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
            )

            f.write(
                f"☀️ Solar Final: {self.solar:.1f}%\n"
            )

            f.write(
                f"🔋 Bateria Final: {self.battery:.1f}%\n"
            )

            f.write(
                f"🌡️ Temperatura Final: {self.temp:.1f}°C\n"
            )

            f.write(
                f"📡 Comunicação Final: {self.comm:.1f}%\n"
            )

            f.write(
                f"⚡ Consumo Final: {self.consumption:.1f} kW\n"
            )

            f.write(
                f"Total de Eventos: {self.total_alerts}\n"
            )

        print(f"\n✅ Relatório salvo: {filename}")

    def run(self):
        simulation_thread = threading.Thread(
            target=self.simulate_data
        )

        simulation_thread.start()

        while True:
            self.print_header()
            self.print_status()
            self.print_logs()

            print("\n[1] Inserir Dados Manualmente")
            print("[2] Ativar Modo Emergência")
            print("[3] Pausar/Retomar Simulação")
            print("[4] Gerar Relatório Final")
            print("[0] Sair")

            op = input("\nEscolha uma opção: ").strip()

            if op == "1":
                self.manual_input()

            elif op == "2":
                self.emergency_mode()

            elif op == "3":
                self.paused = not self.paused

                if self.paused:
                    print("⏸️ Simulação pausada.")
                else:
                    print("▶️ Simulação retomada.")

            elif op == "4":
                self.save_report()

            elif op == "0":
                print("\nFinalizando sistema...")

                self.running = False

                simulation_thread.join(timeout=2)

                break

            else:
                print("❌ Opção inválida.")

            time.sleep(1)


if __name__ == "__main__":
    monitor = SpaceEnergyMonitor()
    monitor.run()