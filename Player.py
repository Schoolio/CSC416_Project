__author__ = 'Zac'
import Pieces
from Pieces import Pawn, King, Queen, Bishop, Knight, Rook

class Player:
    def __init__(self, color):
        self.isWhite = color
        self.pieces = []
        self.startState()

    #used to reset the players to a starting state
    #mostly used in the parent function reset in GameState.py
    def startState(self):
        if self.isWhite is True:
            for x in range(0, 8):
                self.pieces.append(Pawn.Pawn((x, 6)))