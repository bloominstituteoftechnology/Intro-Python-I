# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
        self.score = 0

    def __repr__(self):
        return f"Current Room: {self.currentRoom}"

    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(f"  \n{self.currentRoom}: {self.currentRoom.description}\n")
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

    def printStatus(self):
        print(f"Your name is {self.name} you are in {self.currentRoom} you have {self.items} your score is {self.score}")

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
        else:
            print("You do not have that item in your possession.")

# scoring ------------
    def tallyScore(self, item):
        points = item.points
        self.score += points
