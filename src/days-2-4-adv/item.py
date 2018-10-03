#Item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description
    def __str__(self):
        return f"\nItem:\n {self.name}\n  {self.description}\n"
