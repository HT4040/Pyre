import random
import tkinter as tk
from tkinter import ttk, scrolledtext

class CombatSimulatorWindow:
    def __init__(self, root, players):
        self.root = root
        self.players = players

        self.window = tk.Toplevel(self.root)
        self.window.title("Combat Simulator")
        self.window.geometry("600x550+710+400")

        tk.Label(self.window, text="Attacker:").pack()
        self.attacker_var = tk.StringVar(value=list(self.players.keys())[0])
        attacker_menu = tk.OptionMenu(self.window, self.attacker_var, *self.players.keys())
        attacker_menu.pack()

        tk.Label(self.window, text="Defender:").pack()
        self.defender_var = tk.StringVar(value=list(self.players.keys())[1] if len(self.players) > 1 else list(self.players.keys())[0])
        defender_menu = tk.OptionMenu(self.window, self.defender_var, *self.players.keys())
        defender_menu.pack()

        self.hp_bars = {}
        for player in self.players:
            tk.Label(self.window, text=f"{player} HP").pack(pady=(10, 0))
            hp_var = tk.IntVar(value=self.players[player]["HP"])
            bar = ttk.Progressbar(self.window, maximum=100, length=300, variable=hp_var)
            bar.pack()
            self.hp_bars[player] = hp_var

        self.combat_log = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, height=10, font=("Arial", 11))
        self.combat_log.pack(pady=10, fill=tk.BOTH, expand=True)

        simulate_btn = tk.Button(self.window, text="Simulate Turn", command=self.simulate_combat)
        simulate_btn.pack(pady=10)

        self.update_hp_bars()

    def simulate_combat(self):
        attacker = self.attacker_var.get()
        defender = self.defender_var.get()

        if attacker == defender:
            self.combat_log.insert(tk.END, "A player can't fight themselves!\n\n")
            self.combat_log.see(tk.END)
            return

        atk_stats = self.players[attacker]
        def_stats = self.players[defender]

        def attack_turn(attacker_name, attacker_stats, defender_name, defender_stats):
            roll = random.randint(1, 20)
            log = f"{attacker_name} rolls a {roll} against {defender_name}...\n"

            if roll >= 10:
                damage = max(attacker_stats.get("Strength", 0) - defender_stats.get("Defense", 0), 0)
                defender_stats["HP"] = max(defender_stats.get("HP", 0) - damage, 0)
                log += f"Hit! {attacker_name} deals {damage} damage.\n"
                log += f"{defender_name}'s HP is now {defender_stats['HP']}.\n"
            else:
                log += f"Miss! No damage dealt.\n"

            log += "\n"
            return log

        result_text = ""
        result_text += attack_turn(attacker, atk_stats, defender, def_stats)
        result_text += attack_turn(defender, def_stats, attacker, atk_stats)
        result_text += "-" * 40 + "\n"

        self.combat_log.insert(tk.END, result_text)
        self.combat_log.see(tk.END)
        self.update_hp_bars()

    def update_hp_bars(self):
        for player in self.players:
            hp = self.players[player].get("HP", 0)
            self.hp_bars[player].set(hp)
