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
        for item in items:
            print (item)
    def drop(self, items):
        drop = input("What items do you want to drop: " for item in items)
        for item in self.items:
            if item != drop:
                self.items.append(item)

        