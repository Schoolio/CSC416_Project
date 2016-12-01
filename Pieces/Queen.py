__author__ = 'Zac, Shawyn Kane'


class Queen:
    def __init__(self, location, isWhite):
        self.name = "Queen"
        self.value = 10
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True: self.image = "bin/Queen_W.png"
        else: self.image = "bin/Queen_B.png"

    def get_valid_moves(self, pieces, selectedPiece):
        # if Pieces.protecting_king(pieces, selectedPiece.location, selectedPiece.isWhite): return None
        output = []
        blocked0 = False
        blocked1 = False
        blocked2 = False
        blocked3 = False
        blocked4 = False
        blocked5 = False
        blocked6 = False
        blocked7 = False
        for x in range(1, 9):
            for y in pieces[:]:
                if (selectedPiece.location[0] + x, selectedPiece.location[1]) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked0 = True
                elif not blocked0:
                    output.append((selectedPiece.location[0] + x, selectedPiece.location[1]))

                if (selectedPiece.location[0] - x, selectedPiece.location[1]) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked1 = True
                elif not blocked1:
                    output.append((selectedPiece.location[0] - x, selectedPiece.location[1]))

                if (selectedPiece.location[0], selectedPiece.location[1] + x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked2 = True
                elif not blocked2:
                    output.append((selectedPiece.location[0], selectedPiece.location[1] + x))

                if (selectedPiece.location[0], selectedPiece.location[1] - x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked3 = True
                elif not blocked3:
                    output.append((selectedPiece.location[0], selectedPiece.location[1] - x))

                if (selectedPiece.location[0] + x, selectedPiece.location[1] + x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked4 = True
                elif not blocked4:
                    output.append((selectedPiece.location[0] + x, selectedPiece.location[1] + x))

                if (selectedPiece.location[0] - x, selectedPiece.location[1] - x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked5 = True
                elif not blocked5:
                    output.append((selectedPiece.location[0] - x, selectedPiece.location[1] - x))

                if (selectedPiece.location[0] - x, selectedPiece.location[1] + x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked6 = True
                elif not blocked6:
                    output.append((selectedPiece.location[0] - x, selectedPiece.location[1] + x))

                if (selectedPiece.location[0]+ x, selectedPiece.location[1] - x) == y.location:
                    if y.isWhite != selectedPiece.isWhite: output.append(y.location)
                    blocked7 = True
                elif not blocked7:
                    output.append((selectedPiece.location[0] + x, selectedPiece.location[1] - x))
        return output

    def move(self):  # TODO Write move() function for Queen
        pass

    def attack(self):  # TODO Write attack() function for Queen
        pass