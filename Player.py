__author__ = 'Zac'
import Piece

class Player:
    def __init__(self, color):
        self.pieces = None
        self.isWhite = color

    def startState(self):
        if self.isWhite:
            for x in range(0, 9):
                list.append()