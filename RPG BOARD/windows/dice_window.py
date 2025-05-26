import tkinter as tk
import random

class DiceWindow:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Dice Roller")
        self.label = tk.Label(self.window, text="Roll a Dice", font=("Arial", 14))
        self.label.pack(pady=10)
        self.button = tk.Button(self.window, text="Roll", command=self.roll_dice)
        self.button.pack(pady=10)

    def roll_dice(self):
        roll = random.randint(1, 6)
        self.label.config(text=f"Rolled: {roll}")