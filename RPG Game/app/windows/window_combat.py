import tkinter as tk
import random

def create(app):
    app.sixth_window = tk.Toplevel(app.root)
    app.sixth_window.title("Combat Simulator")
    app.sixth_window.geometry("400x300+1250+100")

    tk.Label(app.sixth_window, text="Select Attacker", font=("Arial", 14)).pack(pady=5)
    app.attacker_var = tk.StringVar()
    tk.OptionMenu(app.sixth_window, app.attacker_var, *app.players.keys()).pack()

    tk.Label(app.sixth_window, text="Select Defender", font=("Arial", 14)).pack(pady=5)
    app.defender_var = tk.StringVar()
    tk.OptionMenu(app.sixth_window, app.defender_var, *app.players.keys()).pack()

    def simulate():
        attacker = app.attacker_var.get()
        defender = app.defender_var.get()
        if not attacker or not defender:
            app.combat_result.config(text="Please select both an attacker and a defender.")
            return
        if attacker == defender:
            app.combat_result.config(text="A player cannot attack themselves!")
            return

        atk_stats = app.players[attacker]
        def_stats = app.players[defender]
        atk_roll = random.randint(1, 20) + atk_stats.get("Strength", 0)
        def_roll = random.randint(1, 20) + def_stats.get("Defense", 0)

        result = f"{attacker} attacks {defender}!\n"
        result += f"Attack roll: {atk_roll} vs Defense roll: {def_roll}\n"
        if atk_roll > def_roll:
            damage = max(1, atk_roll - def_roll)
            def_stats["HP"] = max(0, def_stats["HP"] - damage)
            result += f"Hit! {defender} takes {damage} damage. HP is now {def_stats['HP']}\n"
        else:
            result += f"Miss! {defender} takes no damage.\n"

        app.combat_result.config(text=result)

    tk.Button(app.sixth_window, text="Simulate Attack", font=("Arial", 12), command=simulate).pack(pady=10)
    app.combat_result = tk.Label(app.sixth_window, text="", font=("Arial", 12), wraplength=350, justify="left")
    app.combat_result.pack(pady=10)