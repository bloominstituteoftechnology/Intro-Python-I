# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, currentRoom, items):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    # deal with items by player
    def addItem(self, item):
        self.items.append(item)

