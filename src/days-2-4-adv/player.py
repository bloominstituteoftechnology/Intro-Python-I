# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []

    def __repr__(self):
        return f"Current Room: {self.currentRoom}"

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(nextRoom)
        else:
            print("You cannot move in that direction.")
    def look(self, direction=None):
        if direction is None:
            print(self.currentRoom)
        else:
            nextRoom - self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print(nextRoom)
            else: 
                print("There is nothing there.")


    # deal with items by player
    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        if len(self.items) > 0:
            for i in self.items:
                if i.name == item:
                    self.items.remove(i)
        else:
            print("That item is not available")