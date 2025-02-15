
class GameLibrary:
    def __init__(self):
        self.deadCells = {
            "name": ["Dead Cells"],
            "genre": ["Rogue-like", "Platformer"],
            "dimension": ["2D"],
            "art-style": ["Pixel-Art"]
        }

        self.godOfWar = {
            "name": ["God of War"],
            "genre": ["Action", "Open-world", "Adventure"],
            "dimension": ["3D"],
            "art-style": ["Realistic"]
        }

        self.devilMayCry = {
            "name": ["Devil May Cry"],
            "genre": ["Action", "Hack-n-Slash"],
            "dimension": ["3D"],
            "art-style": ["Stylistic"]
        }

        self.dontStarveTogether = {
            "name": ["Don't Starve Together"],
            "genre": ["Survival", "Sandbox"],
            "dimension": ["2D"],
            "art-style": ["Stylistic"]
        }

        self.celeste = {
            "name": ["Celeste"],
            "genre": ["Platformer", "Adventure"],
            "dimension": ["2D"],
            "art-style": ["Pixel-Art"]
        }

        self.gameLibrary = [
            self.deadCells,
            self.godOfWar,
            self.devilMayCry,
            self.dontStarveTogether,
            self.celeste
        ]
