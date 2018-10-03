# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.inRoom = room
        self.items = []

    def move(self, room):
        self.inRoom = room

    def addItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)

    def showItmes(self):
        print('You are holding the following: ')
        for item in self.items:
            print(item.name)
        
