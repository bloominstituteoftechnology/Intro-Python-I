from room import Room
from player import Player
from item import Item

item = {
    'knife': Item('knife'),
    'coin': Item('coin'),
    'shield': Item('shield')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                "North of you, the cave mount beckons",
                [item['knife'], item['shield']]),

    'foyer':    Room("Foyer",
                """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook",
                """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage",
                """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber",
                """You've found the long-lost treasure chamber! Sadly, it has already been almost completely emptied by earlier adventurers. The only exit is to the south.""",
                [item['coin']]),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

player = Player(room['outside'])

while True:
    print("\nYou are in the %s. %s" % (player.room.name, player.room.description))
    if player.room.items:
        print(f"Inside the room, you see the following items: {', '.join(item.name for item in player.room.items)}")
    inp = input(">>> ").split(" ")
    if inp[0] == "q":
        print("\nYOU HAVE DIED.")
        break
    elif inp[0] == "get" and not player.room.items:
        print("There is nothing for you to take.")
    elif inp[0] == "drop" and not player.items:
        print("You have no items.")
    elif inp[0] == "get":
        player.get(item[inp[1]])
        player.room.remove_item(item[inp[1]])
    elif inp[0] == "drop":
        player.drop(item[inp[1]])
        player.room.add_item(item[inp[1]])
    elif inp[0] == "items":
        if player.items:
            print(f"You have the following items: {', '.join(item.name for item in player.items)}")
        else:
            print("You have no items.")
    elif inp[0] == "n":
        if player.room.n_to:
            player.room = player.room.n_to
        else:
            print("\nThat way is closed to you.")
    elif inp[0] == "s":
        if player.room.s_to:
            player.room = player.room.s_to
        else:
            print("\nThat way is closed to you.")
    elif inp[0] == "e":
        if player.room.e_to:
            player.room = player.room.e_to
        else:
            print("\nThat way is closed to you.")
    elif inp[0] == "w":
        if player.room.w_to:
            player.room = player.room.w_to
        else:
            print("\nThat way is closed to you.")
    else:
        print ("\nI did not recognize that command.")
