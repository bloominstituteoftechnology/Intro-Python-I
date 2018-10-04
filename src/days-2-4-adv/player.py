# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []
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
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print(nextRoom)
            else:
                print("There is nothing there.")
    def takeItem(self, item):
        self.inventory.append(item)
    def dropItem(self, item):
        for i in self.inventory:
            if i.name == item:
                self.inventory.remove(i)
                return i
    def checkInventory(self):
        print("   Inventory:")
        for i in self.inventory:
            print(f"   {i.name}: {i.description}")