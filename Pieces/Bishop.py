__author__ = 'Zac'


class Bishop:
    def __init__(self, location, isWhite):
        self.name = "Bishop"
        self.value = 3
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True:
            self.image = "bin/Bishop_W.png"
        else:
            self.image = "bin/Bishop_B.png"

    def move(self):
        pass

    def attack(self):
        pass