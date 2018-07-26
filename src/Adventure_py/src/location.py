class Location(object):
    def __init__(self, name="Null", north=None, south=None, east=None, west=None, description=None, door=None):
        self.name = name
        self.description = description
        self.door = door
        self.items = {}
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def is_valid_room(self, loc):
        return getattr(self, loc) is not None

    def __str__(self):
        return "you are at " + self.name + "\n\t" + self.description + \
               "\n\nitems found in this room: \n\t" + str(self.items)


if __name__ == "__main__":
    print("This is a module for the main adventure_py file. Do not directly run this.")
    input("\n\nPress the enter key to exit.")