# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, *items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None

    def __str__(self):
        return '{}\n{}'.format(self.name, self.description)

    def getRoomDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

'''
    def connect(self, Room, direction):
        if self.name == "Outside Cave Entrance" and direction == n:
            self.name = "Foyer"
            self.description = """Dim light filters in from the south. Dusty
            passages run north and east."""
            print(self.name)
        elif self.name == "Foyer":
            self.name = "Grand Overlook"
            self.description = """A steep cliff appears before you, falling
            into the darkness. Ahead to the north, a light flickers in
            the distance, but there is no way across the chasm."""
            print(self.name)
        elif self.name == "Narrow Passage":
            self.name = "Treasure Chamber"
            self.description = """You've found the long-lost treasure
            chamber! Sadly, it has already been completely emptied by
            earlier adventurers. The only exit is to the south."""
            print(self.name)
        else:
            print("Thwack! You just hit a brick wall, choose another direction")
'''
