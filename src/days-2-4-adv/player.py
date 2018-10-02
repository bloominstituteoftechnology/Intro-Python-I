# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.object = 'nothing'
    def changeRoom(self, newRoom):
        self.room = newRoom
    def addObject(self, newObject):
        self.object = newObject
    def dropObject(self):
        self.object = 'nothing'