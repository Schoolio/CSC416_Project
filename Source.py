__author__ = 'Zac'

import Graphics, pygame, sys, GameState, Pieces, AI
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
    Graphics.build_suggest(myDisplay)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            # Checks for reset button click
            if Graphics.reset_text.collidepoint(pygame.mouse.get_pos()):
                gameState.reset()
                print("reset")
            if Graphics.suggestButton.collidepoint(pygame.mouse.get_pos()):
                gameState = AI.suggested_move(gameState)
                print("suggest")
            # Checks for selection a position
            myBool = False
            for x in range(8):
                temp = Graphics.board[x]
                for y in range(8):
                    local = temp[y]
                    if local.collidepoint(pygame.mouse.get_pos()):
                        if gameState.selectedPiece is None:
                            print(x, y)
                            gameState.selectedPiece = gameState.get_piece((x, y))
                            myBool = True
                            break
                        elif (gameState.selectedPiece is not None) and (gameState.get_piece((x, y)) is None):
                            print("Target:", (x, y))
                            #gameState.selectedPiece.move(gameState.pieces, (x, y), False)
                            gameState = AI.make_move(gameState, (x, y))
                            print("new location", gameState.selectedPiece.location)
                            gameState.selectedPiece = None
                            myBool = True
                            break
                    if myBool:
                        break
    fpsClock.tick(60)
    pygame.display.update()