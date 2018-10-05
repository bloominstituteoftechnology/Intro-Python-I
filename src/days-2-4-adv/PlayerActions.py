from room import Room
from player import Player
import items


'''
*
********** INIT **********
*
'''
# Declare all the rooms
room = {
    'outside cave entrance': Room("outside cave entrance",
    "North of you, the cave mount beckons"),

    'foyer': Room("foyer", """Dim light filters in from the south.
    Dusty passages run north and east."""),

    'grand overlook': Room("grand overlook", """A steep cliff appears before you,
    falling into the darkness. Ahead to the north,
    a light flickers in the distance,
    but there is no way across the chasm."""),

    'narrow passage': Room("narrow passage", """The narrow passage bends here
    from west to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("treasure chamber", """You've found the long-lost treasure chamber!
    Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south... or is it?"""),

    'secret room': Room("secret room", """You have found the secret room"""),
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
    'sword': items.Weapon("sword", 100, 20),
    'light': items.Tool("light", 50, 'lights up a room'),
    'treasure': items.Asset("treasure", 'preserved', 1000000000000),
    'key': items.Tool("key", 100, 'small key'),
    'apple': items.Food("apple", 1, 20)
}


# initial items in rooms
room['secret room'].items.append(items['treasure'].name)
room['treasure chamber'].items.append(items['light'].name)
room['grand overlook'].items.append(items['sword'].name)
room['narrow passage'].items.append(items['key'].name)
room['foyer'].items.append(items['apple'].name)


# Make a new player
player = Player(room['outside cave entrance'])



'''
*
********** ACTIONS **********
*
'''
# Routes
def routeMovement(direction):
    if direction == 'n':
        if player.room.n_to is not None and player.room.n_to.place == 'secret room':
            shouldEnterSecretRoom()
        else:
            if player.room.n_to is not None:
                updateRoom(player.room.n_to)
                currentLocation()
            else:
                brickWall('m')
    elif direction == 's':
        if player.room.s_to is not None:
            updateRoom(player.room.s_to)
            currentLocation()
        else:
            brickWall('m')
    elif direction == 'e':
        if player.room.e_to is not None:
            updateRoom(player.room.e_to)
            currentLocation()
        else:
            brickWall('m')
    elif direction == 'w':
        if player.room.w_to is not None:
            updateRoom(player.room.w_to)
            currentLocation()
        else:
            brickWall('m')


def routeLookAhead(direction):
    if direction == 'ln':
        if player.room.n_to is not None:
            lookNextRoom(player.room.n_to)
            lookAhead()
        else:
            brickWall('l')
    if direction == 'ls':
        if player.room.s_to is not None:
            lookNextRoom(player.room.s_to)
            lookAhead()
        else:
            brickWall('l')
    if direction == 'le':
        if player.room.e_to is not None:
            lookNextRoom(player.room.e_to)
            lookAhead()
        else:
            brickWall('l')
    if direction == 'lw':
        if player.room.w_to is not None:
            lookNextRoom(player.room.w_to)
            lookAhead()
        else:
            brickWall('l')


def routePlayerActions(action):
    if action == 'bag':
        checkBag()
    
    elif action == 'status':
        checkStatus()
    
    elif action == 'eat':
        eatFood()
    
    elif action == 'look':
        checkForItems(player.room.place)
    
    elif action == 'get':
        getItems(player.room.place)
    
    elif action == 'drop':
        dropItems(player.room.place)


def routeItemActions(action, item):
    if item == 'sword':
        if action == 'get':
            getSingleItem(player.room.place, item)
        elif action == 'drop':
            dropSingleItem(player.room.place, item)
    
    elif item == 'light':
        if action == 'get':
            getSingleItem(player.room.place, item)
        elif action == 'drop':
            dropSingleItem(player.room.place, item)
    
    elif item == 'treasure':
        if action == 'get':
            getSingleItem(player.room.place, item)
        elif action == 'drop':
            dropSingleItem(player.room.place, item)
    
    elif item == 'key':
        if action == 'get':
            getSingleItem(player.room.place, item)
        elif action == 'drop':
            dropSingleItem(player.room.place, item)
    
    elif item == 'apple':
        if action == 'get':
            getSingleItem(player.room.place, item)
        elif action == 'drop':
            dropSingleItem(player.room.place, item)


# Actions
def updateRoom(room):
    player.room = room


def lookNextRoom(room):
    player.nextRoom = room


def shouldEnterSecretRoom():
    if 'key' in player.items:
        updateRoom(player.room.n_to)
        currentLocation()
    else:
        print(f"""

        ~~~~~~~ You Hit A Wall ~~~~~~~
        No Door Ahead

        """)
        print(f"""

        ~~~~~~~ Hint ~~~~~~~
        There Is Something Off About This Wall,
        There seems to be small key hole here

        """)


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

        status: check your status
        bag: check your bag
        eat: eat food from your bag
        look: check room
        get: get all item
        get <item>: get specific item
        drop: drop all item
        drop <item>: drop specific item

        """)


def lookAhead():
    if player.nextRoom.place == 'secret room':
        print(f"""

        ~~~~~~~ There Is Something Off About This Wall ~~~~~~~
        There seems to be small key hole here

        """)
    else:
        print(f"""

        ~~~~~~~ What Lies Ahead ~~~~~~~
        {player.nextRoom.place}

        """)


def checkDarkRooms(location):
    if 'light' in player.items:
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

        ~~~~~~~ Too Dark To Look Around ~~~~~~~

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


def checkStatus():
    print(f"""

    ~~~~~~~ Your Status ~~~~~~~
    name: {player.name}
    health: {player.health}

    """)


def eatFood():
    if 'apple' in player.items:
        player.health += items['apple'].nutrition
        player.items.remove('apple')
        print(f"""
        ~~~~~~~ Tasty and Nutritious Apple ~~~~~~~
        """)
    else:
        print(f"""
        ~~~~~~~ No Food In Bag To Eat ~~~~~~~
        """)


def gettingItemsInDarkRooms(location):
    if 'light' in player.items:
        if len(room[location].items) == 0:
            print(f"""

            ~~~~~~~ {room[location].place} Has No Items ~~~~~~~

            """)
        elif len(room[location].items) > 0:
            print(f"""

            ~~~~~~~ You Have Aquired ~~~~~~~""")
            for item in room[location].items:
                print(f"""
                  {item}""")
            print(f"""
            ~~~~~~~ From {room[location].place} Room ~~~~~~~

            """)
            player.items.extend(room[location].items)
            room[location].items.clear()
    else:
        print(f"""

        ~~~~~~~ Too Dark To Look Around, Can't Find Items ~~~~~~~

        """)


def getItems(location):
    if room[location].isDark == True:
       gettingItemsInDarkRooms(location)
    else:
        if len(room[location].items) == 0:
            print(f"""

            ~~~~~~~ {room[location].place} Has No Items ~~~~~~~

            """)
        elif len(room[location].items) > 0:
            print(f"""

            ~~~~~~~ You Have Aquired ~~~~~~~""")
            for item in room[location].items:
                print(f"""
                  {item}""")
            print(f"""
            ~~~~~~~ From {room[location].place} Room ~~~~~~~

            """)
            player.items.extend(room[location].items)
            room[location].items.clear()


def gettingSingleItemInDarkRooms(location, item):
    if 'light' in player.items:
        if len(room[location].items) == 0:
            print(f"""

            ~~~~~~~ {room[location].place} Has No Items ~~~~~~~

            """)
        elif len(room[location].items) > 0:
            player.items.append(item)
            room[location].items.remove(item)
            print(f"""

            ~~~~~~~ You Have Aquired ~~~~~~~""")
            print(f"""
              {item}""")
            print(f"""
            ~~~~~~~ From {room[location].place} Room ~~~~~~~

            """)
    else:
        print(f"""

        ~~~~~~~ Too Dark To Look Around, Can't Find Items ~~~~~~~

        """)


def getSingleItem(location, item):
    if room[location].isDark == True:
       gettingSingleItemInDarkRooms(location, item)
    else:
        if len(room[location].items) == 0:
            print(f"""

            ~~~~~~~ {room[location].place} Has No Items ~~~~~~~

            """)
        elif len(room[location].items) > 0:
            player.items.append(item)
            room[location].items.remove(item)
            print(f"""

            ~~~~~~~ You Have Aquired ~~~~~~~""")
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
        print(f"""

        ~~~~~~~ You Have Dropped ~~~~~~~""")
        for item in player.items:
            print(f"""
              {item}""")
        print(f"""
        ~~~~~~~ To {room[location].place} Room ~~~~~~~

        """)
        room[location].items.extend(player.items)
        player.items.clear()


def dropSingleItem(location, item):
    if len(player.items) == 0:
        print(f"""

        ~~~~~~~ You Have No Items ~~~~~~~

        """)
    elif len(player.items) > 0:
        room[location].items.append(item)
        player.items.remove(item)
        print(f"""

        ~~~~~~~ You Have Dropped ~~~~~~~""")
        print(f"""
          {item}""")
        print(f"""
        ~~~~~~~ To {room[location].place} Room ~~~~~~~

        """)
