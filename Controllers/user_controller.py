from UIproject.Views.user_view import UserView
from  UIproject.Static.dictionary import GameLibrary
from tkinter import messagebox

class UserController:
    def __init__(self,root):
        self.view = UserView(root)
        self.view.filterBtn.config(command=self.filter_games)

    def filter_games(self):

        genre = self.view.comboGenre.get()
        dimension = self.view.comboDim.get()
        art_style = self.view.comboArt.get()

        filtered_games = []
        get_library = GameLibrary()
        proxy_library = get_library.gameLibrary

        for game in proxy_library:
            for key,value in game:
                print(value)

        for game in proxy_library:
            if (genre in game["genre"] or genre == "None" or genre == "") and \
                    (dimension in game["dimension"] or dimension == "None" or dimension == "") and \
                    (art_style in game["art-style"] or art_style == "None" or art_style == ""):
                filtered_games.append(game["name"])

        matching_games = filtered_games
        if len(matching_games) > 1:
            messagebox.showinfo("Matching Games",str(matching_games))
        else:
            messagebox.showinfo("Matching Games","No games found")
