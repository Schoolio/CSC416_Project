__author__ = 'Zac, Shawyn Kane'
import Pieces


class King:
    def __init__(self, location, isWhite):
        self.name = "King"
        self.value = 100
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True: self.image = "bin/King_W.png"
        else: self.image = "bin/King_B.png"

    def get_valid_moves(self, pieces, selectedPiece):
        output = []
        block0 = False
        block1 = False
        block2 = False
        block3 = False
        block4 = False
        block5 = False
        block6 = False
        block7 = False
        for x in pieces[:]:
            if x.location is (self.location[0] + 1, self.location[1]):
                block0 = True
            if x.location is (self.location[0] - 1, self.location[1]):
                block1 = True
            if x.location is (self.location[0] + 1, self.location[1] + 1):
                block2 = True
            if x.location is (self.location[0] + 1, self.location[1] - 1):
                block3 = True
            if x.location is (self.location[0], self.location[1] + 1):
                block4 = True
            if x.location is (self.location[0], self.location[1] - 1):
                block5 = True
            if x.location is (self.location[0] - 1, self.location[1] + 1):
                block6 = True
            if x.location is (self.location[0] - 1, self.location[1] + 1):
                block7 = True

        if not block0:
            output.append((self.location[0] + 1, self.location[1]))
        if not block1:
            output.append((self.location[0] - 1, self.location[1]))
        if not block2:
            output.append((self.location[0] + 1, self.location[1] + 1))
        if not block3:
            output.append((self.location[0] + 1, self.location[1] - 1))
        if not block4:
            output.append((self.location[0], self.location[1] + 1))
        if not block5:
            output.append((self.location[0], self.location[1] - 1))
        if not block6:
            output.append((self.location[0] - 1, self.location[1] + 1))
        if not block7:
            output.append((self.location[0] - 1, self.location[1] + 1))
        return output
    def move(self):  # TODO Write move() function for King
        pass

    def attack(self):  # TODO Write attack() function for King
        pass