# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location):
        self.location = location
    
    def to(self, location):
        self.location = location

    def __str__(self):
        return f'{self.location}'