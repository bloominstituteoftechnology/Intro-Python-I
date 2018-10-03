# Write a class to hold player information, e.g. what room they are in currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = []
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(f"\n\nYou are in: {nextRoom}")
        else:
            print("\n\nYou cannot move in that direction.")
    def look(self, direction=None):
        if direction is None:
            print(f"\n\nYou are in: {self.currentRoom}")
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                print(f"\n\nYou see: {nextRoom}")
            else:
                print("\n\nThere is nothing there.")
    def pickUpItem(self, item):
        self.inventory.append(item)
    def dropItem(self, item):
        self.inventory.remove(item)