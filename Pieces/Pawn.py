__author__ = 'Zac, Shawyn Kane'
import Pieces

class Pawn:
    def __init__(self, location, is_white):
        self.name = "Pawn"
        self.value = 1
        self.initial_move = True
        self.location = location
        self.image = None
        self.is_white = is_white

        if self.is_white is True: self.image = "bin/Pawn_W.png"
        else: self.image = "bin/Pawn_B.png"

    def get_is_white(self):
        return self.is_white

    def move(self, pieces, inputLocation, twice=False):
        if inputLocation is not (self.location[0], self.location[1] - 1):
            return False
        elif inputLocation is not (self.location[0], self.location[1] - 2):
            return False
        print("do we get here")
        new_location = None

        if (twice is True) and (self.initial_move is False): return False
        if (twice is True) and (self.initial_move is True): new_location = (self.location[0], self.location[1] - 2)
        else: new_location = (self.location[0], self.location[1] - 1)

        if not Pieces.location_is_empty(pieces, new_location): return False
        if Pieces.protecting_king(pieces, self.location): return False
        self.initial_move = False;

        self.location = new_location
        return True

    def attack(self, pieces, left):
        new_location = None
        self.initial_move = False;

        if Pieces.location_is_empty(pieces, new_location) or Pieces.protecting_king(pieces, self.location): return False
        for x in pieces:
            if x.location == new_location: pieces.remove(x)
        self.location[0] = new_location[0]
        self.locatoin[1] = new_location[1]
        return True

    def get_valid_moves(self, selectedPiece, pieces):
        output = []
        if selectedPiece.get_is_white():
            if selectedPiece.initial_move:
                blocked = False
                for x in pieces[:]:
                    if x.location == selectedPiece.location[1] - 1 or x.location == selectedPiece.location[1] - 2:
                        blocked = True
            if blocked is False:
                output.append((selectedPiece.location[0], selectedPiece.location[1] - 1))
                output.append((selectedPiece.location[0], selectedPiece.location[1] - 2))
                return output

            for x in pieces[:]:
                if x.location == selectedPiece.location[1] - 1:
                    blocked = True

            if blocked is False:
                output.append((selectedPiece.location[0], selectedPiece.location[1] - 1))
                return output

        if not selectedPiece.is_white:
            if selectedPiece.initial_move:
                blocked = False
                for x in pieces[:]:
                    if x.location == selectedPiece.location[1] + 1 or x.location == selectedPiece.location[1] + 2:
                        blocked = True
            if blocked is False:
                output.append((selectedPiece.location[0], selectedPiece.location[1] + 1))
                output.append((selectedPiece.location[0], selectedPiece.location[1] + 2))
                return output

            for x in pieces[:]:
                if x.location == selectedPiece.location[1] + 1:
                    blocked = True

            if blocked is False:
                output.append((selectedPiece.location[0], selectedPiece.location[1] + 1))
                return output