# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, startRoom):
        self.curRoom = startRoom
        self.items = []

    def addItem(self, item):
         self.items.append(item)
