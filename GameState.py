#Zac Smith
import Player
class GameState:
    def __init__(self):
        self.board = []
        self.whitesTurn = False
        self.whitePlayer = Player.Player('w')
        self.blackPlayer = Player.Player('b')

    def reset(self):
        x = 0;