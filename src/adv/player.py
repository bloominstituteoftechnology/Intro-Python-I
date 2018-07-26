# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource


class Player:
    def __init__(self, room):
        self.room = room
        self.items = []
        self.score = 0

    def position(self):
        return self.room

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        return self.items.remove(item)

    def hasLightSource(self):
        for item in self.items:
            if isinstance(item, LightSource):
                return True
        return False
