import tkinter as tk

class StatsEditorWindow:
    def __init__(self, root, players):
        self.players = players
        self.window = tk.Toplevel(root)
        self.window.title("Player Stats Editor")
        self.window.geometry("550x440+120+0")

        tk.Label(self.window, text="Edit Player Stats", font=("Arial", 16, "bold")).pack(pady=10)

        self.stat_vars = {}

        for player in self.players:
            frame = tk.LabelFrame(self.window, text=player, padx=10, pady=10, font=("Arial", 12, "bold"))
            frame.pack(fill=tk.X, padx=15, pady=5)

            self.stat_vars[player] = {}

            for stat in self.players[player]:
                stat_label = tk.Label(frame, text=stat, font=("Arial", 12))
                stat_label.pack(side=tk.LEFT, padx=(0,5))

                var = tk.StringVar(value=str(self.players[player][stat]))
                entry = tk.Entry(frame, textvariable=var, width=5, font=("Arial", 12))
                entry.pack(side=tk.LEFT, padx=(0,10))

                self.stat_vars[player][stat] = var

        save_btn = tk.Button(self.window, text="Save Stats", font=("Arial", 14), command=self.save_stats)
        save_btn.pack(pady=15)

        self.save_msg = tk.Label(self.window, text="", font=("Arial", 12))
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
