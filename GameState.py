#Zac Smith
import Pieces
from Pieces import Pawn, King, Rook, Queen, Bishop, Knight

#Gamestate handles the players and turns
#Player has access to pieces to build the piece list
class GameState:
    def __init__(self):
        self.whitesTurn = True
        self.whitePlayer = []
        self.blackPlayer = []
        self.reset()

    #Used to reset the game state to a starting position
    def reset(self):
        for x in range(0, 8):
            self.whitePlayer.append(Pawn.Pawn((x, 6), True))
        self.whitesTurn = True