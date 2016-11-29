__author__ = 'Zac'


def get_valid_moves(pieces, selectedPiece):
    output = []
    if selectedPiece.name is "Rook":
        None
    elif selectedPiece.name is "Knight":
        None
    elif selectedPiece.name is "Bishop":
        None
    elif selectedPiece.name is "Queen":
        None
    elif selectedPiece.name is "King":
        None
    elif selectedPiece.name is "Pawn":
        if selectedPiece.isWhite:
            if selectedPiece.initial_move:
                blocked = False
                for x in pieces[:]:
                    if x.location == selectedPiece.location[0] - 1 or x.location == selectedPiece.location[0] - 2:
                        blocked = True
            if blocked is False:
                output.append((selectedPiece.location[0] - 1, selectedPiece.location[1]))
                output.append((selectedPiece.location[0] - 2, selectedPiece.location[1]))
                return output

            for x in pieces[:]:
                if x.location == selectedPiece.location[0] - 1:
                    blocked = True

            if blocked is False:
                output.append((selectedPiece.location[0] - 1, selectedPiece.location[1]))
                return output

        if not selectedPiece.isWhite:
            if selectedPiece.initial_move:
                blocked = False
                for x in pieces[:]:
                    if x.location == selectedPiece.location[0] + 1 or x.location == selectedPiece.location[0] + 2:
                        blocked = True
            if blocked is False:
                output.append((selectedPiece.location[0] + 1, selectedPiece.location[1]))
                output.append((selectedPiece.location[0] + 2, selectedPiece.location[1]))
                return output

            for x in pieces[:]:
                if x.location == selectedPiece.location[0] + 1:
                    blocked = True

            if blocked is False:
                output.append((selectedPiece.location[0] + 1, selectedPiece.location[1]))
                return output