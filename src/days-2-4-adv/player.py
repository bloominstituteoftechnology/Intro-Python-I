# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, inventory, score=0):
        self.name = name
        self.location = location
        self.inventory = inventory
        self.score = score

    def __str__(self):
        return self.name

    def get_location(self, location):
        return self.location

    def change_location(self, direction):
        new_location = self.location.next_room(direction)
        if new_location == None:
            print("\nThere is nothing in that direction")
        else:
            self.location = new_location

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)

    def view_inventory(self):
        print(f"{self.name} is currently holding:")
        for item in self.inventory:
            print(f"{item.name.capitalize()}")

    def find_item(self, input_item):
        for item in self.inventory:
            if item.name.lower() == input_item.lower():
                return item
            return None

    def get_score(self):
        print(f"\nCurrent Score: {self.score}")

    def add_to_score(self, points):
        self.score = self.score + points
