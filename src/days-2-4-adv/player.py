# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, startRoom, score=0, inventory=[]):
        self.name = name
        self.location = startRoom
        self.inventory = inventory
        self.score = score

    def getInventory(self):
        if (len(self.inventory) == 0):
            return None
        else:
            return ([i.name for i in self.inventory])

    def getItem(self, item):
        self.inventory.append(item)
        itemscore = item.on_take()
        self.score += itemscore

    def getScore(self):
        print(f'Your current score is {self.score}')
    
    def dropItem(self, index):
        self.inventory[index].on_drop()
        del self.inventory[index]