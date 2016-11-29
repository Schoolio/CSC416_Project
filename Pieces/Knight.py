__author__ = 'Zac', 'Shawyn Kane'
import Pieces


class Knight:
    def __init__(self, location, isWhite):
        self.name = "Knight"
        self.value = 3
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True: self.image = "bin/Knight_W.png"
        else: self.image = "bin/Knight_B.png"

    def get_valid_moves(self, pieces, selectedPiece):
        output = []
        blocked0 = False
        blocked1 = False
        blocked2 = False
        blocked3 = False
        blocked4 = False
        blocked5 = False
        blocked6 = False
        blocked7 = False
        for x in pieces[:]:
            if x.location == (selectedPiece.location[0] + 1, selectedPiece.location[1] + 2):
                blocked0 = True
            elif not blocked0:
                output.append((selectedPiece.location[0] + 1, selectedPiece.location[1] + 2))

            if x.location == (selectedPiece.location[0] - 1, selectedPiece.location[1] + 2):
                blocked1 = True
            elif not blocked1:
                output.append((selectedPiece.location[0] - 1, selectedPiece.location[1] + 2))

            if x.location == (selectedPiece.location[0] + 1, selectedPiece.location[1] - 2):
                blocked2 = True
            elif not blocked2:
                output.append((selectedPiece.location[0] + 1, selectedPiece.location[1] - 2))

            if x.location == (selectedPiece.location[0] - 1, selectedPiece.location[1] - 2):
                blocked3 = True
            elif not blocked3:
                output.append((selectedPiece.location[0] - 1, selectedPiece.location[1] - 2))

            if x.location == (selectedPiece.location[0] + 2, selectedPiece.location[1] + 1):
                blocked4 = True
            elif not blocked4:
                output.append((selectedPiece.location[0] + 2, selectedPiece.location[1] + 1))

            if x.location == (selectedPiece.location[0] + 2, selectedPiece.location[1] - 1):
                blocked5 = True
            elif not blocked5:
                output.append((selectedPiece.location[0] + 2, selectedPiece.location[1] - 1))

            if x.location == (selectedPiece.location[0] - 2, selectedPiece.location[1] + 1):
                blocked6 = True
            elif not blocked6:
                output.append((selectedPiece.location[0] - 2, selectedPiece.location[1] + 1))

            if x.location == (selectedPiece.location[0] - 2, selectedPiece.location[1] - 1):
                blocked7 = True
            elif not blocked7:
                output.append((selectedPiece.location[0] - 2, selectedPiece.location[1] - 1))
            return output

    def move(self):  # TODO Write move() function for Knight
        pass

    def attack(self):  # TODO Write attack() function for Knight
        pass