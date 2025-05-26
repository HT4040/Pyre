import tkinter as tk
import random

def create(app):
    app.second_window = tk.Toplevel(app.root)
    app.second_window.title("Roll a d10 Dice")
    app.second_window.geometry("300x150+1400+50")
    app.second_window.configure(bg="gray")

    app.d10_result_label = tk.Label(app.second_window, text="Press 'Roll Dice' to roll!", font=("Arial", 16), bg="gray", fg="white")
    app.d10_result_label.pack(pady=20)

    def roll_d10():
        roll = random.randint(1, 10)
        app.d10_result_label.config(text=f"You rolled a {roll}!")

    app.d10_roll_button = tk.Button(app.second_window, text="Roll Dice (1-10)", font=("Arial", 14), command=roll_d10)
    app.d10_roll_button.pack()