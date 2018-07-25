from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     items=Item('knifes', ['Irish knifes',
                                           'turkish knife', 'viking knife'])
                     ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     items=Item('books', ['magic books',
                                          'bible', 'food', 'albums'])
                     ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     items=Item(
                         'boxes ', ['pirates of the carribian', 'old stuff', 'bombs'])
                     ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     items=Item(
                         'cloths ', ['army uniform', 'clone', 'pilot uniform', 'nurse uniform'])
                     ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     items=Item('shields', ['hand shield', 'mask', ' motorcycle halmet'])),
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


newPlayer = Player('john', 'outside')


# Write a loop that:
done = False
while not done:
    print(' ====> game is here...........')

    c = input('please type the cardial direction where u need to Go:')

    if c == "q":
        break

    cardial = ['n', 'e', 'w', 's']
    if c.lower() not in cardial:
        print('there is no such direction...')
        continue

    if c:
        if c.lower() == 'n':
            c = "n_to"

        elif c.lower() == 's':
            c = "s_to"

        elif c.lower() == 'e':
            c = "e_to"

        elif c.lower() == 'w':
            c = "w_to"

    if hasattr(room[newPlayer.room], c) == False:
        print('====> there is no such direction...')
        continue

    nextRoom = getattr(room[newPlayer.room], c)

    if(nextRoom == None):
        print('====> there is no room here ')
        continue

    if(nextRoom != None):
        print('## GREAT JOB ##  you are  in new room ====>:', nextRoom.name)
        print(
            f"....{nextRoom.description}...\nitem ==>:{nextRoom.items.name}\nitemdesc==>:{nextRoom.items.description}")

    print('\n\n==> Ok ok ok since you made it up to here, we want you to pic an item:')
    pick = False
    while not pick:
        i = input('tape the name of your item plz:')

        spl = i.split(' ')
        join = ''.join(spl[1:])
        joinedItems = [i.replace(" ", "") for i in nextRoom.items.description]

        if len(spl) <= 1:
            print('!!! sorry you have to enter the item name as well')
            continue
        if spl[1] == '':
            print('!!!! item name can`t be whitespace')
            continue

        if spl[0] == 'pick':
            if join != None:
                for i in joinedItems:
                    if join == i:
                        getattr(newPlayer, 'items').append(
                            nextRoom.items.description[joinedItems.index(i)])
                        del(nextRoom.items.description[joinedItems.index(i)])
                        pick = True

            else:
                continue

        else:
            print(' !!!! sorry wrong verb....')
            continue

        print('newpaler items are: ==>', getattr(newPlayer, 'items'))
        print('what left in the room is : ==>', nextRoom.items.description)

    ################################################################

    ##################################################################
    while not done:
        print('keep going .....')
        d = input('please type the 2nd  cardial direction where u need to Go:')

        if d == "q":
            break

        bill = ['n', 'e', 'w', 's']
        if d.lower() not in bill:
            print('there is no such direction...')
            continue

        if d:
            if d.lower() == 'n':
                d = "n_to"

            elif d.lower() == 's':
                d = "s_to"

            elif d.lower() == 'e':
                d = "e_to"

            elif d.lower() == 'w':
                d = "w_to"

        if hasattr(nextRoom, d) == False:
            print('=====> there is no such direction...')
            continue

        roomAfter = getattr(nextRoom, d)

        if(roomAfter == None):
            print('====> there is no room here ...')
            continue

        if(roomAfter != None):
            print('## GREAT JOB ##  you are  in new room ====>:', roomAfter.name)
            print(
                f"....{roomAfter.description}...\nitem ==>:{roomAfter.items.name}\nitemdesc==>:{roomAfter.items.description}")

        print('\n\n==> Ok ok ok since you made it up to here, we want you to pic an item:')
        pick = False
        while not pick:
            i = input('tape the name of your item plz:')

            spl = i.split(' ')
            join = ''.join(spl[1:])
            joinedItems = [i.replace(" ", "")
                           for i in roomAfter.items.description]

            if len(spl) <= 1:
                print('!!! sorry you have to enter the item name as well')
                continue
            if spl[1] == '':
                print('!!!! item name can`t be whitespace')
                continue

            if spl[0] == 'pick':
                if join != None:
                    for i in joinedItems:
                        if join == i:
                            getattr(newPlayer, 'items').append(
                                roomAfter.items.description[joinedItems.index(i)])
                            del(roomAfter.items.description[joinedItems.index(
                                i)])
                            pick = True

                else:
                    continue

            else:
                print(' !!!! sorry wrong verb....')
                continue

            print('newpaler items are: ==>', getattr(newPlayer, 'items'))
            print('what left in the room is : ==>',
                  roomAfter.items.description)
            nextRoom = roomAfter

    # break

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
