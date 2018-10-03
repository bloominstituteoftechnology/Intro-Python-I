class Items():
    def __init__(self, items):
        self.self = self
        self.items = items
        self.object = "test object"
    def getItems(self, name):
        if len(self.items) > 0:
            print(f'{name} has {self.items}')
        else: 
            return f'The room has no items.'