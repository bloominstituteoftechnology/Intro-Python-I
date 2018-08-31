# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """Holds information about a player"""
    def __init__(self, startRoom):
        self.curRoom = startRoom
        self.contents = []
        self.score = 0
