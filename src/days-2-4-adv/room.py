# Implement a class to hold room information. This should have name and
# description attributes.
from item import itemList
from item import LightSource
from player import Player

class Room:
    def __init__(self, title, description, items, is_Light):
        self.title = title
        self.description = description
        self.items = list(items)
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.is_Light = is_Light

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

    def check_for_light(self, player):
        lighted = False
        for item in player.items:
            if type(item) == LightSource:
                lighted = True
        for item in self.items:
            if type(item) == LightSource:
                lighted = True
        if lighted:
            self.is_Light = True
            return player.location.print_items()
        else:
            self.is_Light = False
            return "\nCan't see, It's pitch black!"

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
                     "North of you, the cave mount beckons",  [itemList['torch'], itemList['shield']], True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [itemList['coin']], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [itemList['telescope']], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [itemList['sword']], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [itemList['diamond'], itemList['coin'], itemList['chest']], False),

    'dungeon': Room("Dungeon Chamber", """You've stumbled into a trap!""", [itemList['hat'], itemList['hat'], itemList['ruby']], False)
}
