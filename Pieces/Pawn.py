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

    def move(self, pieces, twice=False):
        new_location = None

        if (twice is True) and (self.initial_move is True): new_location = (self.location[0] + 2, self.location[1])
        else: new_location = (self.location[0] + 1, self.location[1])

        if not Pieces.location_is_empty(pieces, new_location): return False

        self.initial_move = False;
        self.location[0] = new_location[0]
        self.locatoin[1] = new_location[1]
        return True

    def attack(self, pieces, left):
        new_location = None
        self.initial_move = False;

        if Pieces.location_is_empty(pieces, new_location): return False

        for x in pieces:
            if x.location is new_location: pieces.remove(x)
        self.location[0] = new_location[0]
        self.locatoin[1] = new_location[1]
        return True