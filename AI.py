__author__ = 'Zac'

import GameState


def make_move(gameState, target):
    validMoves = gameState.selectedPiece.get_valid_moves(gameState.pieces, gameState.selectedPiece)
    print("Valid moves", validMoves)
    print(gameState.selectedPiece)
    if (validMoves is not None) and (target in validMoves[:]):
        gameState.selectedPiece.location = target
        gameState.selectedPiece.initial_move = False
        gameState.whitesTurn = not gameState.whitesTurn
    print("new location", gameState.selectedPiece.location)
    gameState.selectedPiece = None
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
        possibleMoves.append(make_move(gameState, x[1]))
    bScore = 0
    for x in possibleMoves[:]:
        t = x.score
        if t > bScore:
            bestMove = x
            bScore = t

    return bestMove