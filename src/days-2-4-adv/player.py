# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__ (self, name, room, items=["flashlight", "first-aid kit", "rock"]):
        self.room = room
        self.items = items
        self.name = name
    def printRoom(self, room):
        print (self.room)
    def printItems(self, items):
        print (items)
    def drop(self, items):
        drop = input(f"What items do you want to drop: {self.items}\n->")
        self.items.remove(drop)
    def get(self, items):
        return ''