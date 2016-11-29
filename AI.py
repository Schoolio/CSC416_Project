__author__ = 'Zac'

import GameState


def make_move(gameState, target):
    validMoves = gameState.selectedPiece.get_valid_moves(gameState.pieces, gameState.selectedPiece)
    print("Valid moves", validMoves)
    for x in validMoves[:]:
        if x == target:
            gameState.selectedPiece.location = target
    return gameState

def suggested_move(gameState):
    isWhite = gameState.whitesTurn
    myValidMoves = []
    possibleMoves = []
    bestMove = None
    for x in gameState.pieces[:]:
        if isWhite == x.isWhite:
            print(x)
            gameState.selectedPiece = x
            myValidMoves.append((x, x.get_valid_moves(gameState.pieces, gameState.selectedPiece)))

    for x in myValidMoves[:]:
        gameState.selectedPiece = x[0]
        possibleMoves.append(gameState.make_move(gameState, x[1]))
    bScore = 0
    for x in possibleMoves[:]:
        t = x.score
        if t > bScore:
            bestMove = x
            bScore = t

    return bestMove