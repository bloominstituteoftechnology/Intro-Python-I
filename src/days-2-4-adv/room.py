# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = {}

    def __str__(self):
        return(f'name: {self.name}\n')

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
                if self.inventory[key] == 0:
                    del self.inventory[key]
                    return True
        # print("There is no {} here to get!\n".format(item))
