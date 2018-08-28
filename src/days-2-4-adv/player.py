# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = {}
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
                  # if inventory is 0, delete the key
                  if self.inventory[key] == 0:
                    del self.inventory[key]
                  return True
        print("Nothing to drop!")
    def getInventory(self):
        return self.inventory