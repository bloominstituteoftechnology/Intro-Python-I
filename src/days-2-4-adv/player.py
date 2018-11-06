# Write a class to hold player information, e.g. what room they are in
# currently.

# created a simple constructor to take in a room to match the calling convention in my adv.py
class Player:
    def __init__(self, room, items=None):
        self.room = room
        self.items = [] if items is None else items
        self.gold = 0