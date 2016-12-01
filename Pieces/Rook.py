__author__ = 'Zac, Shawyn Kane'
import Pieces

class Rook:
    def __init__(self, location, isWhite):
        self.name = "Rook"
        self.value = 5
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True: self.image = "bin/Rook_W.png"
        else: self.image = "bin/Rook_B.png"

    def get_valid_moves(self, pieces, selectedPiece):
        # if Pieces.protecting_king(pieces, selectedPiece.location, selectedPiece.isWhite): return None
        output = []
        blocked0 = False
        blocked1 = False
        blocked2 = False
        blocked3 = False
        for x in range(1, 9):
            for y in pieces[:]:
                if (selectedPiece.location[0] + x, selectedPiece.location[1]) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked0 = True
                elif (not blocked0) and ((selectedPiece.location[0] + x, selectedPiece.location[1]) not in output):
                    output.append((selectedPiece.location[0] + x, selectedPiece.location[1]))

                if (selectedPiece.location[0] - x, selectedPiece.location[1]) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked1 = True
                elif (not blocked1) and ((selectedPiece.location[0] - x, selectedPiece.location[1]) not in output):
                    output.append((selectedPiece.location[0] - x, selectedPiece.location[1]))

                if (selectedPiece.location[0], selectedPiece.location[1] + x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked2 = True
                elif (not blocked2) and ((selectedPiece.location[0], selectedPiece.location[1] + x) not in output):
                    output.append((selectedPiece.location[0], selectedPiece.location[1] + x))

                if (selectedPiece.location[0], selectedPiece.location[1] - x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked3 = True
                elif (not blocked3) and ((selectedPiece.location[0], selectedPiece.location[1] - x) not in output):
                    output.append((selectedPiece.location[0], selectedPiece.location[1] - x))
        return output

    def attack(self):  # TODO Write attack() function for Rook
        pass