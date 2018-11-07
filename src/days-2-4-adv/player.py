# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom 
        self.currentRoom = currentRoom
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            print(nextRoom)
        else:
            print("You cannot move that way.")
    def look(self, direction):
        if nextRoom is not None:            
            print(self.currentRoom)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:            
                print(nextRoom)
            else:
                print("There is nothing there.")
    def printInventory(self):
        print("You are carrying:\n")
        for item in self.items:
            print(f"    {item.name}\n")   
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItembyName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None 


        