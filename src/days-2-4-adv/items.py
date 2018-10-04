class Item():
    def __init__(self, name, points):
        self.itemName = name
        self.itemPoints = points
    def __str__(self):
        return self.itemName