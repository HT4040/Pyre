import random
import tkinter as tk

class D10Window:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Roll a d10 Dice")
        self.window.geometry("300x150+1400+50")
        self.window.configure(bg="gray") 

        self.d10_result_label = tk.Label(self.window, text="Press 'Roll Dice' to roll!", 
                                        font=("Arial", 16), bg="gray", fg="white")
        self.d10_result_label.pack(pady=20)

        self.d10_roll_button = tk.Button(self.window, text="Roll Dice (1-10)", font=("Arial", 14),
                                        command=self.roll_d10)
        self.d10_roll_button.pack()

    def roll_d10(self):
        roll = random.randint(1, 10)
        self.d10_result_label.config(text=f"You rolled a {roll}!")
