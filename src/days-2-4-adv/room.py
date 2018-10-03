from items import Items

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        Items.__init__(self, items=None)
    def __str__(self):
        return f'\n{self.name}\n\n   {self.description}'
    def roomItems(self):
        Items.getItems(self, self.name)
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
        Items.dropItem(self, oldItem)
        Items.getItems(self, self.name)
    def addItem(self, newItem):
        Items.addItem(self, newItem)
        Items.getItems(self, self.name)