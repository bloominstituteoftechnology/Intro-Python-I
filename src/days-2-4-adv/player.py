# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(object):
    def __init__(self, name, location, item, score):
        self.name = name
        self.location = location
        self.item = item
        self.score = 0
        
