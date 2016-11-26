__author__ = 'Zac'


class Pawn:
    def __init__(self, location, isWhite):
        self.name = "Pawn"
        self.value = 1
        self.initialMove = True
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True:
            self.image = "bin/Pawn_W.png"
        else:
            self.image = "bin/Pawn_B.png"

    def move(self, twice=False):
        newlocation = None
        if (twice is True) and (self.initialMove is True):
            newlocation = (self.location[0] + 2, self.location[1])
        else:
            newlocation = (self.location[0] + 1, self.location[1])
        initialMove = False;
        # if check(newlocation):
        #   pass
        # else:
        #   return False
        self.location[0] = newlocation[0]
        self.locatoin[1] = newlocation[1]
        return True

    def attack(self, left):
        pass