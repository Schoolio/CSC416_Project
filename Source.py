__author__ = 'Zac'

import Graphics, pygame, sys, Player, GameState
from pygame.locals import *


pygame.init()
myDisplay = pygame.display.set_mode((1000, 800), 0, 32)
Graphics.build_board(myDisplay)
gamestate = GameState.GameState()


Graphics.build_pieces(myDisplay, gamestate.whitePlayer.pieces)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()