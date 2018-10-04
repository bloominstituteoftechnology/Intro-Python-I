from room import Room
from player import Player
from item import Item,Treasure,LightSource
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",False),
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
#Declare items
item={
    'sword':Item('sword',"""Just a basic sword to hack at monsters with ... nothing fancy."""),
    'rock':Item('rock',"""A big rock ... not useful at all."""),
    'sandwich':Item('sandwich',"""Sustenance for when you get hungry later."""),
    'lasso':Item('lasso', """Not sure if it makes people tell the truth or makes one go Indiana Jones.""")
}
#put items in rooms
room['outside'].inventory.append(item['sword'])
room['overlook'].inventory.append(item['rock'])
room['narrow'].inventory.append(item['sandwich'])
room['treasure'].inventory.append(item['lasso'])
#Declare treasures
treasure={
    'diamond':Treasure('diamond',"""Diamond's are a girl's best friend""",1000),
    'gold':Treasure('gold',"""A piece of gold that cursed Captain Barbossa's crew""",800),
    'pearl':Treasure('pearl',"""Who would have thought something so valuable could come from something so small.""",900)
}

#put treasures in rooms
room['foyer'].inventory.append(treasure['diamond'])
room['narrow'].inventory.append(treasure['gold'])
room['overlook'].inventory.append(treasure['pearl'])
#
#declare lightsources
lightsource={
    'candle':LightSource('candle',"""Useful for keeping the Boogeyman at bay.""")
}
room['outside'].inventory.append(lightsource['candle'])
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
valid_directions={'n':'n','s':'s','e':'e','w':'w'}
def game():
    player=Player(input('What is your name?\n'),room['outside'])
    print(f'Hello, {player.name}\n{player.current_location}')
    player.is_there_light()
    while True:
        cmd=input('-->').lower().split()
        if len(cmd)==2:
            if cmd[0]=='get':
                print(player.pickup(cmd[1]))
            elif cmd[0]=='drop':
                print(player.drop(cmd[1]))
            else:
                print('Invalid command.')
        elif len(cmd)==1:
            if cmd[0] in valid_directions:
                print(player.travel(valid_directions[cmd[0]]))
            elif cmd[0]=='q':
                break
            elif cmd[0]=='i' or cmd[0]=='inventory':
                print(player.inventory())
            elif cmd[0]=='score':
                print(player.get_score())
            else:
                print('Invalid command.')
        else:
            print('Invalid command')
game()