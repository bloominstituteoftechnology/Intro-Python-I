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


item = {
    'sword':  Item("sword",
                     "slay the creeps using the sword."),

    'ax':    Item("ax",
                        """crush them with the ax"""),

    'torch': Item("torch",
                        """Find your way!"""),

    'amulet':   Item("amulet",
                         """Stop spells"""),

}

item['outside'].n_to = Item['foyer']
item['foyer'].s_to = Item['outside']
item['narrow'].n_to = Item['overlook']
item['foyer'].e_to = Item['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.






valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

player = Player(input("What is your name? "), room['outside'])

#print(player.currentRoom)

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q":
            break
        elif cmds[0] in valid_directions:
            player.travel(valid_directions[cmds[0]])
        elif cmds[0] == "look":
            player.look()
        else:
            print("I did not understand that cmds.")
    else:

        if cmds[0] == "look":
            if cmds[1] in valid_directions:
                player.look(valid_directions[cmds[1]])
    else:
        if cmds[0] == ('get' or 'take'):
        if cmds[1] not in item:
            print('That item doesn\'t exist.')
        if cmds[1] not in player.location.items:
            print('That item isn\'t in the room.')
        if cmds[1] in player.location.items:
            print('ITS WORKING ')
            player.location.removeItem(f'{cmds[1]}')
            player.addItems([cmds[1]])
    
    if cmds[0] == 'drop':
        if cmds[1] in player.inventory:
            print(player.inventory)
            player.removeItem('rock')
            player.location.addItems([cmds[1]])
        elif cmds[1] in item:
            print('You don\'t have that item in your inventory.')
        elif cmds[1] not in item:
            print('That item doesn\'t exist.')
    
    if cmds[0] == 'i' or 'inventory':
        print('Player Inventory: ', player.inventory)
            print("I did not understand that cmds.")

