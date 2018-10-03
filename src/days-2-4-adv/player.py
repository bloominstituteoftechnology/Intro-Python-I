# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player:
    def __init__(self, currentRoom):
        self.currentRoom = currentRoom
        self.items = [None]

    def get(self, item):
        self.items.append(Item['name'])
