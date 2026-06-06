import os
import time
import random
import threading
import csv
from datetime import datetime


class SpaceEnergyMonitor:
    def __init__(self):
        self.solar = 85.0  # Energia Renovável - Painéis Solares
        self.battery = 78.0  # Nível da Bateria
        self.temp = 24.5  # Temperatura dos Módulos
        self.comm = 96.0  # Comunicação com Terra
        self.consumption = 48.0  # Consumo de Energia
        self.simulation_running = True
        self.logs = []
        self.log_file = "mission_logs.csv"
        self.initialize_log_file()

    def initialize_log_file(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Solar", "Battery", "Temp", "Comm", "Consumption", "Status", "Event"])

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_status(self):
        if self.battery < 25 or self.temp > 45 or self.solar < 30:
            return "CRÍTICO", "\033[91m"  # Vermelho
        elif self.battery < 50 or self.temp > 35:
            return "ATENÇÃO", "\033[93m"  # Amarelo
        return "NORMAL", "\033[92m"  # Verde

    def print_header(self):
        self.clear_screen()
        print("=" * 75)
        print("🌌 MISSÃO ESPACIAL - SISTEMA DE MONITORAMENTO ENERGÉTICO")
        print("🔋 FOCO: ENERGIAS RENOVÁVEIS E SUSTENTABILIDADE")
        print("=" * 75)
        print(f"Hora da Simulação: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

    def print_status(self):
        status, color = self.get_status()
        print(f"Status da Missão: {color}{status}\033[0m\n")

        print(f"☀️  Painéis Solares     : {self.solar:6.1f}%   (Energia Renovável)")
        print(f"🔋  Bateria             : {self.battery:6.1f}%")
        print(f"🌡️  Temperatura         : {self.temp:6.1f}°C")
        print(f"📡  Comunicação         : {self.comm:6.1f}%")
        print(f"⚡  Consumo Atual       : {self.consumption:6.1f} kW")
        print("-" * 75)

    def take_decision(self):
        """Tomada de Decisão Automática"""
        timestamp = datetime.now().strftime("%H:%M:%S")

        if self.battery < 30:
            self.consumption = max(20, self.consumption * 0.75)
            self.add_log(f"[{timestamp}] 🤖 DECISÃO: Modo Economia Ativado (Consumo reduzido)")
        if self.temp > 40:
            self.add_log(f"[{timestamp}] 🤖 DECISÃO: Reduzindo carga térmica dos módulos")
        if self.solar < 40 and self.battery > 50:
            self.add_log(f"[{timestamp}] 🤖 DECISÃO: Otimizando ângulo dos painéis solares")

    def check_alerts(self):
        timestamp = datetime.now().strftime("%H:%M:%S")

        if self.battery < 25:
            self.add_log(f"[{timestamp}] 🔥 ALERTA CRÍTICO: Bateria em nível crítico!")
        if self.temp > 42:
            self.add_log(f"[{timestamp}] 🔥 ALERTA: Sobreaquecimento detectado!")
        if self.solar < 35:
            self.add_log(f"[{timestamp}] ☀️ ALERTA: Baixa eficiência solar")
        if self.comm < 85:
            self.add_log(f"[{timestamp}] 📡 ALERTA: Comunicação instável")

    def add_log(self, message):
        status, _ = self.get_status()
        self.logs.append(message)
        if len(self.logs) > 15:
            self.logs.pop(0)

        # Salva no CSV (persistência)
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                round(self.solar, 1), round(self.battery, 1), round(self.temp, 1),
                round(self.comm, 1), round(self.consumption, 1), status, message
            ])

    def print_logs(self):
        print("📜 LOG DE ALERTAS E DECISÕES:")
        print("-" * 75)
        for log in self.logs[-7:]:
            print(log)
        print("-" * 75)

    def simulate_data(self):
        while self.simulation_running:
            self.solar = max(10, min(100, self.solar + random.uniform(-7, 8)))
            self.battery = max(5, min(100, self.battery - 0.5 + (self.solar * 0.03)))
            self.temp = max(15, min(55, self.temp + random.uniform(-1.8, 2.8)))
            self.comm = max(70, min(100, self.comm + random.uniform(-5, 4)))
            self.consumption = max(25, min(75, self.consumption + random.uniform(-6, 7)))

            self.check_alerts()
            self.take_decision()
            time.sleep(2)

    def save_report(self):
        filename = f"relatorio_missao_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        with open(filename, 'w') as f:
            f.write("RELATÓRIO FINAL - MISSÃO ESPACIAL\n")
            f.write("=" * 50 + "\n")
            f.write(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n")
            f.write(f"☀️ Solar Final: {self.solar:.1f}%\n")
            f.write(f"🔋 Bateria Final: {self.battery:.1f}%\n")
            f.write(f"🌡️ Temperatura: {self.temp:.1f}°C\n")
            f.write(f"Total de Alertas: {len(self.logs)}\n")
        print(f"\n✅ Relatório salvo: {filename}")

    def run(self):
        thread = threading.Thread(target=self.simulate_data, daemon=True)
        thread.start()

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
                self.simulation_running = not self.simulation_running
                print(f"Simulação {'ativada' if self.simulation_running else 'pausada'}.")
            elif op == "4":
                self.save_report()
            elif op == "0":
                print("\nFinalizando sistema de monitoramento...")
                break
            else:
                print("Opção inválida!")

            time.sleep(1.2)

    def manual_input(self):
        try:
            print("\n--- Inserir Dados Manualmente ---")
            self.solar = float(input("☀️ Solar (%): "))
            self.battery = float(input("🔋 Bateria (%): "))
            self.temp = float(input("🌡️ Temperatura (°C): "))
            self.comm = float(input("📡 Comunicação (%): "))
            self.consumption = float(input("⚡ Consumo (kW): "))
            self.add_log(f"[{datetime.now().strftime('%H:%M:%S')}] Dados atualizados manualmente.")
            print("✅ Dados atualizados!")
        except:
            print("❌ Erro: Digite apenas números.")

    def emergency_mode(self):
        self.battery = 98.0
        self.temp = 21.0
        self.solar = 96.0
        self.comm = 99.5
        self.consumption = 35.0
        self.add_log(f"[{datetime.now().strftime('%H:%M:%S')}] 🚨 MODO DE EMERGÊNCIA ATIVADO - Sistemas otimizados")


if __name__ == "__main__":
    monitor = SpaceEnergyMonitor()
    monitor.run()