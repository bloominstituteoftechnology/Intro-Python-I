# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, startRoom):
        self.name = name
        self.curRoom = startRoom
        self.holding = []  # Items the player is carrying, has in possession