class Items():
    def __init__(self, whosItems, items):
        self.self = self
        self.items = items
        self.parent = whosItems
    def getItems(self, name):
        if len(self.items) > 0:
            print(f'\n{name} items: {self.items}')
        else: 
            return f'The room has no items.'
    def addItem(self, newItem):
        self.items.append(newItem)
        Items.getItems(self, self.parent)
    def dropItem(self, oldItem):
        self.items.remove(oldItem)
        Items.getItems(self, self.parent)