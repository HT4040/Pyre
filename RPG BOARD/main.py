import tkinter as tk
from app import DiceApp

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300+700+50")
    root.minsize(400, 300)
    app = DiceApp(root, "assets/RPG BOARD.png")
    root.mainloop()
