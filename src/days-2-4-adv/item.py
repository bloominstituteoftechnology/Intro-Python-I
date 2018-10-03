class Item:
    def __init__(self, item, description):
        self.item = item
        self.description = description

    def __str__(self):
        return self.description
