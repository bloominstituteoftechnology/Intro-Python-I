# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__ (self, name, room, items=[], score=0):
        self.room = room
        self.items = items
        self.name = name
        self.score = score
    def printRoom(self, room):
        print (self.room)
    def printItems(self, items):
        print (f"Inventory: {items}")
    def drop(self, items):
        drop = input(f"\nWhat items do you want to drop: {self.items}\n->")
        if drop == '':
            return
        else:
            self.items.remove(drop)
        self.room.items.append(drop)
        if self.score < 11 and self.score >= 0:
            self.score = 0
        else:
            self.score-=10
    def get(self, items):
        print (f"\n{self.items}")
        get = input("Choose an item \n-> ")
        for item in self.items:
            if item == get and len(self.items) > 0:
                self.items.append(get)
                self.room.items.remove(get)
                self.score+=10
            else:
                print ("\nYou already have that item or no item not found\n")
