# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__ (self, name, location, items = []):
        self.name = name
        self.location = location
        self.items = items

    def print_location(self):
        print(f"🤓  Hey { self.name }, you are at 🏠 { self.location.get_room() } now")

    def travel(self, direction):
        self.location = self.location.get_paths(direction) or self.location
        self.print_location()

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            
    def get_item(self):
        print(f"{ self.items }")