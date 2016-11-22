__author__ = 'Zac'

import pygame

squareSize = 20
resolution = (400, 400)
color = {"black": (39, 69, 19), "white": (255, 248, 220), "large_border": (205,133,63), "inlay_border": (0, 0, 0)}
boardStart = (25, 25)


def build_board():
    for x in range(0, 9):
        for y in range(0, 9):
            pygame.Rect()