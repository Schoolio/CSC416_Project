# Zac Smith
import Pieces
from Pieces import Pawn, King, Rook, Queen, Bishop, Knight


# Gamestate handles the players and turns
# Player has access to pieces to build the piece list
class GameState:
    def __init__(self):
        self.whitesTurn = True
        self.pieces = []
        self.reset()
        self.status = "None"
        self.score = 0
        self.selectedPiece = None

    # Used to reset the game state to a starting position
    def reset(self):
        for x in range(0, 8):
            self.pieces.append(Pawn.Pawn((x, 6), True))
            self.pieces.append(Pawn.Pawn((x, 1), False))
        # White Pieces
        self.pieces.append(Rook.Rook((7, 7), True))
        self.pieces.append(Rook.Rook((0, 7), True))
        self.pieces.append(Knight.Knight((1, 7), True))
        self.pieces.append(Knight.Knight((6, 7), True))
        self.pieces.append(Bishop.Bishop((2, 7), True))
        self.pieces.append(Bishop.Bishop((5, 7), True))
        self.pieces.append(Queen.Queen((3, 7), True))
        self.pieces.append(King.King((4, 7), True))
        # Black Pieces
        self.pieces.append(Rook.Rook((7, 0), False))
        self.pieces.append(Rook.Rook((0, 0), False))
        self.pieces.append(Knight.Knight((1, 0), False))
        self.pieces.append(Knight.Knight((6, 0), False))
        self.pieces.append(Bishop.Bishop((2, 0), False))
        self.pieces.append(Bishop.Bishop((5, 0), False))
        self.pieces.append(Queen.Queen((3, 0), False))
        self.pieces.append(King.King((4, 0), False))
        # Set turn
        self.whitesTurn = True

    def calculate_score(self):
        output = 0
        for x in self.pieces:
            if x.isWhite:
                output = output + x.value
            else:
                output = output - x.value
        return output

    def select_piece(self, location):
        for x in self.pieces[:]:
            if x.location == location:
                return x