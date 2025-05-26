import tkinter as tk
from tkinter import scrolledtext

class EncounterWindow:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Encounters List")
        self.window.geometry("400x600+1400+300")

       
        encounters = [
            "1: Nothing happens here",
            "2: Time-Warp Ruins. 1-5 nothing happens, 6-10 1 damage, 11-15 nothing happens, 16-20 heal 10",
            "3: You find a hidden passage leading to a secret room. 1-5 trap roll d10 for the damage taken, 6-15 you find nothing, 16-20 you find treasure",
            "4: Skeleton Warrior Rise. HP: 5, Strength: 2, Defense: 0, Dexterity: 0",
            "5: Bandit Roadblock. 1-10 fight, 11-20 you scare them off, HP: 10, Strength: 2, Defense: 1, Dexterity: 1",
            "6: You find a magical sword stuck in a stone.1-19 you don't pull it out, 20 you win",
            "7: Dire Wolf Stalks You. 1-9 it attacks, 10-17 it flees, 18-20, it flees dropping a herb that heals you 2 hp, HP: 20, Strength: 3, Defense: 2, Dexterity: 3",
            "8: You encounter a wizard who offers to help. 1-10 roll d10 to see how much damage you take, 11-13 heal 2, 14-18 heal 6, 19-20 random stat increase",
            "9: You fall into a hidden trap! Roll D20 to see how much damage you take.",
            "10: A sudden storm forces you to take shelter. 1-10 roll d10 to see how much damage you take for not making it, 11-20, you make it to shelter",
            "11: Traveling Bard Challenge. Roll Performance (D20): 1-8 booed and get rocks thrown at you, lose 1 hp, 9-15 solid, 16-20 crowd loves you, get a random item.",
            "12: Giant Spider Encounter! HP: 15, Strength: 3, Defense: 1, Dexterity: 3",
            "13: A wild goblin attacks! HP: 5, Strength: 1, Defense: 1, Dexterity: 1",
            "14: You run into a dragon blowing its breath. Roll D20 to see how much damage you take",
            "15: You stumble upon an ancient ruin filled with secrets.1-17 you find nothing, 18-20 you find treasure",
            "16: You find a mysterious potion. Drink it? Roll D10 to see how much you heal.",
            "17: Orc Ambush! HP: 30, Strength: 5, Defense: 3, Dexterity: 0",
            "18: You discover a treasure chest. Open it carefully. 1-15 = ?????, 16-20 = Treasure.",
            "19: Lost Child in the Forest. Roll D20: 1-10 illusion trap roll d10 for damage, 11-15 you guide the child home and heal 2, 16-20 rewarded.",   
            "20: Church Caravan. 1-10 nothing happens, 1 you are a heratic and must fight the paladin HP: 25, Strength: 3, Defense: 2, Dexterity: 2 , 2-15 heal d10, 16-20, get an item."
        ]

        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.text_area.insert(tk.END, "Possible Encounters:\n\n")
        for encounter in encounters:
            self.text_area.insert(tk.END, encounter + "\n\n")

        self.text_area.config(state=tk.DISABLED)
