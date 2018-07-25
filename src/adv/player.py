# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self,playerName,start,inventory):
        self.current = start;
        self.name = playerName;
        self.inventory =inventory

