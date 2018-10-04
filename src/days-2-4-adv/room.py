# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, is_light=False):
        self.name = name
        self.description = description
        self.items = []
        self.is_light = is_light
    
    def __str__(self):
        return f'{self.name}:\n{self.description}.'
        
    # \n\nItems available in room: {self.items}\n

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
