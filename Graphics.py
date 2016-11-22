__author__ = 'Zac'

import pygame, Pieces

squareSize = 70
resolution = (400, 400)
color = {"black": (39, 69, 19), "white": (255, 248, 220), "large_border": (205, 133, 63), "inlay_border": (0, 0, 0)}
boardStart = (25, 100)


def build_board(display):
    for x in range(0, 8):
        for y in range(0, 8):
            if (x + y) % 2 == 0:
                pygame.draw.rect(display, color["black"], ((boardStart[0] + (y * squareSize)), (boardStart[1] + (x * squareSize)), squareSize, squareSize))
            else:
                pygame.draw.rect(display, color["white"], (boardStart[0] + (y * squareSize), boardStart[1] + (x * squareSize), squareSize, squareSize))


def build_pieces(display, pieces):
    for x in pieces[:]:
        display.blit(pygame.image.load(x.image), (boardStart[0] + (x.location[0] * squareSize), boardStart[1] + (x.location[1] * squareSize)))