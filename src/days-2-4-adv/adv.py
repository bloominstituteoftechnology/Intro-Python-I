from room import Room
from player import Player

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["apple"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["key"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

playerOne = Player('Dray', room['outside'])

arr = ['n', 'e', 's', 'w']
while True:
    print('\nIt is ' + playerOne.room.name + '.')
    print(playerOne.room.description)
    inp = input("\nChoose direction: n/s/e/w, enter i to check inventory, c to check room for items,  or q to quit: ").strip().lower()
    
    if (inp == 'q'):
        print('Goodbye!')
        break
    elif (inp in arr):
        if hasattr(playerOne.room, inp+'_to'):
            playerOne.room = getattr(playerOne.room, inp + '_to')
        else:
            print('This path is blocked. Choose another direction')
    elif (inp == 'i'):
        playerOne.check_bag()
    elif (inp == 'c'):
        playerOne.room.check_room()
        if len(playerOne.room.items) is not 0:
            action = input('Take(t), drop(d) or Skip(s): ')
            if (action == 't'):
                playerOne.takeItem(playerOne.room.items)
                playerOne.room.remove_item(playerOne.room.items)
            elif(action == 'd'):
                if len(playerOne.bag) is not 0:
                    playerOne.dropItem()
            elif (action =='s'):
                pass

    else:
        print ("I did not recognize that command")