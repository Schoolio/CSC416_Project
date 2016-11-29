__author__ = 'Zac, Shawyn Kane'
import Pieces


class King:
    def __init__(self, location, isWhite):
        self.name = "King"
        self.value = 100
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True: self.image = "bin/King_W.png"
        else: self.image = "bin/King_B.png"

    def get_valid_moves(self, pieces, selectedPiece):
        pass

    def move(self):  # TODO Write move() function for King
        pass

    def attack(self):  # TODO Write attack() function for King
        pass