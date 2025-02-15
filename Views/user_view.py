import tkinter as tk
from tkinter import ttk


class UserView:
    def __init__(self,root):

        self.root = root
        self.root.geometry("300x300")

        self.filterBtn = tk.Button(root, text="Filter")


        #Comboboxes
        self.comboGenre = ttk.Combobox( root,
            state= "readonly",
            values=["Survival", "Platformer", "Hack-n-Slash", "Open-world","Adventure","Rogue-like","Action","Sandbox","None"]
        )
        self.comboDim = ttk.Combobox( root,

            state= "readonly",
            values=["2D", "3D","None"]
        )
        self.comboArt = ttk.Combobox(
            state= "readonly",
            values=["Pixel-Art","Realistic","Stylistic","None"]
        )

        self.comboDim.set("Select a Dimension")
        self.comboGenre.set("Select a Genre")
        self.comboArt.set("Select an Art-style")

        self.comboGenre.pack(pady=20)
        self.comboDim.pack(pady=0)
        self.comboArt.pack(pady=20)
        self.filterBtn.pack(pady=20)
