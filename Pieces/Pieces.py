__author__ = 'Shawyn Kane'


def location_is_empty(self, pieces, new_location):
    return new_location not in [x.location for x in pieces]