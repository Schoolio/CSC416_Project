__author__ = 'Shawyn Kane'


def location_is_empty(self, pieces, new_location):
    return new_location not in [x.location for x in pieces]


def protecting_king(self, pieces, piece_to_check_location):
    king_location = None
    for x in pieces:
        if x.name is "King":
            king_location = x.location
            break
    location_difference = (king_location[0]-piece_to_check_location[0],king_location[1]-piece_to_check_location[1])
    if abs(location_difference[0])/abs(location_difference[1]) == 1:
        if ((location_difference[0]/abs(location_difference[0])) + (location_difference[1]/abs(location_difference[1]))) == -2:
            check_location = [piece_to_check_location[0]-1, piece_to_check_location[1]-1]
            while check_location[0] > -1 and check_location[1] > -1:
                for x in pieces:
                    if x.location == check_location:
                        if x.name in ("Bishop", "Queen"): return True
                        else: return False
                check_location[0] -= 1
                check_location[1] -= 1
            return False
        elif ((location_difference[0]/abs(location_difference[0])) + (location_difference[1]/abs(location_difference[1]))) == 2:
            check_location = [piece_to_check_location[0] + 1, piece_to_check_location[1] + 1]
            while check_location[0] < 8 and check_location[1] < 8:
                for x in pieces:
                    if x.location == check_location:
                        if x.name in ("Bishop", "Queen"):
                            return True
                        else:
                            return False
                check_location[0] += 1
                check_location[1] += 1
            return False
        elif ((location_difference[0]/abs(location_difference[0])) + abs(location_difference[1]/abs(location_difference[1]))) == 2:
            check_location = [piece_to_check_location[0] + 1, piece_to_check_location[1] - 1]
            while check_location[0] < 8 and check_location[1] > -1:
                for x in pieces:
                    if x.location == check_location:
                        if x.name in ("Bishop", "Queen"):
                            return True
                        else:
                            return False
                check_location[0] += 1
                check_location[1] -= 1
            return False
        elif ((location_difference[0]/abs(location_difference[0])) + abs(location_difference[1]/abs(location_difference[1]))) == 0:
            check_location = [piece_to_check_location[0] - 1, piece_to_check_location[1] + 1]
            while check_location[0] > -1 and check_location[1] < 8:
                for x in pieces:
                    if x.location == check_location:
                        if x.name in ("Bishop", "Queen"):
                            return True
                        else:
                            return False
                check_location[0] -= 1
                check_location[1] += 1
            return False
    elif king_location[0] == piece_to_check_location[0]:
        if (king_location[1] - piece_to_check_location[1]) > 0:
            check_location = [piece_to_check_location[0], piece_to_check_location[1] + 1]
            while check_location[1] < 8:
                for x in pieces:
                    if x.location == check_location:
                        if x.name in ("Rook", "Queen"):
                            return True
                        else:
                            return False
                check_location[1] += 1
            return False
        else:
            check_location = [piece_to_check_location[0], piece_to_check_location[1] - 1]
            while check_location[1] > -1:
                for x in pieces:
                    if x.location == check_location:
                        if x.name in ("Rook", "Queen"):
                            return True
                        else:
                            return False
                check_location[1] -= 1
            return False
    elif king_location[1] == piece_to_check_location[1]:
        if (king_location[0] - piece_to_check_location[0]) > 0:
            check_location = [piece_to_check_location[0] + 1, piece_to_check_location[1]]
            while check_location[0] < 8:
                for x in pieces:
                    if x.location == check_location:
                        if x.name in ("Rook", "Queen"):
                            return True
                        else:
                            return False
                check_location[0] += 1
            return False
        else:
            check_location = [piece_to_check_location[0] - 1, piece_to_check_location[1]]
            while check_location[0] > -1:
                for x in pieces:
                    if x.location == check_location:
                        if x.name in ("Rook", "Queen"):
                            return True
                        else:
                            return False
                check_location[0] -= 1