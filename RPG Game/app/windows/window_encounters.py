import tkinter as tk
from tkinter import scrolledtext

def create(app):
    app.third_window = tk.Toplevel(app.root)
    app.third_window.title("Encounters List")
    app.third_window.geometry("400x600+1400+300")

    text_area = scrolledtext.ScrolledText(app.third_window, wrap=tk.WORD, font=("Arial", 12))
    text_area.pack(fill=tk.BOTH, expand=True)
    text_area.insert(tk.END, "Possible Encounters:\n\n")
    for encounter in app.encounters_list:
        text_area.insert(tk.END, encounter + "\n\n")
    text_area.config(state=tk.DISABLED)