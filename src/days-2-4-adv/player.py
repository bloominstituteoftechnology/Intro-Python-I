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
            nextRoom.printRoomDescription(player)
        else:
            print("You cannot move in that direction.")

    def look(self,direction = None):
        if direction is None:
            self.currentRoom.printRoomDescription(player)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                nextRoom.printRoomDescription(player)
            else:
                print("There is nothing in that room.")

    def __repr__(self):
        return "Current Location: {}".format(self.currentRoom)

    def printStatus(self):
        print(f"Your name is {self.name}")

    def printInventory(self):
        print("You have collected: \n")
        for item in self.items:
            print(f"  {item.name}: {item.description}\n")

    # deal with items by player

    def findItemByName(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def dropItem(self, itemName):
        itemToDrop = self.findItemByName(" ".join(itemName))
        if itemToDrop is not None:
            self.removeItem(itemToDrop)
            self.currentRoom.addItem(itemToDrop)
            itemToDrop.on_Drop()
        else:
            print("You do not have that item in your possession.")
