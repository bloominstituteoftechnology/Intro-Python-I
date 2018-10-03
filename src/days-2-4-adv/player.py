# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__ (self, room, items):
        self.room = room
        self.items = items
    def printRoom(self, room):
        print (self.room)
    def printItems(self, items):
        for item in items:
            print (item)

        