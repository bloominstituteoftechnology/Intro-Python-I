from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'a': Item("AXE", """Glowing axe of a great lost warrior"""),
    'm': Item("MAGIC WAND", """Heavy with power"""),
    'c': Item("CLOAK", """Invisibility"""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main

# Make a new player object that is currently in the 'outside' room.
p = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


print(f"""{p.currentRoom.name}: {p.currentRoom.description}""")


while True:
    cmd = input("which way do you want to go?")
    if cmd.upper() == "Q":  # written this way so input is same case
        print(""" QUIT """)
        break
    if cmd.upper() == "N":
        if hasattr(p.currentRoom.n_to, "name"):
            p.currentRoom = p.currentRoom.n_to
            print(f"""{p.currentRoom.name}: {p.currentRoom.description}""")
        else:
            print("You cant go there")
    elif cmd.upper() == "E":
        if hasattr(p.currentRoom.e_to, "name"):
            p.currentRoom = p.currentRoom.e_to
            print(f"""{p.currentRoom.name}: {p.currentRoom.description}""")
        else:
            print("You cant go there")
    elif cmd.upper() == "S":
        if hasattr(p.currentRoom.s_to, "name"):
            p.currentRoom = p.currentRoom.s_to
            print(f"""{p.currentRoom.name}: {p.currentRoom.description}""")
        else:
            print("You cant go there")
    elif cmd.upper() == "W":
        if hasattr(p.currentRoom.w_to, "name"):
            p.currentRoom = p.currentRoom.w_to
            print(f"""{p.currentRoom.name}: {p.currentRoom.description}""")
        else:
            print("You cant go there")
