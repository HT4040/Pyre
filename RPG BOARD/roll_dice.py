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

        self.result_label = tk.Label(root, text="Press 'Roll Dice' to roll!", 
                                     font=("Arial", 18), bg="#ffffff", fg="#000000")
        self.roll_button = tk.Button(root, text="Roll Dice (1-20)", font=("Arial", 16), padx=20, pady=10,
                                     command=self.roll_d20)

        self.result_window = self.canvas.create_window(0, 0, anchor="n", window=self.result_label)
        self.button_window = self.canvas.create_window(0, 0, anchor="n", window=self.roll_button)
        self.bg_image = None

        self.resize_image()

        self.players = {
            f"Player {i}": {"HP": 20, "Strength": 2, "Defense": 1,"Dexterity":1}
            for i in range(1, 6)
            
        }

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
        roll = random.randint(1, 20)
        self.result_label.config(text=f"You rolled a {roll}!")

    def create_second_window(self):
        self.second_window = tk.Toplevel(self.root)
        self.second_window.title("Roll a d10 Dice")
        self.second_window.geometry("300x150+1400+50")
        self.second_window.configure(bg="gray") 

        self.d10_result_label = tk.Label(self.second_window, text="Press 'Roll Dice' to roll!", 
                                        font=("Arial", 16), bg="gray", fg="white")
        self.d10_result_label.pack(pady=20)

        self.d10_roll_button = tk.Button(self.second_window, text="Roll Dice (1-10)", font=("Arial", 14),
                                        command=self.roll_d10)
        self.d10_roll_button.pack()

    def roll_d10(self):
        roll = random.randint(1, 10)
        self.d10_result_label.config(text=f"You rolled a {roll}!")

    def create_third_window(self):
        self.third_window = tk.Toplevel(self.root)
        self.third_window.title("Encounters List")
        self.third_window.geometry("400x600+1400+300")

        encounters = [
            "1: Nothing happens here",
            "2: Time-Warp Ruins. 1-5 nothing happens, 6-10 1 damage, 11-15 nothing happens, 16-20 heal 10",
            "3: You find a hidden passage leading to a secret room. 1-5 trap roll d10 for the damage taken, 6-15 you find nothing, 16-20 you find treasure",
            "4: Skeleton Warrior Rise. HP: 5, Strength: 2, Defense: 0, Dexterity: 0",
            "5: Bandit Roadblock. 1-10 fight, 11-20 you scare them off, HP: 10, Strength: 2, Defense: 1, Dexterity: 1",
            "6: You find a magical sword stuck in a stone.1-19 you don't pull it out, 20 you win",
            "7: Dire Wolf Stalks You. 1-9 it attacks, 10-17 it flees, 18-20, it flees dropping a herb that heals you 2 hp, HP: 20, Strength: 3, Defense: 2, Dexterity: 3",
            "8: You encounter a wizard who offers to help. 1-10 roll d10 to see how much damage you take, 11-13 heal 2, 14-18 heal 6, 19-20 random stat increase",
            "9: You fall into a hidden trap! Roll D20 to see how much damage you take.",
            "10: A sudden storm forces you to take shelter. 1-10 roll d10 to see how much damage you take for not making it, 11-20, you make it to shelter",
            "11: Traveling Bard Challenge. Roll Performance (D20): 1-8 booed and get rocks thrown at you, lose 1 hp, 9-15 solid, 16-20 crowd loves you, get a random item.",
            "12: Giant Spider Encounter! HP: 15, Strength: 3, Defense: 1, Dexterity: 3",
            "13: A wild goblin attacks! HP: 5, Strength: 1, Defense: 1, Dexterity: 1",
            "14: You run into a dragon blowing its breath. Roll D20 to see how much damage you take",
            "15: You stumble upon an ancient ruin filled with secrets.1-17 you find nothing, 18-20 you find treasure",
            "16: You find a mysterious potion. Drink it? Roll D10 to see how much you heal.",
            "17: Orc Ambush! HP: 30, Strength: 5, Defense: 3, Dexterity: 0",
            "18: You discover a treasure chest. Open it carefully. 1-15 = ?????, 16-20 = Treasure.",
            "19: Lost Child in the Forest. Roll D20: 1-10 illusion trap roll d10 for damage, 11-15 you guide the child home and heal 2, 16-20 rewarded.",   
            "20: Church Caravan. 1-10 nothing happens, 1 you are a heratic and must fight the paladin HP: 25, Strength: 3, Defense: 2, Dexterity: 2 , 2-15 heal d10, 16-20, get an item."
        ]

        self.text_area = scrolledtext.ScrolledText(self.third_window, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.text_area.insert(tk.END, "Possible Encounters:\n\n")
        for encounter in encounters:
            self.text_area.insert(tk.END, encounter + "\n\n")

        self.text_area.config(state=tk.DISABLED)

    def create_fourth_window(self):
        self.fourth_window = tk.Toplevel(self.root)
        self.fourth_window.title("Player Stats Editor")
        self.fourth_window.geometry("550x440+120+0")

        tk.Label(self.fourth_window, text="Edit Player Stats", font=("Arial", 16, "bold")).pack(pady=10)

        self.stat_vars = {}

        for player in self.players:
            frame = tk.LabelFrame(self.fourth_window, text=player, padx=10, pady=10, font=("Arial", 12, "bold"))
            frame.pack(fill=tk.X, padx=15, pady=5)

            self.stat_vars[player] = {}

            for stat in self.players[player]:
                stat_label = tk.Label(frame, text=stat, font=("Arial", 12))
                stat_label.pack(side=tk.LEFT, padx=(0,5))

                var = tk.StringVar(value=str(self.players[player][stat]))
                entry = tk.Entry(frame, textvariable=var, width=5, font=("Arial", 12))
                entry.pack(side=tk.LEFT, padx=(0,10))

                self.stat_vars[player][stat] = var

        save_btn = tk.Button(self.fourth_window, text="Save Stats", font=("Arial", 14), command=self.save_stats)
        save_btn.pack(pady=15)

        self.save_msg = tk.Label(self.fourth_window, text="", font=("Arial", 12))
        self.save_msg.pack()

    def save_stats(self):
        for player, stats in self.stat_vars.items():
            for stat, var in stats.items():
                try:
                    val = int(var.get())
                    if val < 0:
                        raise ValueError
                    self.players[player][stat] = val
                except ValueError:
                    self.save_msg.config(text=f"Invalid value for {player} {stat}. Please enter a positive integer.", fg="red")
                    return
        self.save_msg.config(text="Stats saved successfully!", fg="green")

    def create_fifth_window(self):
        self.fifth_window = tk.Toplevel(self.root)
        self.fifth_window.title("Inventory Editor")
        self.fifth_window.geometry("600x500+100+500")

        tk.Label(self.fifth_window, text="Select Player", font=("Arial", 14)).pack(pady=5)

        self.selected_player = tk.StringVar(value="Player 1")
        player_menu = tk.OptionMenu(self.fifth_window, self.selected_player, *self.players.keys(), command=self.update_inventory_display)
        player_menu.pack(pady=5)

        tk.Label(self.fifth_window, text="Available Items", font=("Arial", 14, "bold")).pack(pady=10)

        self.item_listbox = tk.Listbox(self.fifth_window, height=10, font=("Arial", 12))
        self.item_listbox.pack(padx=10, fill=tk.X)
        self.items = [
    ("Sword of Flames", "A blazing sword that adds +3 to attack rolls."),
    ("Magic Amulet of Dodging", "+3 to Dexterity."),
    ("Cloak of speed", "Provides +1 to Dexterity."),
    ("Ring of Fortitude", "Increases HP by 5."),
    ("Boots of Swiftness", "Adds +2 to Dexterity."),
    ("Potion of Healing", "Restores 10 HP when consumed."),
    ("Scroll of Fireball", "Casts a fireball dealing 8 fire damage."),
    ("Shield of Protection", "One time blocking of any damage."),
    ("Tome of Strength", "Permanently increases Strength by 1."),
    ("Scroll of Skipping", "Can skip any encounter once."),
        ]
        for item in self.items:
            self.item_listbox.insert(tk.END, item)

        btn_frame = tk.Frame(self.fifth_window)
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="Add Item", command=self.add_item_to_player, font=("Arial", 12))
        add_btn.grid(row=0, column=0, padx=10)

        remove_btn = tk.Button(btn_frame, text="Remove Item", command=self.remove_item_from_player, font=("Arial", 12))
        remove_btn.grid(row=0, column=1, padx=10)

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

    def create_sixth_window(self):
        self.sixth_window = tk.Toplevel(self.root)
        self.sixth_window.title("Combat Simulator")
        self.sixth_window.geometry("600x550+710+400")

        tk.Label(self.sixth_window, text="Attacker:").pack()
        self.attacker_var = tk.StringVar(value="Player 1")
        attacker_menu = tk.OptionMenu(self.sixth_window, self.attacker_var, *self.players.keys())
        attacker_menu.pack()

        tk.Label(self.sixth_window, text="Defender:").pack()
        self.defender_var = tk.StringVar(value="Player 2")
        defender_menu = tk.OptionMenu(self.sixth_window, self.defender_var, *self.players.keys())
        defender_menu.pack()

    
        self.hp_bars = {}
        for player in self.players:
            tk.Label(self.sixth_window, text=f"{player} HP").pack(pady=(10, 0))
            hp_var = tk.IntVar(value=self.players[player]["HP"])
            bar = ttk.Progressbar(self.sixth_window, maximum=100, length=300, variable=hp_var)
            bar.pack()
            self.hp_bars[player] = hp_var

        self.combat_log = scrolledtext.ScrolledText(self.sixth_window, wrap=tk.WORD, height=10, font=("Arial", 11))
        self.combat_log.pack(pady=10, fill=tk.BOTH, expand=True)

        simulate_btn = tk.Button(self.sixth_window, text="Simulate Turn", command=self.simulate_combat)
        simulate_btn.pack(pady=10)

        self.update_hp_bars()  


    def simulate_combat(self):  
        attacker = self.attacker_var.get()
        defender = self.defender_var.get()

        if attacker == defender:
            self.combat_log.insert(tk.END, "A player can't fight themselves!\n\n")
            return

        atk_stats = self.players[attacker]
        def_stats = self.players[defender]

        def attack_turn(attacker_name, attacker_stats, defender_name, defender_stats):
            roll = random.randint(1, 20)
            log = f"{attacker_name} rolls a {roll} against {defender_name}...\n"

            if roll >= 10:
                damage = max(attacker_stats["Strength"] - defender_stats["Defense"], 0)
                defender_stats["HP"] = max(defender_stats["HP"] - damage, 0)
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
            hp = self.players[player]["HP"]
            self.hp_bars[player].set(hp)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300+700+50")
    root.minsize(400, 300)
    app = DiceApp(root, "RPG BOARD.png")  
    root.mainloop()
