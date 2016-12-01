__author__ = 'Zac, Shawyn Kane'

import GameState


def make_move(gameState, target):
    validMoves = gameState.selectedPiece.get_valid_moves(gameState.pieces, gameState.selectedPiece)  # validate move
    print("Valid moves", validMoves)
    print(gameState.selectedPiece)
    if (validMoves is not None) and (target in validMoves[:]):  # validate move
        for piece in gameState.pieces[:]:  # this is suppose to remove a piece that is attacked
            if piece.location == target: gameState.pieces.remove(piece)  # suppose to remove a piece that is attacked
            elif (gameState.selectedPiece.name == "Pawn") and piece.isWhite != gameState.selectedPiece.isWhite and \
                 (piece.location == (gameState.selectedPiece.location[0] - 1, gameState.selectedPiece.location[1]) or \
                 piece.location == (gameState.selectedPiece.location[0] + 1, gameState.selectedPiece.location[1])) and \
                 piece.moved_two:
                gameState.pieces.remove(piece)
        if (gameState.selectedPiece.name == "Pawn") and (abs(gameState.selectedPiece.location[1] - target[1]) == 2):
            gameState.selectedPiece.moved_two = True
        elif gameState.selectedPiece.name == "Pawn":
            gameState.selectedPiece.moved_two = False
        gameState.selectedPiece.location = target  # move selected piece
        gameState.selectedPiece.initial_move = False  # indicate that the selected piece has been moved at least once
        gameState.whitesTurn = not gameState.whitesTurn  # change turn if the selected piece is moved
    print("new location", gameState.selectedPiece.location)
    gameState.selectedPiece = None  # deselect the selected piece
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