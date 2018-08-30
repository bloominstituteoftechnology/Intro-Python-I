from room import Room
from player import Player
from item import Item
# Declare all the rooms
items = {
    'scimitar': Item('Scimitar', '+7 Attack'),
    'mace': Item('Mace', '+13 Attack'),
    'tower_shield': Item('Tower Shield', '+8 Block'),
    'heraldic_shield': Item('Heraldic Shield', '+12 Block'),
    'chainmail': Item('Chainmail', '+15 Defense'),
    'gold_plate': Item('Gold Plate', '+25 Defense'),
    'health_potion': Item('Health Potion', 'Heal 10 HP'),
    'mana_potion': Item('Mana Potion', 'Restore 20 Mana'),
    'gold': Item('Gold', 'Currency for other items from vendors'),
    'demon_heart': Item('Demon Heart', 'Bestows owner with great power')
}

room = {
    'outside':  Room("Outside Cave Entrance",
        """North of you, the cave mount beckons""",
     [items['scimitar'], items['health_potion']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[items['tower_shield'], items['chainmail']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[items['mace'], items['mana_potion']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
[items['gold_plate'], items['heraldic_shield']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
[items['gold'], items['demon_heart']]),
}

# Link rooms together

room['outside'].connectRooms(room['foyer'], 'n')
room['foyer'].connectRooms(room['overlook'], 'n')
room['foyer'].connectRooms(room['narrow'], 'e')
room['narrow'].connectRooms(room['treasure'], 'n')


# Main

player = Player(room['outside'])

suppressRoomPrint = False

while True:
    if suppressRoomPrint:
        suppressRoomPrint = False
    else:
        print (player.location)
    print (f'\n{player.location.title}\n {player.location.description}\n {player.location.getItems()}\n')
    inp = input("What is your command: ")

    if inp == "q":
        break
    if inp == "n" or inp == "s" or inp == "w" or inp == "e":
        newRoom = player.location.getRoomInDirection(inp)
        if newRoom == None:
            print('\x1b[1;37;41m + \nImpossible, try again.\n\x1b[0m')
            suppressRoomPrint = True
        else:
            player.change_location(newRoom)