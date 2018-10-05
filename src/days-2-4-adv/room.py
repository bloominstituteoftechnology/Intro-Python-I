# Implement a class to hold room information. This should have name and
# description attributes.
import random

class Room:
    def __init__ (self, name, description, items = [], treasures = [], lightsources = []):
        self.name = name
        self.description = description
        self.items = items  
        self.treasures = treasures
        self.lightsources = lightsources
        self.is_lighted = len(self.lightsources) == 0
        self.n_to = None 
        self.e_to = None
        self.s_to = None 
        self.w_to = None

    def get_room(self):
        return self.name

    def print_description(self):
        print(f"\n🗒️   { self.description }\n")

    def get_paths(self, direction):
        if direction is "n":
            return self.n_to
        elif direction is "s":
            return self.s_to
        elif direction is "e":
            return self.e_to
        elif direction is "w":
            return self.w_to
        else:
            print("\n⚠️  The direction you have chosen is not accessible!\n")
            return None

    def print_treasures(self):
        for treasure in self.treasures:
            return treasure.name

    def generate_items(self, player):
        if random.random() > 0.5:
            random_item = self.items[random.randint(0, len(self.items) - 1)]
            player.add_item(random_item)