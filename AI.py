__author__ = 'Zac'

import GameState

def get_valid_moves(pieces, selectedPiece):
    output = []
    blocked0 = False
    blocked1 = False
    blocked2 = False
    blocked3 = False
    if selectedPiece.name is "Rook":
        for x in range(8):
            for y in pieces[:]:
                if (selectedPiece.location[0] + x, selectedPiece.location[1]) == y.location:
                    blocked0 = True
                elif not blocked0:
                    output.append((selectedPiece.location[0] + x, selectedPiece.location[1]))

                if (selectedPiece.location[0] - x, selectedPiece.location[1]) == y.location:
                    blocked1 = True
                elif not blocked1:
                    output.append((selectedPiece.location[0] - x, selectedPiece.location[1]))

                if (selectedPiece.location[0], selectedPiece.location[1] + x) == y.location:
                    blocked2 = True
                elif not blocked2:
                    output.append((selectedPiece.location[0], selectedPiece.location[1] + x))

                if (selectedPiece.location[0], selectedPiece.location[1] - x) == y.location:
                    blocked3 = True
                elif not blocked3:
                    output.append((selectedPiece.location[0], selectedPiece.location[1] - x))
    elif selectedPiece.name is "Knight":
        None
    elif selectedPiece.name is "Bishop":
        None
    elif selectedPiece.name is "Queen":
        None
    elif selectedPiece.name is "King":
        None
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
    validMoves = get_valid_moves(gameState.pieces, gameState.selectedPiece)
    print("Valid moves", validMoves)
    for x in validMoves[:]:
        if x == target:
            gameState.selectedPiece.location = target
    return gameState