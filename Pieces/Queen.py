__author__ = 'Zac'


class Queen:
    def __init__(self, location, isWhite):
        self.name = "Queen"
        self.value = 10
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True:
            self.image = "bin/Queen_W.png"
        else:
            self.image = "bin/Queen_B.png"

    def move(self):
        pass

    def attack(self):
        pass