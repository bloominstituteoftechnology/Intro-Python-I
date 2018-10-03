# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location, items):
        self.location = location
        self.items = []
    
    def __str__(self):
        return f'{self.location}'
    
    def view_items(self):
        return f'{self.items}'

    def to(self, location):
        self.location = location
