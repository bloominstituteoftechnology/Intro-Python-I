from room import Room
from player import Player
from items import Item


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
    earlier adventurers. The only exit is to the south... or is it?"""),

    'secret room': Room("Secret Room", """You have found the secret room"""),
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
room['treasure chamber'].n_to = room['secret room']
room['secret room'].s_to = room['treasure chamber']
room['narrow passage'].isDark = True


# Items
items = {
    'sword': Item("Sword"),

    'light': Item("Light"),

    'treasure chest': Item("Treasure Chest"),
    
    'key': Item("Key")
}


# initial items in rooms
room['secret room'].items.append(items['treasure chest'].name)
room['treasure chamber'].items.append(items['light'].name)
room['grand overlook'].items.append(items['sword'].name)
room['narrow passage'].items.append(items['key'].name)


# Make a new player
player = Player(room['outside cave entrance'])


# Player Actions
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

        bag: check your bag
        look: check room
        get: get item
        drop: drop item
        """)


def lookAhead():
    print(f"""

    ~~~~~~~ What Lies Ahead ~~~~~~~ 
    {player.nextRoom.place}

    """)


def checkDarkRooms(location):
    if 'Light' in player.items:
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
    else:
        print(f"""

        ~~~~~~~ Too Dark To See ~~~~~~~ 

        """)


def checkForItems(location):

    if room[location].isDark == True:
        checkDarkRooms(location)

    else:
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


def checkBag():

    if len(player.items) == 0:
        print(f"""

        ~~~~~~~ You Have No Items ~~~~~~~ 

        """)
    elif len(player.items) > 0:
        print(f"""

        ~~~~~~~ Items in Your Bag ~~~~~~~""")
        for item in player.items:
            print(f"""
              {item}
            """)


def getInDarkRooms(location):
    if 'Light' in player.items:
        if len(room[location].items) == 0:
            print(f"""

            ~~~~~~~ {room[location].place} Has No Items ~~~~~~~ 

            """)
        elif len(room[location].items) > 0:
            player.items.extend(room[location].items)
            room[location].items.clear()
            print(f"""

            ~~~~~~~ You Have Aquired ~~~~~~~""")

            for item in player.items:
                print(f"""
                {item}""")

            print(f"""
            ~~~~~~~ From {room[location].place} Room ~~~~~~~
            """)
    else:
        print(f"""

        ~~~~~~~ Too Dark To See ~~~~~~~ 

        """)


def getItems(location):
    if room[location].isDark == True:
       getInDarkRooms(location)
    else:
        if len(room[location].items) == 0:
            print(f"""

            ~~~~~~~ {room[location].place} Has No Items ~~~~~~~ 

            """)
        elif len(room[location].items) > 0:
            player.items.extend(room[location].items)
            room[location].items.clear()
            print(f"""

            ~~~~~~~ You Have Aquired ~~~~~~~""")

            for item in player.items:
                print(f"""
                {item}""")

            print(f"""
            ~~~~~~~ From {room[location].place} Room ~~~~~~~
            """)


def dropItems(location):
    if len(player.items) == 0:
        print(f"""

        ~~~~~~~ You Have No Items ~~~~~~~ 

        """)
    elif len(player.items) > 0:
        room[location].items.extend(player.items)
        player.items.clear()
        print(f"""

        ~~~~~~~ You Have Dropped ~~~~~~~""")

        for item in room[location].items:
            print(f"""
            {item}""")

        print(f"""
        ~~~~~~~ To {room[location].place} Room ~~~~~~~
        """)
