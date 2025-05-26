import tkinter as tk

class InventoryWindow:
    def __init__(self, root, players):
        self.root = root
        self.players = players
        self.window = tk.Toplevel(self.root)
        self.window.title("Inventory Editor")
        self.window.geometry("600x500+100+500")

        tk.Label(self.window, text="Select Player", font=("Arial", 14)).pack(pady=5)

        self.selected_player = tk.StringVar(value=list(self.players.keys())[0])
        player_menu = tk.OptionMenu(self.window, self.selected_player, *self.players.keys(), command=self.update_inventory_display)
        player_menu.pack(pady=5)

        tk.Label(self.window, text="Available Items", font=("Arial", 14, "bold")).pack(pady=10)

        self.item_listbox = tk.Listbox(self.window, height=10, font=("Arial", 12))
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

        # Insert only item names into the listbox for clarity
        for item in self.items:
            self.item_listbox.insert(tk.END, item[0])

        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="Add Item", command=self.add_item_to_player, font=("Arial", 12))
        add_btn.grid(row=0, column=0, padx=10)

        remove_btn = tk.Button(btn_frame, text="Remove Item", command=self.remove_item_from_player, font=("Arial", 12))
        remove_btn.grid(row=0, column=1, padx=10)

        self.inventory_display = tk.Label(self.window, text="", justify=tk.LEFT, font=("Arial", 12))
        self.inventory_display.pack(pady=20, padx=10, anchor="w")

        self.update_inventory_display()

    def add_item_to_player(self):
        player = self.selected_player.get()
        selection = self.item_listbox.curselection()
        if not selection:
            return
        item_name = self.item_listbox.get(selection[0])
        self.players[player].setdefault("Inventory", []).append(item_name)
        self.update_inventory_display()

    def remove_item_from_player(self):
        player = self.selected_player.get()
        selection = self.item_listbox.curselection()
        if not selection:
            return
        item_name = self.item_listbox.get(selection[0])
        inventory = self.players[player].get("Inventory", [])
        if item_name in inventory:
            inventory.remove(item_name)
        self.update_inventory_display()

    def update_inventory_display(self, *args):
        player = self.selected_player.get()
        inventory = self.players[player].get("Inventory", [])
        if inventory:
            inv_text = "Inventory:\n" + "\n".join(f"- {i}" for i in inventory)
        else:
            inv_text = "Inventory:\n(empty)"
        self.inventory_display.config(text=inv_text)
