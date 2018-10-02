from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, a huge ugly house sits creepily"),

    'spoopy':   Room("Heckin Spoopy Manor", """This place is spoopy as heck. Weird hallways run north and east. 
    But like.. I duno why you would stay"""),

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

room['outside'].n_to = room['spoopy']
room['spoopy'].s_to = room['outside']
room['spoopy'].n_to = room['overlook']
room['spoopy'].e_to = room['narrow']
room['overlook'].s_to = room['spoopy']
room['narrow'].w_to = room['spoopy']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
me = Player(room['outside'])
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
    {me.currentRoom.name}:

    {me.currentRoom.description}
    """)
while True:
    cmd = input("which way?-> ")
    if cmd == "q":
        print ("""
    ~~~~ until tomorrow ~~~~
        """)
        break
    if cmd == "n":
        if hasattr(me.currentRoom.n_to, "name"):
            me.currentRoom = me.currentRoom.n_to
            print (f"""
    {me.currentRoom.name}:

    {me.currentRoom.description}
    """)
        else:
            print ("""
    Yo you cant go that way dog, duh, ya dingus
            """)
    elif cmd == "e":
        if hasattr(me.currentRoom.e_to, "name"):
            me.currentRoom = me.currentRoom.e_to
            print (f"""
    {me.currentRoom.name}:

    {me.currentRoom.description}
    """)
        else:
            print ("""
    Yo you cant go that way dog, duh, ya dingus
            """)
    elif cmd == "s":
        if hasattr(me.currentRoom.s_to, "name"):
            me.currentRoom = me.currentRoom.s_to
            print (f"""
    {me.currentRoom.name}:

    {me.currentRoom.description}
    """)
        else:
            print ("""
    Yo you cant go that way dog, duh, ya dingus
            """)
    elif cmd == "w":
        if hasattr(me.currentRoom.w_to, "name"):
            me.currentRoom = me.currentRoom.w_to
            print (f"""
    {me.currentRoom.name}:

    {me.currentRoom.description}
    """)
        else:
            print ("""
    Yo you cant go that way dog, duh, ya dingus
            """)
