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
        print (f"Inventory: {items}")
    def drop(self, items):
        drop = input(f"\nWhat items do you want to drop: {self.items}\n->")
        self.items.remove(drop)
        self.room.items.append(drop)
    def get(self, items):
        print (f"\n{self.room.items}")
        get = input("Choose an item \n-> ")
        for item in self.room.items:
            if item == get:
                self.items.append(get)
            else:
                print ("\nYou already have that item or no item not found\n")
