# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = {}
        self.health = 100
        self.score = 0
    def take(self, item):
        for key in self.inventory:
            if key == item:
                self.inventory[key] += 1
                return True
        self.inventory[item] = 1
    def drop(self, item):
        for key in self.inventory:
            if key == item:
                if self.inventory[key] > 0:
                  self.inventory[key] -= 1
                  # if inventory is 0, delete
                  if self.inventory[key] == 0:
                    del self.inventory[key]
                  return True
        print("You don't have a {} to drop.\n".format(item))
    def getInventory(self):
        return self.inventory
    def getScore(self):
        return self.score