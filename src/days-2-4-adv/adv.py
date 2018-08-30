from room import Room
from player import Player
from item import Item
import os


###########
# Initialization
###########

#Declare all items:
items = {}
items['rocks']  = Item('rocks', 'good as weapon and building a fort')
items['gloves']  = Item('gloves', 'good to keep warm, climb and not leave fingerprints')
items['hammer']  = Item('hammer', 'good for building stuff, breaking stuff and of course a weapon')
items['flashlight']  = Item('flashlight', 'light source and a weapon')
items['carabiner']  = Item('carabiner', 'good for climbing and hanging')
items['rope']  = Item('rope', 'good for climbing and hanging and a weapon')
items['snowboard']  = Item('snowboard', 'in case you have to jet')
items['mushies']  = Item('mushies', 'good as weapon and to spread the love')
items['tent']  = Item('tent', 'good for camping, sleeping and sexing')
items['hashies']  = Item('hashies', 'good for a party and to spark it up')
items['mollys']  = Item('mollys', 'good for a party and to spread the love')
items['gold']  = Item('gold', 'can be used to trade')
items['silver']  = Item('silver', 'can be used to trade')
items['titanium']  = Item('titanium', 'can be used to trade')


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['rocks'], items['gloves']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['hammer'] , items['flashlight'] ]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['carabiner'], items['rope'], items['snowboard'] ]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['mushies'], items['mollys'], items['hashies'] , items['tent'] ]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['gold'] , items['silver'] , items['titanium'] ]),
}


# Link rooms together
room['outside'].connectRooms(room['foyer'], 'n')
room['foyer'].connectRooms(room['overlook'], 'n')
room['foyer'].connectRooms(room['narrow'], 'e')
room['narrow'].connectRooms(room['treasure'], 'n')


# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])


# Messages
def printRedMsg(msg):
    print(f"\x1b[1;31;40m {msg} \x1b[0m")

user_prompt_msg = '\x1b[1;32;40m' + "\n\n\nEnter [take/drop] item-name OR a cardinal direction [n,s,e,w] OR q to quit: " + '\x1b[0m'
exit_msg = "\nThank you for playing!"
invalid_command_msg = "I didn't recognize that command, please enter: [take/drop item-name] or [n,s,e,w,q]"
item_nonexist = "Sorry that item doesn't exist"


###########
# Game Loop
###########
while True:
    #Messages during each loop: where they are and what's in the room
    print("\n\n\nYou are currently in the {}".format(player.room.name))
    print("\n{}".format(player.room.description))
    print("\n\nThis room has the following items: ")
    player.room.displayItems()

    #Grab user input and clear screen
    inp = input(user_prompt_msg).split(' ')
    os.system('cls' if os.name == 'nt' else 'clear')

    #If the user enters 1 word
    if len(inp) == 1:

        if inp[0] == "q":
            print(exit_msg)
            break

        elif inp[0] == "n" or inp[0] == "s" or inp[0] == "e" or inp[0] == "w":
            nextRoom = player.room.getRoomInDirection(inp[0])
            if nextRoom ==  None:
                printRedMsg("Sorry that direction does not exist.. please try again")
            else:
                player.set_room(nextRoom)

        elif inp[0] == "i":
            print("\n\nYou have the following items: ")
            player.displayItems()

        else:
            printRedMsg(invalid_command_msg)
    
    #If the user enters 2 words
    elif len(inp) == 2:

        #FIRST check to see if the 2 word input requirement is *NOT* met:
        #   1. Check if the first word of the input is *NOT* (take or drop)  *AND*
        #   2. Check if the second word of the input is *NOT* in the (player.room or player)
        if not ( ( inp[0] == 'take' or inp[0] == 'drop' ) and ( inp[1] in player.room.getItemsList() or inp[1] in player.getItemsList() ) ):
            printRedMsg(invalid_command_msg)
        
        #Now since the two word input requirement is met:
        else:
            if (inp[0] == 'take'):
                if items[inp[1]] in player.room.items:
                    player.room.removeItem(inp[1])
                    player.addItem(items[inp[1]])
                else:
                    printRedMsg(item_nonexist)


            elif (inp[0] == 'drop'):
                if items[inp[1]] in player.items:
                    player.removeItem(inp[1])
                    player.room.addItem(items[inp[1]])
                else:
                    printRedMsg(item_nonexist)
            
            else:
                printRedMsg(invalid_command_msg)
    
    #If the user enters 3 or more words
    else:
        printRedMsg(invalid_command_msg)

