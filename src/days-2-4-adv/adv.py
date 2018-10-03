from player import Player
from room import Room
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ['knife', 'torch', 'helmet']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['steel-sword', 'golden-key', 'barrel-of-beer']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ['ancient-scroll', 'bandages', 'rope']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ['empty-chest', 'clay-jar', 'rock']),
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
items = []
player = Player(name, room, items )
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
    print('As you go along you can pick up items and add them to your inventory!')
    print(f'The items in this room are:{player.room.items}')
    print('Which ones do you want to pick up! You can only choose one per room.')
    cmds = input("What's Next? -->  ").split(' ')

    error = "You cannot go this way!! Try again"
    valid_directions = ["n", "e", "w", "s"]
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(cmds[0]) 
        else:
            print("The command entered does not exist.")
            print()
    if cmds[0] == "look":
        if cmds[1] in valid_directions:
            player.look(cmds[1])
    if cmds[0] == "get":
        player.get_item(cmds[1])