class Item:
    def __init__(self, name, description):
        self.name = str(name)
        self.description = str(description)
    def __str__(self):
        return self.name