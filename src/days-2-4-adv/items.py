class Items():
    def __init__(self, items):
        self.self = self
        self.items = items
        self.object = "test object"
    def getItems(self, name):
        if len(self.items) > 0:
            print(f'\n{name} items: {self.items}')
        else: 
            return f'The room has no items.'
    def addItem(self, newItem):
        self.items.append(newItem)
    def dropItem(self, oldItem):
        self.items.remove(oldItem)