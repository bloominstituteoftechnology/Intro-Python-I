# Implement a class to hold room information. This should have name and
# description attributes.

from item import itemList

class Room:
    def __init__(self, title, description, items):
        self.title = title
        self.description = description
        self.items = list(items)
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def getRoomInDirection(self, direction):
        if direction =="n":
            return self.n_to
        elif direction =="s":
            return self.s_to
        elif direction =="e":
            return self.e_to
        elif direction =="w":
            return self.w_to
        else:
            return 'None'

    def print_items(self):
        if len(self.items) == 0:
            return "No items available"
        elif len(self.items) >= 1:
            item_list = "\n"
            for item in self.items:
                item_list += f"{item.name}\n"            
            return item_list   

    def connectRooms(self, destinationRoom, direction):
        if direction == "n":
            self.n_to = destinationRoom
            destinationRoom.s_to = self
        elif direction == "s":
            self.s_to = destinationRoom
            destinationRoom.n_to = self
        elif direction == "e":
            self.e_to = destinationRoom
            destinationRoom.w_to = self
        elif direction == "w":
            self.w_to = destinationRoom
            destinationRoom.e_to = self
        else:
            print(f"\x1b[1;31;40m\nInvalid Direction\x1b[0m")

roomlist = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",  [itemList['torch'], itemList['shield']] ),             

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [itemList['coin']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [itemList['telescope']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [itemList['sword']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [itemList['coin'], itemList['coin'], itemList['chest']]),

    'dungeon': Room("Dungeon Chamber", """You've stumbled into a trap!""", [itemList['hat'], itemList['hat'], itemList['hat']])
}