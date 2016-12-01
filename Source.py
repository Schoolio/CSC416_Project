__author__ = 'Zac, Shawyn Kane'

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
        if event.type == KEYDOWN:
            if event.key == K_1:
                gameState.pieces = gameState.preset1()
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

                        if ((gameState.selectedPiece is None) and (gameState.get_piece((x, y)) is not None)) and (gameState.get_piece((x, y)).isWhite is gameState.whitesTurn):
                            print(x, y)
                            if gameState.whitesTurn == gameState.get_piece((x, y)).isWhite:
                                gameState.selectedPiece = gameState.get_piece((x, y))
                                myBool = True
                                break
                            gameState.selectedPiece = gameState.get_piece((x, y))
                            myBool = True
                            break
                        # The following elif block will select the tile to move the selected piece and try to move the
                        # currently selected piece (if there is one selected) if the tile selected is not valid to move
                        # to the currently selected piece will be deselected (in AI.make_move() function).
                        elif (gameState.selectedPiece is not None) and (gameState.get_piece((x, y)) is None):
                            print("Target:", (x, y))
                            #gameState.selectedPiece.move(gameState.pieces, (x, y), False)
                            gameState = AI.make_move(gameState, (x, y))

                            myBool = True
                            break
                    if myBool:
                        break
    fpsClock.tick(60)
    pygame.display.update()