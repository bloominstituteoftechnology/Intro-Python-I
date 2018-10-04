# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom, startingItems=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = startingItems
        self.power = 0
    # travel method when called takes user to new room
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(nextRoom)
        else:
            print("You cannot move in that direction.")
    # look method
    def look(self, direction=None):
        if direction is None:
            print(self.currentRoom)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print(nextRoom)
            else:
                print("There is nothing there.")
    # prints player inventory
    def printInventory(self):
        print("\nYou are carrying:\n")
        for item in self.items:
            print(f"  ~~ {item.name} ~~\n")
    # adds item to players items
    def addItem(self, item):
        self.items.append(item)
    # removes item to players items
    def removeItem(self, item):
        self.items.remove(item)
    # gets the item in question via user command 
    def getItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None