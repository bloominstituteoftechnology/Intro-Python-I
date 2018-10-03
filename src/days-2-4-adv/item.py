#Item class
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"Items in room: {self.name}. Description: {self.description}\n"
