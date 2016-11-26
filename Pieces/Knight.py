__author__ = 'Zac'


class Knight:
    def __init__(self, location, isWhite):
        self.name = "Knight"
        self.value = 3
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True:
            self.image = "bin/Knight_W.png"
        else:
            self.image = "bin/Knight_B.png"

    def move(self):
        pass

    def attack(self):
        pass