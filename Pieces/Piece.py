import Pawn, Rook, King, Queen, Knight, Bishop

class Pieces:
    def __init__(self, type, location):
        self.type = self.setType(type)
        self.location = location

    def setType(self, type):
        if type is "Pawn":
            return Pawn.Pawn()
        elif type is "Rook":
            return Rook.Rook()
        elif type is "Knight":
            return Knight.Knight()
        elif type is "Bishop":
            return Bishop.Bishop()
        elif type is "Queen":
            return Queen.Queen()
        elif type is "King":
            return King.King()