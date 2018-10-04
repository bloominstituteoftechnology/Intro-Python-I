from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance","North of you, the cave mount beckons"),

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

# declare items

room['outside'].addItem(Item('sword', 'a sword for slashing'))
room['foyer'].addItem(Item('shield', 'a sheild for protection'))
room['overlook'].addItem(Item('compass', 'a compass to show the direction'))


# Make a new player object that is currently in the 'outside' room.
name = input('Who are you? \n')
me = Player(name ,room['outside'])

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

print (f"""
    {me.startRoom.name}:
    {me.startRoom.description}
    """)
while True:
    cmd = input("which way?-> ")
    if cmd[0] == "q":
        print ("""
    Quitting
        """)
        break
    if cmd[0] is "n" or "s" or "e" or "w":
        me.enter(cmd[0])
    else:
        if cmd[0] == 'get':
            itemToAdd = me.startRoom.selectItem(cmd[1])
            if itemToAdd == None:
                print('Item is not here')
            else:
                me.addItem(itemToAdd)
        elif cmd[0] == 'drop':
            itemToDrop = me.selectItem(cmd[1])
            if itemToDrop is None:
                print('You dont have that item')
            else:
                me.removeItem(itemToDrop)
        else:
             print('Cannot do that...')