from player import Player
from room import Room


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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
#
print()
print("\nWelcome! Are you ready to embark on an adventure?")
name = input(" What is your name?   ")
room = room['outside']
player = Player(name, room)
print()
print(f'Welcome, {player.name}!\n Lets begin the journey!')
print()
print("To play this game, use the buttons n, e, w, and s. \n\n n = North \n e = East \n w = West \n s = South \n q = Quit")
print()
print("The ultimate goal of this game is get to the treasure before anyone else gets to it.")
print("Be careful to not fall to your death!")

# Write a loop that:

while True:
    print(f'Current Room: {player.room.name}...')
    print(player.room.description)
    print()
    cmd = input("Enter the Next Direction --->")

    if cmd == "q":
        break
    elif cmd == "n":
        if hasattr(player.room.n_to, 'name'):
            player.room = player.room.n_to
        else:
            print("You cannot go this way!! Try again")
    elif cmd == "s":
        if hasattr(player.room.s_to, 'name'):
            player.room = player.room.s_to
        else:
            print("You cannot go this way!! Try again")
    elif cmd == "e":
        if hasattr(player.room.e_to, 'name'):
            player.room = player.room.e_to
        else:
            print("You cannot go this way!! Try again")
    elif cmd == "w":
        if hasattr(player.room.w_to, 'name'):
            player.room = player.room.w_to
        else:
            print("You cannot go this way!! Try again")

