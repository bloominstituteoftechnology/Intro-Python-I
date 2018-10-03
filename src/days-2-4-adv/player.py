# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, currentRoom, inventory):
        self.name = name
        self.currentRoom = currentRoom
        self.inventory = inventory
        self.score = 0
    def increaseScore(self, value):
        self.score += value
    def printInv(self):
        if len(self.inventory) > 0:
            print("You have:")
            for item in self.inventory:
                print(item.name, ":", item.description)
        else:
            print("You do not have any items besides the shirt on your back.")