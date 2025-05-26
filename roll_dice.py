import random
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image, ImageTk

class DiceApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Roll a d20 Dice")
        self.original_image = Image.open(image_path)
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.root.bind("<Configure>", self.resize_image)

        self.result_label = tk.Label(root, text="Press 'Roll Dice' to roll!", font=("Arial", 18), bg="#ffffff", fg="#000000")
        self.roll_button = tk.Button(root, text="Roll Dice (1-20)", font=("Arial", 16), padx=20, pady=10, command=self.roll_d20)

        self.result_window = self.canvas.create_window(0, 0, anchor="n", window=self.result_label)
        self.button_window = self.canvas.create_window(0, 0, anchor="n", window=self.roll_button)
        self.bg_image = None

        self.resize_image()

        self.players = {
            f"Player {i}": {"HP": 20, "Strength": 2, "Defense": 1, "Dexterity": 1}
            for i in range(1, 6)
        }
        self.turn_index = 0
        self.player_order = list(self.players.keys())

        self.create_second_window()
        self.create_third_window()
        self.create_fourth_window()
        self.create_fifth_window()
        self.create_sixth_window()

    def resize_image(self, event=None):
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        if width < 100 or height < 100:
            return
        resized = self.original_image.resize((width, height), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(resized)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_image)
        self.canvas.coords(self.result_window, width // 2, height // 3)
        self.canvas.coords(self.button_window, width // 2, height // 2)

    def roll_d20(self):
        current_player = self.player_order[self.turn_index]
        roll = random.randint(1, 20)
        encounter_text = self.encounters_list[roll - 1]
        self.result_label.config(text=f"{current_player}'s turn\nYou rolled a {roll}!\n{encounter_text}")
        self.turn_index = (self.turn_index + 1) % len(self.player_order)

    def create_second_window(self):
        self.second_window = tk.Toplevel(self.root)
        self.second_window.title("Roll a d10 Dice")
        self.second_window.geometry("300x150+1400+50")
        self.second_window.configure(bg="gray")

        self.d10_result_label = tk.Label(self.second_window, text="Press 'Roll Dice' to roll!", font=("Arial", 16), bg="gray", fg="white")
        self.d10_result_label.pack(pady=20)

        self.d10_roll_button = tk.Button(self.second_window, text="Roll Dice (1-10)", font=("Arial", 14), command=self.roll_d10)
        self.d10_roll_button.pack()

    def roll_d10(self):
        roll = random.randint(1, 10)
        self.d10_result_label.config(text=f"You rolled a {roll}!")

    def create_third_window(self):
        self.third_window = tk.Toplevel(self.root)
        self.third_window.title("Encounters List")
        self.third_window.geometry("400x600+1400+300")

        self.encounters_list = [
            "1: Nothing happens here as of right now",
            "2: Time-Warp Ruins. 1-5 nothing happens, 6-10 1 damage, 11-15 nothing happens, 16-20 heal 10",
            "3: You find a hidden passage leading to a secret room. 1-5 trap roll d10 for damage, 6-15 nothing, 16-20 treasure",
            "4: Skeleton Warrior Rise. HP: 5, Strength: 2, Defense: 0, Dexterity: 0",
            "5: Bandit Roadblock. 1-10 fight, 11-20 scare them off. HP: 10, Strength: 2, Defense: 1, Dexterity: 1",
            "6: Magical sword in stone. 1-19 fail, 20 win",
            "7: Dire Wolf. 1-9 attack, 10-17 flee, 18-20 drop herb. HP: 20, Strength: 3, Defense: 2, Dexterity: 3",
            "8: Wizard. 1-10 damage, 11-13 heal 2, 14-18 heal 6, 19-20 stat boost",
            "9: Trap! Roll D20 for damage",
            "10: Storm. 1-10 D10 damage, 11-20 safe",
            "11: Bard. 1-8 booed, 9-15 ok, 16-20 item",
            "12: Giant Spider. HP: 15, Strength: 3, Defense: 1, Dexterity: 3",
            "13: Goblin. HP: 5, Strength: 1, Defense: 1, Dexterity: 1",
            "14: Dragon breath. Roll D20 for damage",
            "15: Ancient ruin. 1-17 nothing, 18-20 treasure",
            "16: Mysterious potion. Roll D10 to heal",
            "17: Orc Ambush. HP: 30, Strength: 5, Defense: 3, Dexterity: 0",
            "18: Treasure chest. 1-15 ????, 16-20 treasure",
            "19: Lost child. 1-10 trap, 11-15 heal 2, 16-20 reward",
            "20: Church Caravan. 1-10 nothing, 2-15 heal D10, 16-20 item"
        ]

        self.text_area = scrolledtext.ScrolledText(self.third_window, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.insert(tk.END, "Possible Encounters:\n\n")
        for encounter in self.encounters_list:
            self.text_area.insert(tk.END, encounter + "\n\n")
        self.text_area.config(state=tk.DISABLED)

    def add_item_to_player(self):
        player = self.selected_player.get()
        selection = self.item_listbox.curselection()
        if not selection:
            return
        item = self.item_listbox.get(selection[0])
        self.players[player].setdefault("Inventory", []).append(item)
        self.update_inventory_display()

    def remove_item_from_player(self):
        player = self.selected_player.get()
        selection = self.item_listbox.curselection()
        if not selection:
            return
        item = self.item_listbox.get(selection[0])
        inventory = self.players[player].get("Inventory", [])
        if item in inventory:
            inventory.remove(item)
        self.update_inventory_display()


    def create_fourth_window(self):
        self.fourth_window = tk.Toplevel(self.root)
        self.fourth_window.title("Player Stats Editor")
        self.fourth_window.geometry("550x440+120+0")

        tk.Label(self.fourth_window, text="Edit Player Stats", font=("Arial", 16, "bold")).pack(pady=10)

        self.stat_vars = {}
        self.name_vars = {}

        for player in self.players:
            frame = tk.LabelFrame(self.fourth_window, text=player, padx=10, pady=10, font=("Arial", 12, "bold"))
            frame.pack(fill=tk.X, padx=15, pady=5)

        for player in self.players:
            frame = tk.LabelFrame(self.fourth_window, text=player, padx=10, pady=10, font=("Arial", 12, "bold"))
            frame.pack(fill=tk.X, padx=15, pady=5)

        self.name_vars[player] = tk.StringVar(value=player)
        tk.Label(frame, text="Name:", font=("Arial", 12)).pack(side=tk.LEFT)
        tk.Entry(frame, textvariable=self.name_vars[player], width=12, font=("Arial", 12)).pack(side=tk.LEFT, padx=(5, 15))

        self.stat_vars[player] = {}
        for stat in self.players[player]:
            if stat == "Inventory":
                continue
        tk.Label(frame, text=stat, font=("Arial", 12)).pack(side=tk.LEFT, padx=(0, 5))
        var = tk.StringVar(value=str(self.players[player][stat]))
        tk.Entry(frame, textvariable=var, width=5, font=("Arial", 12)).pack(side=tk.LEFT, padx=(0, 10))
        self.stat_vars[player][stat] = var
        tk.Entry(frame, textvariable=self.name_vars[player], width=12, font=("Arial", 12)).pack(side=tk.LEFT, padx=(5, 15))

        self.stat_vars[player] = {}
        for stat in self.players[player]:
            if stat == "Inventory":
                continue
            tk.Label(frame, text=stat, font=("Arial", 12)).pack(side=tk.LEFT, padx=(0, 5))
            var = tk.StringVar(value=str(self.players[player][stat]))
            tk.Entry(frame, textvariable=var, width=5, font=("Arial", 12)).pack(side=tk.LEFT, padx=(0, 10))
            self.stat_vars[player][stat] = var

        tk.Button(self.fourth_window, text="Save Stats", font=("Arial", 14), command=self.save_stats).pack(pady=15)
        self.save_msg = tk.Label(self.fourth_window, text="", font=("Arial", 12))
        self.save_msg.pack()

    def save_stats(self):
        new_players = {}
        new_order = []
        for old_name, stats in self.stat_vars.items():
            new_name = self.name_vars[old_name].get().strip()
        if not new_name:
            self.save_msg.config(text=f"Name for {old_name} cannot be empty.", fg="red")
            return
        if new_name in new_players:
            self.save_msg.config(text=f"Duplicate name: {new_name}", fg="red")
            return
        new_players[new_name] = self.players[old_name]
        for stat, var in stats.items():
            try:
                val = int(var.get())
                if val < 0:
                    raise ValueError
                new_players[new_name][stat] = val
            except ValueError:
                self.save_msg.config(text=f"Invalid value for {new_name} {stat}.", fg="red")
                return
        new_order.append(new_name)
        self.players = new_players
        self.player_order = new_order
        self.save_msg.config(text="Stats and names saved successfully!", fg="green")

    def create_sixth_window(self):
        self.sixth_window = tk.Toplevel(self.root)
        self.sixth_window.title("Combat Simulator")
        self.sixth_window.geometry("400x300+1250+100")

        tk.Label(self.sixth_window, text="Select Attacker", font=("Arial", 14)).pack(pady=5)
        self.attacker_var = tk.StringVar()
        attacker_menu = tk.OptionMenu(self.sixth_window, self.attacker_var, *self.players.keys())
        attacker_menu.pack()

        tk.Label(self.sixth_window, text="Select Defender", font=("Arial", 14)).pack(pady=5)
        self.defender_var = tk.StringVar()
        defender_menu = tk.OptionMenu(self.sixth_window, self.defender_var, *self.players.keys())
        defender_menu.pack()

        attack_btn = tk.Button(self.sixth_window, text="Simulate Attack", font=("Arial", 12), command=self.simulate_combat)
        attack_btn.pack(pady=10)

        self.combat_result = tk.Label(self.sixth_window, text="", font=("Arial", 12), wraplength=350, justify="left")
        self.combat_result.pack(pady=10)

        self.attacker_menu = tk.OptionMenu(self.sixth_window, self.attacker_var, *self.players.keys())
        self.attacker_menu.pack()
        self.defender_menu = tk.OptionMenu(self.sixth_window, self.defender_var, *self.players.keys())
        self.defender_menu.pack()

    def simulate_combat(self):
        attacker = self.attacker_var.get()
        defender = self.defender_var.get()
        if not attacker or not defender:
            self.combat_result.config(text="Please select both an attacker and a defender.")
            return
        if attacker == defender:
            self.combat_result.config(text="A player cannot attack themselves!")
            return

        atk_stats = self.players[attacker]
        def_stats = self.players[defender]
        attack_roll = random.randint(1, 20) + atk_stats.get("Strength", 0)
        defense_roll = random.randint(1, 20) + def_stats.get("Defense", 0)

        result = f"{attacker} attacks {defender}!\n"
        result += f"Attack roll: {attack_roll} vs Defense roll: {defense_roll}\n"
        if attack_roll > defense_roll:
            damage = max(1, attack_roll - defense_roll)
            def_stats["HP"] = max(0, def_stats["HP"] - damage)
            result += f"Hit! {defender} takes {damage} damage. HP is now {def_stats['HP']}.\n"
        else:
            result += f"Miss! {defender} takes no damage.\n"

        self.combat_result.config(text=result)


    def create_fifth_window(self):
        self.fifth_window = tk.Toplevel(self.root)
        self.fifth_window.title("Inventory Editor")
        self.fifth_window.geometry("600x500+100+500")

        tk.Label(self.fifth_window, text="Select Player", font=("Arial", 14)).pack(pady=5)

        self.selected_player = tk.StringVar(value=self.player_order[0])
        self.inventory_menu = tk.OptionMenu(self.fifth_window, self.selected_player, *self.players.keys(), command=self.update_inventory_display)
        self.inventory_menu.pack(pady=5)

        tk.Label(self.fifth_window, text="Available Items", font=("Arial", 14, "bold")).pack(pady=10)

        self.item_listbox = tk.Listbox(self.fifth_window, height=10, font=("Arial", 12))
        self.item_listbox.pack(padx=10, fill=tk.X)

        self.items = [
            ("Sword of Flames", "A blazing sword that adds +3 to attack rolls."),
            ("Magic Amulet of Dodging", "+3 to Dexterity."),
            ("Cloak of Speed", "Provides +1 to Dexterity."),
            ("Ring of Fortitude", "Increases HP by 5."),
            ("Boots of Swiftness", "Adds +2 to Dexterity."),
            ("Potion of Healing", "Restores 10 HP when consumed."),
            ("Scroll of Fireball", "Casts a fireball dealing 8 fire damage."),
            ("Shield of Protection", "One-time blocking of any damage."),
            ("Tome of Strength", "Permanently increases Strength by 1."),
            ("Scroll of Skipping", "Can skip any encounter once.")
        ]
        for item in self.items:
            self.item_listbox.insert(tk.END, item)

        tk.Button(self.fifth_window, text="Add Item", font=("Arial", 12), command=self.add_item_to_player).pack(pady=5)
        tk.Button(self.fifth_window, text="Remove Item", font=("Arial", 12), command=self.remove_item_from_player).pack(pady=5)
        self.inventory_display = tk.Label(self.fifth_window, text="", justify=tk.LEFT, font=("Arial", 12))
        self.inventory_display.pack(pady=20, padx=10, anchor="w")

        self.update_inventory_display()

    def add_item_to_player(self):
        player = self.selected_player.get()
        selection = self.item_listbox.curselection()
        if not selection:
            return
        item = self.item_listbox.get(selection[0])
        self.players[player].setdefault("Inventory", []).append(item)
        self.update_inventory_display()

    def remove_item_from_player(self):
        player = self.selected_player.get()
        selection = self.item_listbox.curselection()
        if not selection:
            return
        item = self.item_listbox.get(selection[0])
        inventory = self.players[player].get("Inventory", [])
        if item in inventory:
            inventory.remove(item)
        self.update_inventory_display()

    def update_inventory_display(self, *args):
        player = self.selected_player.get()
        inventory = self.players[player].get("Inventory", [])
        if inventory:
            inv_text = "Inventory:\n" + "\n".join(f"- {i}" for i in inventory)
        else:
            inv_text = "Inventory:\n(empty)"
        self.inventory_display.config(text=inv_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300+700+50")
    root.minsize(400, 300)
    app = DiceApp(root, "RPG BOARD.png")
    root.mainloop()

