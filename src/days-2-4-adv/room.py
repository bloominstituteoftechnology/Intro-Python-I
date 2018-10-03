# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = []
    
    def __str__(self):
        return f'{self.name}:\n{self.description}.\n\nItems available in room: {self.items}\n'

    def add_item(self, item):
        print(item)
        return self.items.append(item)

    def view_items(self):

        return f'Items available in room: {self.items}'
