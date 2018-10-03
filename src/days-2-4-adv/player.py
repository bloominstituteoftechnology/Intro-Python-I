# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__ (self, name, location):
        self.name = name
        self.location = location

    def print_location(self):
        print(f"🤓  Hey {self.name}, you are at 🏠 { self.location.get_room() } now")

    def travel(self, direction):
        self.location = self.location.get_paths(direction) or self.location
        self.print_location()