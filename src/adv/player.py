# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, start):
        self.currentArea = start
        self.score = 0
        self.item = []