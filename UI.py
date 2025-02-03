from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

class Game:
    def __init__(self, genre, dimension):
        self.givenGenre = genre
        self.givenDimension = dimension

    def show_developer(self):
        if self.givenDimension == "2D" and self.givenGenre == "Platformer":
            messagebox.showinfo("info", "505")
        elif self.givenDimension == "3D" and self.givenGenre == "Survival":
            messagebox.showinfo("info", "Santa")
        else:
            messagebox.showwarning("info", "Unknown")

class UI():
    def __init__(self):
        self.root = tk.Tk()  # Initialize the root window
        self.root.geometry("300x300")
        self.checkDeveloper = tk.Button(self.root, text="Check Developer")
        self.checkDeveloper.place(x=100,y=200)

        # Create combo boxes as instance variables so they can be accessed by other methods
        self.comboGenre = ttk.Combobox(
            state="readonly",
            values=["Survival", "Platformer", "Other"]
        )
        self.comboDim = ttk.Combobox(
            state="readonly",
            values=["2D", "3D"]
        )

        self.comboDim.place(x=100, y=100)
        self.comboGenre.place(x=100, y=50)

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
