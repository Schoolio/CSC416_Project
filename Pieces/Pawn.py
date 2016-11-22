__author__ = 'Zac'

class Pawn:
    def __init__(self, location):
        self.name = "Pawn"
        self.canDoubleMove = True
        self.value = 1
        self.location = location
        self.image = "bin/Pawn_W.png"