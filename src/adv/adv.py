from room import Room
from player import Player
from items import Item
from items import Treasure
from items import LightSource
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     items=Item('knifes', ['Irish knifes',
                                           'turkish knife', 'viking knife']), treasure=None, light=LightSource('lamp', 'moderate light ', False)
                     ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. """,
                     items=Item('books', ['magic books',
                                          'bible', 'food', 'albums']), treasure=None, light=None
                     ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. #### THERE IS A TREASURE HERE#### """,
                     items=Item(
                         'boxes ', ['pirates of the carribian', 'old stuff', 'bombs']), treasure=Treasure('gold', 'british gold bullion', 90), light=None
                     ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air. #### THERE IS A TREASURE HERE #######""",
                     items=Item(
                         'cloths ', ['army uniform', 'clone', 'pilot uniform', 'nurse uniform']), treasure=Treasure("bronze", "argentina bronze bullion", 35), light=None
                     ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     items=Item('shields', ['hand shield', 'mask', ' motorcycle halmet']), treasure=None, light=LightSource('lamp', 'very strong light', True)),
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


newPlayer = Player('john', 'outside')  # outside = ROOM()


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
        print('\n\n====> there is no such direction...')
        continue

    nextRoom = getattr(room[newPlayer.room], c)

    if(nextRoom == None):
        print('\n\n====> there is no room here ')
        continue

    if(nextRoom != None):
        print('\n\n## GREAT JOB ##  you are  in new room ====>:\n', nextRoom.name)
        print(
            f"....{nextRoom.description}...\n\nroom items==>:{nextRoom.items.description}")
        print('\n\nnewpaler items are: ==>', getattr(newPlayer, 'items'))

        if nextRoom.treasure != None:
            print('\nthis is the treasure name ==>:', nextRoom.treasure)
            print('\nthis is the treasure value ==>:', nextRoom.treasure.value)
            print('\nthis is the treasure description  ==>:',
                  nextRoom.treasure.description)
        else:
            print('\n==> there is no treasure', nextRoom.treasure)

    print('\n\n==> Ok ok ok since you made it up to here, we want you to pic an item:')
    pick = False
    while not pick:
        i = input('type the name of your item plz:')

        spl = i.split(' ')
        join = ''.join(spl[1:])
        joinedItems = [i.replace(" ", "") for i in nextRoom.items.description]

        if len(spl) <= 1:
            if spl[0] == 'i' or spl[0] == 'inventory':
                print('\nnewpaler items are: ==>', getattr(newPlayer, 'items'))
                continue
            if spl[0] == 'score':
                print('newpaler score  is : ==>',
                      getattr(newPlayer, 'score'))
                continue

            else:
                print('\n!!! sorry you have to enter verb and  the item name as well')
                continue

        elif spl[1] == '':
            print('\n!!!! item name can`t be whitespace')
            continue

        elif spl[0] == 'drop':
            dropped = getattr(newPlayer, 'items')[
                getattr(newPlayer, 'items').index(spl[1])]
            print('dropped ==>:', dropped)

            nextRoom.items.description.append(dropped)

            del(getattr(newPlayer, 'items')[
                getattr(newPlayer, 'items').index(spl[1])])

            pick = True

        elif spl[0] == 'pick':
            # if join != None:
            for i in joinedItems:

                if join == i:
                    getattr(newPlayer, 'items').append(
                        nextRoom.items.description[joinedItems.index(i)])
                    del(nextRoom.items.description[joinedItems.index(i)])
                    Item.on_take()
                    pick = True

            if pick == False:
                print('\n=====> !!!sorry there is no such item ')
            # continue
            # else:
            #     continue

        else:
            print('\n !!!! sorry wrong verb....')
            continue

        print('\n\n what left newpaler items are: ==>',
              getattr(newPlayer, 'items'))
        print('\n\nwhat left in the room is : ==>', nextRoom.items.description)

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
            print('\n=====> there is no such direction...')
            continue

        roomAfter = getattr(nextRoom, d)

        if(roomAfter == None):
            print('\n====> there is no room here ...')
            continue

        if(roomAfter != None):
            print('\n\n## GREAT JOB ##  you are  in new room ====>:\n', roomAfter.name)
            print(
                f"....{roomAfter.description}...\n\nitem ==>:{roomAfter.items.name}\nroom items==>:{roomAfter.items.description}")
            print('\n\nnewpaler items are: ==>', getattr(newPlayer, 'items'))

            if roomAfter.treasure != None:
                print('\n## this is the treasure name ==>:',
                      roomAfter.treasure.name)
                print('\n## this is the treasure value  ==>:',
                      roomAfter.treasure.value)
                print('\n## this is the treasure description ==>:',
                      roomAfter.treasure.description)
            else:
                print('\n==> ## there is no treasure here')

        print('\n\n==> Ok ok ok since you made it up to here, we want you to pic an item:')
        pick = False
        while not pick:
            i = input('type the name of your item plz:')

            spl = i.split(' ')
            join = ''.join(spl[1:])
            joinedItems = [i.replace(" ", "")
                           for i in roomAfter.items.description]

            if len(spl) <= 1:
                if spl[0] == 'i' or spl[0] == 'inventory':
                    print('newpaler items are: ==>',
                          getattr(newPlayer, 'items'))
                    continue

                if spl[0] == 'score':
                    print('newpaler score  is: ==>',
                          getattr(newPlayer, 'score'))
                    continue

                else:
                    print(
                        '\n!!! sorry you have to enter verb and  the item name as well')
                    continue

            elif spl[1] == '':
                print('\n!!!! item name can`t be whitespace')
                continue

            elif spl[0] == 'drop':

                dropped2 = getattr(newPlayer, 'items')[
                    getattr(newPlayer, 'items').index(spl[1])]
                print('dropped ==>:', dropped2)

                roomAfter.items.description.append(dropped2)

                del(getattr(newPlayer, 'items')[
                    getattr(newPlayer, 'items').index(spl[1])])
                pick = True

            elif spl[0] == 'pick':
                if join == 'treasure':
                    if roomAfter.treasure.name not in getattr(newPlayer, 'items'):
                        newPlayer.score += roomAfter.treasure.on_take()

                    getattr(newPlayer, 'items').append(
                        getattr(roomAfter.treasure, 'name'))
                    print('i piked the  treasure', roomAfter.treasure.name)

                    if roomAfter.treasure.name in getattr(newPlayer, 'items'):
                        newPlayer.score += roomAfter.treasure.on_take()

                    pick = True
                else:
                    for i in joinedItems:
                        if join == i:
                            getattr(newPlayer, 'items').append(
                                roomAfter.items.description[joinedItems.index(i)])
                            del(roomAfter.items.description[joinedItems.index(
                                i)])
                            pick = True
                            Item.on_take()
                    if pick == False:
                        print('\n=====> !!!sorry there is no such item ')
                    # else:
                    #     continue

            else:
                print('\n !!!! sorry wrong verb....')
                continue

            print('\n what left in newpaler items are: ==>',
                  getattr(newPlayer, 'items'))
            print('\n newpaler score is: ==>',
                  getattr(newPlayer, 'score'))
            print('\nwhat left in the room is : ==>',
                  roomAfter.items.description)
            nextRoom = roomAfter


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
