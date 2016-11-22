#Zac Smith
import Player


#Gamestate handles the players and turns
#Player has access to pieces to build the piece list
class GameState:
    def __init__(self):
        self.board = []
        self.whitesTurn = False
        self.whitePlayer = Player.Player(True)
        self.blackPlayer = Player.Player(False)

    #Used to reset the game state to a starting position
    def reset(self):
        self.whitePlayer.startState()
        self.blackPlayer.startState()
        self.whitesTurn = True