__author__ = 'Zac'

import GameState

def get_valid_moves(pieces, selectedPiece):

    elif selectedPiece.name is "Knight":
        pass
    elif selectedPiece.name is "Bishop":
        pass
    elif selectedPiece.name is "Queen":
        pass
    elif selectedPiece.name is "King":
        pass
    elif selectedPiece.name is "Pawn":
        if selectedPiece.is_white:
            if selectedPiece.initial_move:
                blocked = False
                for x in pieces[:]:
                    if x.location == selectedPiece.location[1] - 1 or x.location == selectedPiece.location[1] - 2:
                        blocked = True
            if blocked is False:
                output.append((selectedPiece.location[0], selectedPiece.location[1] - 1))
                output.append((selectedPiece.location[0], selectedPiece.location[1] - 2))
                return output

            for x in pieces[:]:
                if x.location == selectedPiece.location[1] - 1:
                    blocked = True

            if blocked is False:
                output.append((selectedPiece.location[0], selectedPiece.location[1] - 1))
                return output

        if not selectedPiece.is_white:
            if selectedPiece.initial_move:
                blocked = False
                for x in pieces[:]:
                    if x.location == selectedPiece.location[1] + 1 or x.location == selectedPiece.location[1] + 2:
                        blocked = True
            if blocked is False:
                output.append((selectedPiece.location[0], selectedPiece.location[1] + 1))
                output.append((selectedPiece.location[0], selectedPiece.location[1] + 2))
                return output

            for x in pieces[:]:
                if x.location == selectedPiece.location[1] + 1:
                    blocked = True

            if blocked is False:
                output.append((selectedPiece.location[0], selectedPiece.location[1] + 1))
                return output

def make_move(gameState, target):
    validMoves = gameState.selectedPiece.get_valid_moves(gameState.pieces, gameState.selectedPiece)
    print("Valid moves", validMoves)
    for x in validMoves[:]:
        if x == target:
            gameState.selectedPiece.location = target
    return gameState