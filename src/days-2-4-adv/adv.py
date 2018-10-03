from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside cave entrance': Room("Outside Cave Entrance",
    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south.
    Dusty passages run north and east."""),

    'grand overlook': Room("Grand Overlook", """A steep cliff appears before you,
    falling into the darkness. Ahead to the north,
    a light flickers in the distance,
    but there is no way across the chasm."""),

    'narrow passage': Room("Narrow Passage", """The narrow passage bends here
    from west to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("Treasure Chamber", """You've found the long-lost treasure chamber!
    Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside cave entrance'].n_to = room['foyer']
room['foyer'].s_to = room['outside cave entrance']
room['foyer'].n_to = room['grand overlook']
room['foyer'].e_to = room['narrow passage']
room['grand overlook'].s_to = room['foyer']
room['narrow passage'].w_to = room['foyer']
room['narrow passage'].n_to = room['treasure chamber']
room['treasure chamber'].s_to = room['narrow passage']

# print('check attribute', room['outside cave entrance'].n_to.place)

#
# Main
#

# Make a new player object that is currently in the 'outside cave entrance' room.
player = Player(room['outside cave entrance'])
play = True
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


def currentLocation():
    print(f"""
    ~~~~~~~ You Have Entered ~~~~~~~ 
    {player.room.place}
    """)

    print(f"""
    ~~~~~~~ Hint ~~~~~~~ 
    {player.room.description}

    """)


def brickWall(type):

    if type == 'm':
        print(f"""

        ~~~~~~~ You Hit A Wall ~~~~~~~ 
        Nowhere To Go, Try Another Direction

        """)
    elif type == 'l':
        print(f"""

        ~~~~~~~ Nothing Ahead ~~~~~~~ 
        Nothing Ahead, Try Another Direction

        """)
    elif type == 'e':
        print(f"""

        ~~~~~~~ Not Allowed ~~~~~~~ 
        Action Not Allowed

        Allowed Actions:
        n: move north      ln: look north
        s: move south      ls: look south
        e: move east       le: look east
        w: move west       lw: look west

        look: check room
        get: get item
        drop: drop item
        """)


def lookAhead():
    print(f"""

    ~~~~~~~ What Lies Ahead ~~~~~~~ 
    {player.nextRoom}

    """)


def checkForItems(location):

    if len(room[location].items) == 0:
        print(f"""

        ~~~~~~~ {room[location].place} Has No Items ~~~~~~~ 

        """)
    elif len(room[location].items) > 0:
        print(f"""

        ~~~~~~~ Items in {room[location].place} ~~~~~~~""")
        for item in room[location].items:
            print(f"""
                {item}
            """)


while play:

    cmd = input('Where Shall You Go? -> ').lower().split(" ")

    if len(cmd) == 1:
        if cmd[0] == 'q':
            break
        # movement
        elif cmd[0] == 'n':
            if player.room.n_to is not None:
                player.updateRoom(player.room.n_to)
                currentLocation()
            else:
                brickWall('m')
        elif cmd[0] == 's':
            if player.room.s_to is not None:
                player.updateRoom(player.room.s_to)
                currentLocation()
            else:
                brickWall('m')
        elif cmd[0] == 'e':
            if player.room.e_to is not None:
                player.updateRoom(player.room.e_to)
                currentLocation()
            else:
                brickWall('m')
        elif cmd[0] == 'w':
            if player.room.w_to is not None:
                player.updateRoom(player.room.w_to)
                currentLocation()
            else:
                brickWall('m')
        # looking ahead
        elif cmd[0] == "ln":
            if player.room.n_to is not None:
                player.lookNextRoom(player.room.n_to)
                lookAhead()
            else:
                brickWall('l')
        elif cmd[0] == "ls":
            if player.room.s_to is not None:
                player.lookNextRoom(player.room.s_to)
                lookAhead()
            else:
                brickWall('l')
        elif cmd[0] == "le":
            if player.room.e_to is not None:
                player.lookNextRoom(player.room.e_to)
                lookAhead()
            else:
                brickWall('l')
        elif cmd[0] == "lw":
            if player.room.w_to is not None:
                player.lookNextRoom(player.room.w_to)
                lookAhead()
            else:
                brickWall('l')
        # items
        elif cmd[0] == "look":
            if player.room.place.lower() == 'outside cave entrance':
                checkForItems('outside cave entrance')

            elif player.room.place.lower() == 'foyer':
                checkForItems('foyer')

            elif player.room.place.lower() == 'grand overlook':
                checkForItems('grand overlook')

            elif player.room.place.lower() == 'narrow passage':
                checkForItems('narrow passage')

            elif player.room.place.lower() == 'treasure chamber':
                checkForItems('treasure chamber')

        elif cmd[0] == "get":
            #do something
            print("do")
        elif cmd[0] == "drop":
            #do something
            print("do")
        else:
            brickWall('e')
