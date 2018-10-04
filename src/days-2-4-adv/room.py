from inventory import Inventory

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.points = None
        Inventory.__init__(self, self.name)
    def __str__(self):
        return f'\n{self.name}\n\n   {self.description}'
    def roomItems(self):
        Inventory.getItems(self, self.name)
    def getItem(self, name):
        print(name, "getitem")
        return Inventory.getItem(self, name)
    def showItems(self):
        Inventory.showItems(self, self.name)
    def removeObject(self):
        self.object = 'nothing'
    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "e":
            return self.e_to
        elif direction == "s":
            return self.s_to
        elif direction == "w":
            return self.w_to
        else: 
            return name
    def dropItem(self, oldItem):
        Inventory.dropItem(self, oldItem)
    def addItem(self, item):
        Inventory.addItem(self, item)