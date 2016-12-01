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

    def get_valid_moves(self, pieces, selectedPiece):
        output = []
        blocked0 = False
        blocked1 = False
        blocked2 = False
        blocked3 = False
        for x in range(1, 9):
            for y in pieces[:]:
                if (selectedPiece.location[0] + x, selectedPiece.location[1] + x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked0 = True
                elif not blocked0:
                    output.append((selectedPiece.location[0] + x, selectedPiece.location[1] + x))

                if (selectedPiece.location[0] - x, selectedPiece.location[1] - x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked1 = True
                elif not blocked1:
                    output.append((selectedPiece.location[0] - x, selectedPiece.location[1] - x))

                if (selectedPiece.location[0] - x, selectedPiece.location[1] + x) == y.location:
                    blocked2 = True
                elif not blocked2:
                    output.append((selectedPiece.location[0] - x, selectedPiece.location[1] + x))

                if (selectedPiece.location[0] + x, selectedPiece.location[1] - x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked3 = True
                elif not blocked3:
                    output.append((selectedPiece.location[0] + x, selectedPiece.location[1] - x))
        return output

    def move(self):  # TODO Write move() function for Bishop
        pass

    def attack(self):  # TODO Write attack() function for Bishop
        pass