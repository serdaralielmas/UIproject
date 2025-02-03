from tkinter import ttk

import tkinter as tk
from Functions import Game

class UI:
    def __init__(self):
        self.root = tk.Tk()  # Initialize the root window
        self.root.geometry("300x300")
        self.checkDeveloper = tk.Button(self.root, text="Check Developer")


        # Create combo boxes as instance variables so they can be accessed by other methods

        self.comboGenre = ttk.Combobox(
            state="readonly",
            values=["Survival", "Platformer", "Other"]
        )
        self.comboGenre.set("Select an option")

        self.comboDim = ttk.Combobox(

            state="readonly",
            values=["2D", "3D"]
        )
        self.comboDim.set("Select an option")
        self.comboGenre.pack(pady=10)
        self.comboDim.pack(pady=10)
        self.checkDeveloper.pack(pady=20)


        # Set up button
        self.button_funcs()

    def show_developer_click(self):
        # Get the selected values from combo boxes
        genre = self.comboGenre.get()
        dim = self.comboDim.get()

        # Create Game object and show the developer
        game = Game(genre, dim)
        game.show_developer()

    def button_funcs(self):

        self.checkDeveloper.config(command=self.show_developer_click)

    def run(self):
        # Start the Tkinter event loop
        self.root.mainloop()

# Run the UI
runner = UI()
runner.run()

#Test message
#DogusFirstCommit
