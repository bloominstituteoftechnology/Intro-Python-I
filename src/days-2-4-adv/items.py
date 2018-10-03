class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.get = None
        self.drop = None