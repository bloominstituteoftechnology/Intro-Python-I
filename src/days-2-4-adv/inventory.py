class Inventory():
    def __init__(self, parent):
        self.self = self
        self.items = []
        self.parent = parent
    def showItems(self, name):#should be display items
        print(f"\n{self.name} currently has:\n")
        if len(self.items) == 0:
            print("    Nothing")
        else: 
            for item in self.items:
                if item == None: 
                    print("    Nothing")
                else: 
                    print(f"    {item.itemName}")
    def getItems(self, name):
        return self.items
    def getItem(self, name):
        for item in self.items:
            if item.itemName.lower() == name.lower():
                return item
        return None
    def addItem(self, item):
        self.items.append(item)
        if hasattr(item, 'itemPoints'): 
            newPoints = item.itemPoints
            return newPoints
        else: 
            return 0
    def removePoints(self, item):
        item.itemPoints = 0
    def dropItem(self, oldItem):
        self.items.remove(oldItem)
        Inventory.showItems(self, self.parent)
