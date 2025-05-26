import random
import tkinter as tk
from PIL import Image, ImageTk

from windows.d10_window import D10Window
from windows.encounter_window import EncounterWindow
from windows.stats_editor_window import StatsEditorWindow
from windows.inventory_window import InventoryWindow
from windows.combat_simulator_window import CombatSimulatorWindow

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

        # Create the other windows by instantiating their classes
        self.d10_window = D10Window(self.root)
        self.encounter_window = EncounterWindow(self.root)
        self.stats_editor_window = StatsEditorWindow(self.root, self.players)
        self.inventory_window = InventoryWindow(self.root, self.players)
        self.combat_simulator_window = CombatSimulatorWindow(self.root, self.players)

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
