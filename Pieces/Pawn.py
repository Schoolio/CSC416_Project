__author__ = 'Zac'

class Pawn:
    def __init__(self, location, isWhite):
        self.name = "Pawn"
        self.canDoubleMove = True
        self.value = 1
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True:
            self.image = "bin/Pawn_W.png"
        else:
            self.image = "bin/Pawn_B.png"