

class Room():
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        if self.items is None:
            return f'\n== You find yourself in the {self.name}. {self.description} ==\n\n== There are no items in this room. =='
        else:
            return f'\n== You find yourself in the {self.name}. {self.description} ==\n\n== You see a {self.items.name}! {self.items.description} =='



