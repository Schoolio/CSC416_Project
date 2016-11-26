__author__ = 'Zac'


class King:
    def __init__(self, location, isWhite):
        self.name = "King"
        self.value = 100
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True:
            self.image = "bin/King_W.png"
        else:
            self.image = "bin/King_B.png"

    def move(self):
        pass

    def attack(self):
        pass