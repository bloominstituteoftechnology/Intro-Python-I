# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, is_light, inventory = []):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.inventory = inventory
        # self.is_light = is_light
    def __str__(self):
        return(f'name: {self.name}\n')

    def item_picked_up(self, item):
        self.inventory.remove(item)

    def item_dropped(self, item):
        self.inventory.append(item)

    def check_items(self, item):
        print(f'items include: {self.inventory}')

    def inv(self):
        print(f'{" ".join(item.name for item in self.inventory)}')

    
    
