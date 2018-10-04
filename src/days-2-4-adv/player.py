# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__ (self, name, room, items):
        self.room = room
        self.items = items
        self.name = name
    def printRoom(self, room):
        print (self.room)
    def printItems(self, items):
        print (items)
    def drop(self, items):
        drop = input(f"What items do you want to drop: {self.items}\n->")
        return self.items.remove(drop)
    def get(self, items):
        print (self.room.items)
        get = input("Choose an item \n-> ")
        for item in self.room.items:
            if item == get:
                self.items.append(get)
            else:
                print ("You already have that item or no item not found")
