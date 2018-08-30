class Room:
    def __init__(self, name, description, items=[], adjacent_rooms={}):
        self.name = name
        self.description = description
        self.items = items
        self.adjacent_rooms = adjacent_rooms
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        del self.items[self.items.index(item)]

class Player:
    def __init__(self, room, items=[]):
        self.room = room
        self.items = items
    def get(self, item):
        self.items.append(item)
    def drop(self, item):
        del self.items[self.items.index(item)]

class Item:
    def __init__(self, name):
        self.name = name

item = {
    'knife': Item('knife'),
    'coin': Item('coin'),
    'shield': Item('shield')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons",
                    [item['knife'], item['shield']],
                    {'n': 'foyer', 's': None, 'w': None, 'e': None}),

    'foyer':    Room("Foyer",
                    """Dim light filters in from the south. Dusty passages run north and east.""",
                    [],
                    {'n': 'overlook', 's': 'outside', 'w': None, 'e': 'narrow'}),

    'overlook': Room("Grand Overlook",
                    """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                    [],
                    {'n': None, 's': 'foyer', 'w': None, 'e': None}),

    'narrow':   Room("Narrow Passage",
                    """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                    [],
                    {'n': 'treasure', 's': None, 'w': 'foyer', 'e': None}),

    'treasure': Room("Treasure Chamber",
                    """You've found the long-lost treasure chamber! Sadly, it has already been almost completely emptied by earlier adventurers. The only exit is to the south.""",
                    [item['coin']],
                    {'n': None, 's': 'narrow', 'w': 'foyer', 'e': None})
}

player = Player(room['outside'])

while True:
    print("\nYou are in the %s. %s" % (player.room.name, player.room.description))
    if player.room.items:
        print(f"\nInside the room, you see the following items: {', '.join(item.name for item in player.room.items)}")
    inp = input("\n>>> ").split(" ")
    if len(inp) == 1 or len(inp) == 2 and not inp[1]:
        command, target = inp[0], None
        if command == "q":
            print("\nYOU HAVE DIED.")
            break
        elif command == "items":
            if player.items:
                print(f"\nYou have the following items: {', '.join(item.name for item in player.items)}")
            else:
                print("\nYou have no items.")
        elif command in ['n', 's', 'e', 'w']:
            if player.room.adjacent_rooms[command] == None:
                print("\nYou cannot move that way.")
            else:
                new_room = player.room.adjacent_rooms[command]
                player.room = room[new_room]
        else:
            print ("\nI did not recognize that command.")
    elif len(inp) == 2:
        command, target = inp
        if command == "get" and not player.room.items:
            print("\nThere is nothing for you to take.")
        elif command == "drop" and not player.items:
            print("\nYou have no items.")
        elif command == "get":
            player.get(item[target])
            player.room.remove_item(item[target])
        elif command == "drop":
            player.drop(item[target])
            player.room.add_item(item[target])
        else:
            print ("\nI did not recognize that command.")
    else:
        print ("\nI did not recognize that command.")
