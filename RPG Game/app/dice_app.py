import tkinter as tk
import random
from PIL import Image, ImageTk
from app.encounters import ENCOUNTERS
from app.windows import (
    window_d10,
    window_encounters,
    window_stats,
    window_inventory,
    window_combat
)

class DiceApp:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Roll a d20 Dice")
        self.original_image = Image.open(image_path)
        self.canvas = tk.Canvas(root, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.root.bind("<Configure>", self.resize_image)

        self.result_label = tk.Label(root, text="Press 'Roll Dice' to roll!", font=("Arial", 18), bg="#ffffff")
        self.roll_button = tk.Button(root, text="Roll Dice (1-20)", font=("Arial", 16), padx=20, pady=10, command=self.roll_d20)

        self.result_window = self.canvas.create_window(0, 0, anchor="n", window=self.result_label)
        self.button_window = self.canvas.create_window(0, 0, anchor="n", window=self.roll_button)
        self.bg_image = None

        self.players = {
            f"Player {i}": {"HP": 20, "Strength": 2, "Defense": 1, "Dexterity": 1}
            for i in range(1, 6)
        }
        self.turn_index = 0
        self.player_order = list(self.players.keys())
        self.encounters_list = ENCOUNTERS

        self.resize_image()

        # Load all modular windows
        window_d10.create(self)
        window_encounters.create(self)
        window_stats.create(self)
        window_inventory.create(self)
        window_combat.create(self)

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
