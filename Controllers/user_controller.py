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

        get_library = GameLibrary()
        proxy_library = get_library.gameLibrary

        categories = []
        matching_games = []
        categories = [genre,dimension,art_style]
        i = 0
        y = 0
        if genre != "None": y += 1
        if dimension != "None": y += 1
        if art_style != "None": y += 1

        for game in proxy_library:
            i = 0
            for key, value in game.items():
                for x in value:
                    if x in categories:
                        i += 1
                    if i == y:
                        if game["name"][0] not in matching_games:
                            matching_games.append(game["name"][0])

        if len(matching_games) > 0:
            messagebox.showinfo("Matching Games",str(matching_games))
        else:
            messagebox.showinfo("Matching Games","No games found")

