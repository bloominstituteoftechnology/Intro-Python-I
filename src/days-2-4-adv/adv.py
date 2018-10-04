# namespace for importing classes from other files, similar to importing components in react

from room import Room
from player import Player
from item import Item

# Declare all the rooms

# rooms Dict(Object)
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons. A slain knight holds a Broadsword. \n\n Take Broadsword?\n\n", 'sword'),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. A potion of mana sits atop a nearby shelf. \n\n Take PotionM?\n\n""", 'potionM'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. You notice the glimmer of a lost shield. \n\n Take Shield?\n\n""", 'shield'),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air. A glowing potion of health is noticed nearby. \n\n Take potionH?\n\n""", 'potionH'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The only exit is to the south. Inside stands a lone shimmering gold goblet.\n\n Take goblet?\n\n """, 'goblet'),
}


# Link rooms together

# from outside we can only travel north
# from the foyer we can head south, north, or east
# from the overlook we can only head south
# from the narrow passage we can travel west or north
# from the treasure room we can only travel south
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Declare items

# item Dict(Object)
item = {
    'sword':  Item("Broadsword",
                     "Slay thine enemies with the mighty Broadsword."),

    'shield':    Item("Shield", 
                        """Holdfast to the iron shield and stand guard against enemy attacks."""),

    'potionH': Item("Health Potion", 
                        """Drink it's contents and live to fight another day!"""),

    'potionM':   Item("Mana Potion",
                         """Stay in the fight by quenching your thirst for power!"""),

    'goblet': Item("Goblet of Invulnerability",
                         """As long as this item is equipped death shall be a stranger to you"""),
}

room['outside'].item.append(item['sword'])
room['foyer'].item.append(item['potionM'])
room['overlook'].item.append(item['shield'])
room['narrow'].item.append(item['potionH'])
room['treasure'].item.append(item['goblet'])

#
# Main
#

#valid inputs for directions a player can move in  

valid_directions = {"n": "n", "s": "s", "e": "e", "w": "w",
                    "forward": "n", "backwards": "s", "right": "e", "left": "w"}

# prints each rooms name, description and any items it may hold.

print(room['outside'])
print(room['foyer'])
print(room['overlook'])
print(room['narrow'])
print(room['treasure'])

# Make a new player object that is currently in the 'outside' room.

player = Player(input("What is your name? "), room['outside'])
print(player.currentRoom)

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

while True:
    cmds = input("-> ").lower().split(" ")
    if len(cmds) == 1:
        if cmds[0] == "q": # if command is q
            break # break out of loop
        elif cmds[0] in valid_directions: # if command is n s e or w
            player.travel(valid_directions[cmds[0]])
             # invoke player travel function that moves player in valid direction matching command
        elif cmds[0] == "look": # if command is 'look'
            player.look() # player looks around current room.
        else:
            print("I did not understand that command.") # invalid command prints error message
    else:
        if cmds[0] == "look":
            if cmds[1] in valid_directions: # if player uses command look in a valid direction
                player.look(valid_directions[cmds[1]]) # player looks to nextRoom matching command
        else:
            print("I did not understand that command.") # invalid command prints error message
