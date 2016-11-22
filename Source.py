__author__ = 'Zac'

import Graphics, pygame, sys, Player
from pygame.locals import *


pygame.init()
myDisplay = pygame.display.set_mode((1000, 800), 0, 32)
Graphics.build_board(myDisplay)
pygame.display.update()
white = Player.Player(True)
Graphics.build_pieces(myDisplay,white)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()