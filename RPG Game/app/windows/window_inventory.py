import tkinter as tk

def create(app):
    app.fifth_window = tk.Toplevel(app.root)
    app.fifth_window.title("Inventory Editor")
    app.fifth_window.geometry("600x500+100+500")

    tk.Label(app.fifth_window, text="Select Player", font=("Arial", 14)).pack(pady=5)

    app.selected_player = tk.StringVar(value=app.player_order[0])
    app.inventory_menu = tk.OptionMenu(app.fifth_window, app.selected_player, *app.players.keys(), command=lambda _: update_inventory_display())
    app.inventory_menu.pack(pady=5)

    tk.Label(app.fifth_window, text="Available Items", font=("Arial", 14, "bold")).pack(pady=10)

    app.item_listbox = tk.Listbox(app.fifth_window, height=10, font=("Arial", 12))
    app.item_listbox.pack(padx=10, fill=tk.X)

    app.items = [
        "Sword of Flames",
        "Magic Amulet of Dodging",
        "Cloak of Speed",
        "Ring of Fortitude",
        "Boots of Swiftness",
        "Potion of Healing",
        "Scroll of Fireball",
        "Shield of Protection",
        "Tome of Strength",
        "Scroll of Skipping"
    ]
    for item in app.items:
        app.item_listbox.insert(tk.END, item)

    def add_item():
        player = app.selected_player.get()
        selection = app.item_listbox.curselection()
        if not selection:
            return
        item = app.item_listbox.get(selection[0])
        app.players[player].setdefault("Inventory", []).append(item)
        update_inventory_display()

    def remove_item():
        player = app.selected_player.get()
        selection = app.item_listbox.curselection()
        if not selection:
            return
        item = app.item_listbox.get(selection[0])
        inventory = app.players[player].get("Inventory", [])
        if item in inventory:
            inventory.remove(item)
        update_inventory_display()

    def update_inventory_display():
        player = app.selected_player.get()
        inventory = app.players[player].get("Inventory", [])
        inv_text = "Inventory:\n" + "\n".join(f"- {i}" for i in inventory) if inventory else "Inventory:\n(empty)"
        app.inventory_display.config(text=inv_text)

    tk.Button(app.fifth_window, text="Add Item", font=("Arial", 12), command=add_item).pack(pady=5)
    tk.Button(app.fifth_window, text="Remove Item", font=("Arial", 12), command=remove_item).pack(pady=5)

    app.inventory_display = tk.Label(app.fifth_window, text="", justify=tk.LEFT, font=("Arial", 12))
    app.inventory_display.pack(pady=20, padx=10, anchor="w")

    update_inventory_display()