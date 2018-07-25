class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def printItem(self):
        return f"{self.name} has {self.description}"


# test = Item("Sword", "500 physical damage and 200 magicka")

# print(test.printItem())