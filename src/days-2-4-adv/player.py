# Write a class to hold player information, e.g. what room they are in
# currently.

# created a simple constructor to take in a room to match the calling convention in my adv.py
class Player:
    def __init__(self, room):
        self.room = room