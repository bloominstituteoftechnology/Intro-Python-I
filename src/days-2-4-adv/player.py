# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location=None):
        self.name = name
        self.location = location

    def __str__(self):
        return self.name
        
    def get_location(self.location):
        return self.location
