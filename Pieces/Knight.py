__author__ = 'Zac', 'Shawyn Kane'
import Pieces


class Knight:
    def __init__(self, location, isWhite):
        self.name = "Knight"
        self.value = 3
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True: self.image = "bin/Knight_W.png"
        else: self.image = "bin/Knight_B.png"

    def get_valid_moves(self):
        pass

    def move(self):  # TODO Write move() function for Knight
        pass

    def attack(self):  # TODO Write attack() function for Knight
        pass