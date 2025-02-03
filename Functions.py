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