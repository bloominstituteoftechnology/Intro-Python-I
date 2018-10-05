# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, currentRoom, startingItems=[],score, item):
        self.name = name
        self.currentRoom = currentRoom
        self.item = item
        self.items = startingItems
        self.score = score
        self.strength = 10
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        print(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")
    def look(self, direction=None):
        if direction is None:
            self.currentRoom.printRoomDescription(self)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                nextRoom.printRoomDescription(self)
            else:
                print("There is nothing there.")
    def get_item(self, item):
        #self.inventory.append(item)
        if item.name == 'treasure':
            self.score += 100
        else:
            self.score += 0
    def printStatus(self):
        print(f"Your name is {self.name}, your score is {self.score}")

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
            def get_item(self, item):
        self.inventory.append(item)
        if item.name == 'treasure':
            self.score += 1000
        else:
            self.score += 100

    # def __init__(self, name, currentRoom, inventory):
    #     self.name = name
    #     self.currentRoom = currentRoom
    #     self.items = []
    #     self.inventory = inventory
    # def travel(self, direction):
    #     nextRoom = self.currentRoom.getRoomInDirection(direction)
    #     if nextRoom is not None:
    #         self.currentRoom = nextRoom
    #         print(nextRoom)
    #     else:
    #         print("You cannot move in that direction.")
    # def look(self, direction=None):
    #     if direction is None:
    #         print(self.currentRoom)
    #     else:
    #         nextRoom = self.currentRoom.getRoomInDirection(direction)
    #         if nextRoom is not None:
    #             print(nextRoom)
    #         else:
    #             print("There is nothing there.")
    # def addItem(self, item):
    #     self.inventory.extend(item)
    #
    # def removeItem(self, item):
    #     self.inventory.remove(item)
