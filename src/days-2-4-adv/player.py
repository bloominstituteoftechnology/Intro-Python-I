# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__ (self, name, location, items = []):
        self.name = name
        self.location = location
        self.items = items
        self.treasures = []
        self.lightsources = []
        self.score = 0

    def print_location(self):
        print(f"🤓  Hey { self.name }, you are at 🏠 { self.location.get_room() } now")

    def travel(self, direction):
        self.location = self.location.get_paths(direction) or self.location
        self.print_location()

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            print(f"🔫  You have found a { item.name }")

    def add_treasure(self, treasure):
        self.treasures.append(treasure)
        if treasure.is_picked is False:
            self.score += treasure.value
            treasure.is_picked = True
            print(f"👍  Your score is increased!\n  Score: { self.score }")

    def add_lightsource(self, lightsource):
        self.lightsources.append(lightsource)
        print(f"🔦  You have found a { lightsource.name }!")
            
    def get_item(self):
        print(f"👦🏻  { self.name } has following items: \n")
        for item in self.items:
            print(f"{ item.name }")

    def get_score(self):
        print(f"Score: { self.score }")