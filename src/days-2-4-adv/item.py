class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def getItem(self):
        return [self.name, self.description]