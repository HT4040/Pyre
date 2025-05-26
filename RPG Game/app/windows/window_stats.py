import tkinter as tk

def create(app):
    app.fourth_window = tk.Toplevel(app.root)
    app.fourth_window.title("Player Stats Editor")
    app.fourth_window.geometry("550x440+120+0")

    tk.Label(app.fourth_window, text="Edit Player Stats", font=("Arial", 16, "bold")).pack(pady=10)

    app.stat_vars = {}
    app.name_vars = {}

    for player in app.players:
        frame = tk.LabelFrame(app.fourth_window, text=player, padx=10, pady=10, font=("Arial", 12, "bold"))
        frame.pack(fill=tk.X, padx=15, pady=5)

        app.name_vars[player] = tk.StringVar(value=player)
        tk.Label(frame, text="Name:", font=("Arial", 12)).pack(side=tk.LEFT)
        tk.Entry(frame, textvariable=app.name_vars[player], width=12, font=("Arial", 12)).pack(side=tk.LEFT, padx=(5, 15))

        app.stat_vars[player] = {}
        for stat in app.players[player]:
            if stat == "Inventory":
                continue
            tk.Label(frame, text=stat, font=("Arial", 12)).pack(side=tk.LEFT, padx=(0, 5))
            var = tk.StringVar(value=str(app.players[player][stat]))
            tk.Entry(frame, textvariable=var, width=5, font=("Arial", 12)).pack(side=tk.LEFT, padx=(0, 10))
            app.stat_vars[player][stat] = var

    def save_stats():
        new_players = {}
        new_order = []
        for old_name, stats in app.stat_vars.items():
            new_name = app.name_vars[old_name].get().strip()
            if not new_name:
                app.save_msg.config(text=f"Name for {old_name} cannot be empty.", fg="red")
                return
            if new_name in new_players:
                app.save_msg.config(text=f"Duplicate name: {new_name}", fg="red")
                return
            new_players[new_name] = app.players[old_name]
            for stat, var in stats.items():
                try:
                    val = int(var.get())
                    if val < 0:
                        raise ValueError
                    new_players[new_name][stat] = val
                except ValueError:
                    app.save_msg.config(text=f"Invalid value for {new_name} {stat}.", fg="red")
                    return
            new_order.append(new_name)
        app.players = new_players
        app.player_order = new_order
        app.save_msg.config(text="Stats and names saved successfully!", fg="green")

    tk.Button(app.fourth_window, text="Save Stats", font=("Arial", 14), command=save_stats).pack(pady=15)
    app.save_msg = tk.Label(app.fourth_window, text="", font=("Arial", 12))
    app.save_msg.pack()