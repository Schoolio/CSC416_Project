__author__ = 'Zac'
import Pieces

class Player:
    def __init__(self, color):
        self.pieces = None
        self.isWhite = color
        self.image = "bin/Pawn_W.png"
        self.location = (0, 0)

    #used to reset the players to a starting state
    #mostly used in the parent function reset in GameState.py
    def startState(self):
        if self.isWhite:
            for x in range(0, 9):
                list.append()