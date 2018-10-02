# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def _init_(self, name, startRoom):
        self.name = name
        self.startRoom = startRoom
    def _str_(self):
        return