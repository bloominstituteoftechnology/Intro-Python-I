# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, items=[]):
        self.location = location
        self.items = items
    
    def __str__(self):
        return f'{self.location}'

    def add_item(self, item):
        return self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
        print (f'\nYou have dropped {item}')
    
    def inventory(self):
        print(f'\nYou have the following items: {self.items}')

    def to(self, location):
        self.location = location
