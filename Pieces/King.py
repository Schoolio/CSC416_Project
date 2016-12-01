__author__ = 'Zac, Shawyn Kane'
import Pieces


class King:
    def __init__(self, location, isWhite):
        self.name = "King"
        self.value = 100
        self.location = location
        self.image = None
        self.isWhite = isWhite

        if self.isWhite is True: self.image = "bin/King_W.png"
        else: self.image = "bin/King_B.png"

    def get_valid_moves(self, pieces, selectedPiece):
        x = 1
        moves = ((selectedPiece.location[0] + x, selectedPiece.location[1]),
                 (selectedPiece.location[0] - x, selectedPiece.location[1]),
                 (selectedPiece.location[0], selectedPiece.location[1] + x),
                 (selectedPiece.location[0], selectedPiece.location[1] - x),
                 (selectedPiece.location[0] + x, selectedPiece.location[1] + x),
                 (selectedPiece.location[0] - x, selectedPiece.location[1] - x),
                 (selectedPiece.location[0] - x, selectedPiece.location[1] + x),
                 (selectedPiece.location[0] + x, selectedPiece.location[1] - x))
        output = []
        pieces_on_same_side = []
        # opponent_knights_moves = None

        for piece in pieces:
            if piece.isWhite == selectedPiece.isWhite: pieces_on_same_side.append(piece)

        occupied_locations = [x.location for x in pieces_on_same_side]
        # opponent_knights_moves = [k.get_valid_moves(self, pieces, k) for k in pieces if (k.name == "Knight") and \
        #                          (k.isWhite is not selectedPiece.isWhite)]
        # for move in moves:
        #     if (move not in occupied_locations) and (not Pieces.protecting_king(pieces, move, selectedPiece.isWhite)):
        #         if opponent_knights_moves is not None:
        #             for x in opponent_knights_moves:
        #                 if move not in x: output.append(move)
        #         else:
        #             output.append(move)
        for move in moves:
            if move not in occupied_locations:
                output.append(move)
        return output

    def move(self):  # TODO Write move() function for King
        pass

    def attack(self):  # TODO Write attack() function for King
        pass