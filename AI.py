__author__ = 'Zac'

import GameState


def make_move(gameState, target):
    validMoves = gameState.selectedPiece.get_valid_moves(gameState.pieces, gameState.selectedPiece)
    print("Valid moves", validMoves)
    for x in validMoves[:]:
        if x == target:
            gameState.selectedPiece.location = target
    return gameState