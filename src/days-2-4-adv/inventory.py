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
                    print(item)
                    # print(item.name)
                    print(item.itemName)
                    # print(item.points)
                    # help(item)
                    # vars(item)
                    # print(__contains__(item))
                    # print(type(item))
                    # for thing in item:
                    #     print(thing)
                    # print(f"    {item.values}")
    def getItems(self, name):
        return self.items
    def getItem(self, name):
        print(name, "getitem inventory")
        for item in self.items:
            print(item, 'item')
            print(item.itemName, 'item')
            if item.itemName.lower() == name.lower():
                print(item, "maybe this is grassITEM?")
                return item
        return None
    def addItem(self, item):
        print(item)
        self.items.append(item)
        for item in self.items:
            print(item, "add item in inventory")
        # return points 
    def dropItem(self, oldItem):
        self.items.remove(oldItem)
        Inventory.getItems(self, self.parent)
