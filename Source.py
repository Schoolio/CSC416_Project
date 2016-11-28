__author__ = 'Zac'

import Graphics, pygame, sys, GameState, Pieces
from pygame.locals import *


pygame.init()
myDisplay = pygame.display.set_mode(Graphics.resolution, 0, 32)
Graphics.build_border(myDisplay)
Graphics.build_board(myDisplay)
gameState = GameState.GameState()
Graphics.build_menu(myDisplay)
Graphics.build_pieces(myDisplay, gameState.pieces)
Graphics.build_status(myDisplay, gameState.status)
Graphics.build_score(myDisplay, gameState.score)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if Graphics.reset_text.collidepoint(pygame.mouse.get_pos()):
                gameState.reset()
                print("reset")