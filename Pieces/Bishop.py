__author__ = 'Zac, Shawyn Kane'
import Pieces


class Bishop:
    def __init__(self, location, isWhite):
        self.name = "Bishop"
        self.value = 3
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True: self.image = "bin/Bishop_W.png"
        else: self.image = "bin/Bishop_B.png"

    def move(self):  # TODO Write move() function for Bishop
        pass


    def attack(self):  # TODO Write attack() function for Bishop
        pass