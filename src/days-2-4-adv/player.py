# Write a class to hold player information, e.g. what room they are in
# currently.
class Player(Room):
    def __init__(self, location, name, description):
        Room.__init__(self, name, description)
        self.location = location
        
    def printP(self):
        return self.location, self.name, self.description