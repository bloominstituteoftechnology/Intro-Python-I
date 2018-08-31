# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, startLocation, inventory = []):
        self.inventory = inventory
        self.weapon = None
        self.health = 100
        self.name = name

        self.location = startLocation
        print("\nHello {},".format(self.name),
              "you are: {}".format(self.location))

    def change_location(self, new_location):
        self.location = new_location
        print("\nMoved to: {}".format(self.location))

    def addItem(self, item):
        self.inventory.append(item)
        print("\n{} has been added to inventory".format(item.name))

    def removeItem(self, item):
        self.inventory.remove(item)
        print("\n{} has been removed from inventory\n".format(item.name))

    def listInventory(self):
        for item in self.inventory:
            print(item)
        if not self.inventory:
            print("\nInventory is empty\n")
        

    def getItem(self, name):
        for i in self.inventory:
            if i.name.lower() == name:
                return i
        return None
        
    def eatItem(self, item):
        if item.calories:
            if item.meals > 1:
                inp = int(input("\nHow much would you like to eat?: "))
                if inp <= item.meals and inp > 0:
                    self.health = self.health + (item.calories * inp)
                    item.meals = item.meals - inp
                    print("\nYou have gained {} health\n".format(item.calories * inp))
                else:
                    print("\nMust pick between 1 and {}\n".format(item.meals))
            else:
                self.health = self.health + item.calories
                print("\nYou have gained {} health\n".format(item.calories))
        else:
            print("\nYou can't eat this!\n")
    
    def playerInfo(self):
        print("\nHealth: {}\n".format(self.health))

    def __repr__(self):
        return "Current Location: {}".format(self.location)

    def __str__(self):
        return "Current Location: {}".format(self.location)
