class Items():
    def __init__(self, parent, items, points=1):
        self.self = self
        self.items = items
        self.parent = parent
        self.points = points
    def getItems(self, name):
        print(f"\n{self.name} currently has:\n")
        for item in self.items:
            print(f"    {item}")
    def addItem(self, newItem):
        self.items.append(newItem)
        Items.getItems(self, self.parent)
        points = self.points
        self.points = 0 
        return points 
    def dropItem(self, oldItem):
        self.items.remove(oldItem)
        Items.getItems(self, self.parent)