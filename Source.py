__author__ = 'Zac'

import Graphics, pygame, sys, Player, GameState, Pieces
from pygame.locals import *
from Pieces import Pawn


pygame.init()
myDisplay = pygame.display.set_mode((1000, 800), 0, 32)
Graphics.build_board(myDisplay)
gameState = GameState.GameState()

Graphics.build_pieces(myDisplay, gameState.whitePlayer)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()