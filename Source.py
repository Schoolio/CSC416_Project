__author__ = 'Zac'

import Graphics, pygame, sys, GameState, Pieces
from pygame.locals import *


pygame.init()
myDisplay = pygame.display.set_mode(Graphics.resolution, 0, 32)
gameState = GameState.GameState()
fpsClock = pygame.time.Clock()

while True:
    Graphics.build_border(myDisplay)
    Graphics.build_board(myDisplay)
    Graphics.build_menu(myDisplay)
    Graphics.build_pieces(myDisplay, gameState.pieces)
    Graphics.build_status(myDisplay, gameState.status)
    Graphics.build_score(myDisplay, gameState.score)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            #Checks for reset button click
            if Graphics.reset_text.collidepoint(pygame.mouse.get_pos()):
                gameState.reset()
                print("reset")
            #Checks for selection a position
            for x in range(8):
                temp = Graphics.board[x]
                for y in range(8):
                    local = temp[y]
                    if local.collidepoint(pygame.mouse.get_pos()):
                        print(x, y)
    fpsClock.tick(60)
    pygame.display.update()