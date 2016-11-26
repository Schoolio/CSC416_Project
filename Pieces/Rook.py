__author__ = 'Zac'


class Rook:
    def __init__(self, location, isWhite):
        self.name = "Rook"
        self.value = 5
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True:
            self.image = "bin/Rook_W.png"
        else:
            self.image = "bin/Rook_B.png"

    def move(self):
        pass

    def attack(self):
        pass