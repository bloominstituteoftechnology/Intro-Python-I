# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_location, items):
        self.current_location = current_location
        self.items = items