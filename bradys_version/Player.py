

class Player:
    def __init__(self, name, currentRoom, startingItems=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.items = startingItems
        self.strength = 10

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            nextRoom.printRoomDescription(player)
        else:
            print("You cannot move in that direction.")

    def look(self, direction=None):
        if direction is None:
            self.currentRoom.printRoomDescription(player)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                nextRoom.printRoomDescription(player)
            else:
                print("There is nothing there.")

    def printStatus(self):
        print(f"Your name is {self.name}, your strength is {self.strength}")

    def printInventory(self):
        print("You are carrying:\n")
        for item in self.items:
            print(f"  {item.name} - {item.description}\n")

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)

    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def hasLight(self):
        return True

    def dropItem(self, itemName):
        itemToDrop = self.findItemByName(" ".join(itemName))
        if itemToDrop is not None:
            self.removeItem(itemToDrop)
            self.currentRoom.addItem(itemToDrop)
            itemToDrop.on_drop()
        else:
            print("You are not holding that item.")
