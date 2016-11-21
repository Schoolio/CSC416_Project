#Zac Smith
import Player
class GameState:
    def __init__(self):
        self.board = []
        self.whitesTurn = False
        self.whitePlayer = Player.Player(True)
        self.blackPlayer = Player.Player(False)

    def reset(self):
        x = 0;