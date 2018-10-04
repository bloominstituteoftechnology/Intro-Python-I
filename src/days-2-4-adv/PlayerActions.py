from room import Room
from player import Player
from items import Item


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
    'sword': Item("sword"),
    'light': Item("light"),
    'treasure': Item("treasure"),
    'key': Item("key")
}


# initial items in rooms
room['secret room'].items.append(items['treasure'].name)
room['treasure chamber'].items.append(items['light'].name)
room['grand overlook'].items.append(items['sword'].name)
room['narrow passage'].items.append(items['key'].name)


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

    if player.room.place == 'outside cave entrance':
        if action == 'look':
            checkForItems('outside cave entrance')
        elif action == 'get':
            getItems('outside cave entrance')
        elif action == 'drop':
            dropItems('outside cave entrance')

    elif player.room.place == 'foyer':
        if action == 'look':
            checkForItems('foyer')
        elif action == 'get':
            getItems('foyer')
        elif action == 'drop':
            dropItems('foyer')

    elif player.room.place == 'grand overlook':
        if action == 'look':
            checkForItems('grand overlook')
        elif action == 'get':
            getItems('grand overlook')
        elif action == 'drop':
            dropItems('grand overlook')

    elif player.room.place == 'narrow passage':
        if action == 'look':
            checkForItems('narrow passage')
        elif action == 'get':
            getItems('narrow passage')
        elif action == 'drop':
            dropItems('narrow passage')

    elif player.room.place == 'treasure chamber':
        if action == 'look':
            checkForItems('treasure chamber')
        elif action == 'get':
            getItems('treasure chamber')
        elif action == 'drop':
            dropItems('treasure chamber')

    elif player.room.place == 'secret room':
        if action == 'look':
            checkForItems('secret room')
        elif action == 'get':
            getItems('secret room')
        elif action == 'drop':
            dropItems('secret room')


def routeItemActions(action, item):
    if player.room.place == 'outside cave entrance':
        if item == 'sword':
            if action == 'get':
                getSingleItem('outside cave entrance', item)
            elif action == 'drop':
                dropSingleItem('outside cave entrance', item)
        elif item == 'light':
            if action == 'get':
                getSingleItem('outside cave entrance', item)
            elif action == 'drop':
                dropSingleItem('outside cave entrance', item)
        elif item == 'treasure':
            if action == 'get':
                getSingleItem('outside cave entrance', item)
            elif action == 'drop':
                dropSingleItem('outside cave entrance', item)
        elif item == 'key':
            if action == 'get':
                getSingleItem('outside cave entrance', item)
            elif action == 'drop':
                dropSingleItem('outside cave entrance', item)

    elif player.room.place == 'foyer':
        if item == 'sword':
            if action == 'get':
                getSingleItem('foyer', item)
            elif action == 'drop':
                dropSingleItem('foyer', item)
        elif item == 'light':
            if action == 'get':
                getSingleItem('foyer', item)
            elif action == 'drop':
                dropSingleItem('foyer', item)
        elif item == 'treasure':
            if action == 'get':
                getSingleItem('foyer', item)
            elif action == 'drop':
                dropSingleItem('foyer', item)
        elif item == 'key':
            if action == 'get':
                getSingleItem('foyer', item)
            elif action == 'drop':
                dropSingleItem('foyer', item)

    elif player.room.place == 'grand overlook':
        if item == 'sword':
            if action == 'get':
                getSingleItem('grand overlook', item)
            elif action == 'drop':
                dropSingleItem('grand overlook', item)
        elif item == 'light':
            if action == 'get':
                getSingleItem('grand overlook', item)
            elif action == 'drop':
                dropSingleItem('grand overlook', item)
        elif item == 'treasure':
            if action == 'get':
                getSingleItem('grand overlook', item)
            elif action == 'drop':
                dropSingleItem('grand overlook', item)
        elif item == 'key':
            if action == 'get':
                getSingleItem('grand overlook', item)
            elif action == 'drop':
                dropSingleItem('grand overlook', item)

    elif player.room.place == 'narrow passage':
        if item == 'sword':
            if action == 'get':
                getSingleItem('narrow passage', item)
            elif action == 'drop':
                dropSingleItem('narrow passage', item)
        elif item == 'light':
            if action == 'get':
                getSingleItem('narrow passage', item)
            elif action == 'drop':
                dropSingleItem('narrow passage', item)
        elif item == 'treasure':
            if action == 'get':
                getSingleItem('narrow passage', item)
            elif action == 'drop':
                dropSingleItem('narrow passage', item)
        elif item == 'key':
            if action == 'get':
                getSingleItem('narrow passage', item)
            elif action == 'drop':
                dropSingleItem('narrow passage', item)

    elif player.room.place == 'treasure chamber':
        if item == 'sword':
            if action == 'get':
                getSingleItem('treasure chamber', item)
            elif action == 'drop':
                dropSingleItem('treasure chamber', item)
        elif item == 'light':
            if action == 'get':
                getSingleItem('treasure chamber', item)
            elif action == 'drop':
                dropSingleItem('treasure chamber', item)
        elif item == 'treasure':
            if action == 'get':
                getSingleItem('treasure chamber', item)
            elif action == 'drop':
                dropSingleItem('treasure chamber', item)
        elif item == 'key':
            if action == 'get':
                getSingleItem('treasure chamber', item)
            elif action == 'drop':
                dropSingleItem('treasure chamber', item)

    elif player.room.place == 'secret room':
        if item == 'sword':
            if action == 'get':
                getSingleItem('secret room', item)
            elif action == 'drop':
                dropSingleItem('secret room', item)
        elif item == 'light':
            if action == 'get':
                getSingleItem('secret room', item)
            elif action == 'drop':
                dropSingleItem('secret room', item)
        elif item == 'treasure':
            if action == 'get':
                getSingleItem('secret room', item)
            elif action == 'drop':
                dropSingleItem('secret room', item)
        elif item == 'key':
            if action == 'get':
                getSingleItem('secret room', item)
            elif action == 'drop':
                dropSingleItem('secret room', item)


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
        There Is Something Off About This Wall, There seems to be small key hole here
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

        bag: check your bag
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


def gettingItemsInDarkRooms(location):
    if 'light' in player.items:
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
