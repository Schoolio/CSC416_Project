__author__ = 'Zac'

import pygame, Pieces, sys
from pygame.locals import *

squareSize = 75
color = {"black": (39, 69, 19), "white": (255, 248, 220), "large_border": (205, 133, 63), "inlay_border": (0, 0, 0)}
boardStart = (75, 75)
resolution = (1070, 770)
borderWidth = 20
reset_text = None
board = [[0 for x in range(8)] for y in range(8)]

def build_board(display):
    for x in range(0, 8):
        for y in range(0, 8):
            if (x + y) % 2 == 0:
                board[y][x] = pygame.draw.rect(display, color["black"], ((boardStart[0] + (y * squareSize)), (boardStart[1] + (x * squareSize)), squareSize, squareSize))
            else:
                board[y][x] = pygame.draw.rect(display, color["white"], (boardStart[0] + (y * squareSize), boardStart[1] + (x * squareSize), squareSize, squareSize))


def build_pieces(display, pieces):
    for x in pieces[:]:
        display.blit(pygame.image.load(x.image), (boardStart[0] + (x.location[0] * squareSize), boardStart[1] + (x.location[1] * squareSize)))


def build_border(display):
    pygame.draw.rect(display, color["large_border"], (boardStart[0] - borderWidth, boardStart[1] - borderWidth, 640, 640))


def build_menu(display):
    BasicFont = pygame.font.SysFont(None, 64)
    pygame.draw.rect(display, (255, 255, 255), (boardStart[0] + (squareSize * 8) + 45, 55, 325, 640))
    pygame.draw.rect(display, (0, 0, 0), (boardStart[0] + (squareSize * 8) + 55, 65, 305, 620))
    BasicText = BasicFont.render("Chess", True, (255, 255, 255), (0, 0, 0))
    textRect = BasicText.get_rect()
    textRect.centerx = boardStart[0] + (squareSize * 8) + 55 + 157
    textRect.centery = 95
    display.blit(BasicText, textRect)
    reset_font = BasicFont.render("Reset", True, (0, 0, 0), (255, 255, 255))
    global reset_text
    reset_text = BasicText.get_rect()
    reset_text.centerx = boardStart[0] + (squareSize * 8) + 55 + 157
    reset_text.centery = 400
    display.blit(reset_font, reset_text)


def button_press():
    global reset_text


def build_status(display, status):
    BasicFont = pygame.font.SysFont(None, 32)
    status_font = BasicFont.render("Status: %s" % status, True, (255, 255, 255), (0, 0, 0))
    status_text = status_font.get_rect()
    status_text.centerx = boardStart[0] + (squareSize * 8) + 55 + 157
    status_text.centery = 200
    display.blit(status_font, status_text)


def build_score(display, score):
    BasicFont = pygame.font.SysFont(None, 32)
    status_font = BasicFont.render("Score: %s" % score, True, (255, 255, 255), (0, 0, 0))
    status_text = status_font.get_rect()
    status_text.centerx = boardStart[0] + (squareSize * 8) + 55 + 157
    status_text.centery = 500
    display.blit(status_font, status_text)