from room import Room
from player import Player
from item import Item

# Declare all the rooms
 
room = {
    'outside':  Room('Outside Cave Entrance',
                     'North of you, the cave mount beckons', 'outside', [Item('key', 'Looks like it is used to open the cave entrance'), Item('baseball bat', 'for defence purposes?')]),

    'foyer':    Room('Foyer', '''Dim light filters in from the south. Dusty
passages run north and east.''', 'foyer', []),

    'overlook': Room('Grand Overlook', '''A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.''', 'overlook', []),

    'narrow':   Room('Narrow Passage', '''The narrow passage bends here from west
to north. The smell of gold permeates the air.''', 'narrow', []),

    'treasure': Room('Treasure Chamber', '''You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.''', 'treasure', [Item('treasure', 'something shiny')]),
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
class Main:
    def start(self):
# Make a new player object that is currently in the 'outside' room.
        player1 = Player(input('\nProvide your name, hero: '), room['outside'], [Item('toothpick', 'Can be useful'), Item('Pocket rubish', 'No comment')], 0)
        print('\nHello ' + player1.name + '!!!!!!\n')
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters 'q', quit the game.

        move = ''

        while move != 'q':
            player1.getRoom()
            move = input('\n###### CONTROLS ######\nNORTH(n), SOUTH(s), EAST(e) OR WEST(w)\n\n#################### \n####### MENU #######\n|| QUIT(q) the game || INVENTORY(i) || CHECK(c) the room ||\n\nYour next move, ' + player1.name.capitalize() + ' ==>> ')
            
            if move != 'q':
                
                if move == 'i':
                    player1.getScore()
                    player1.check_inventory()
                    dropDecision = input('\n==> DROP(d) item, PASS(p)\n')
                    
                    if dropDecision == 'd':
                        number = input('--> Item number: ')
                        try:
                            int(number)
                        except ValueError:
                            print('There is no item with that number!')
                        
                        else:
                            player1.room.dropped_item(player1.inventory[int(number)])
                            player1.drop_item(int(number))

                        
                elif move == 'c':
                    player1.room.room_items()
                    addDecision = input('\n==> ADD(a) item, PASS(p)')

                    if addDecision == 'a':
                        itemNumber = input('--> Item number: ')
                        try:
                            int(itemNumber)
                        except ValueError:
                            print('There is no item with that number!')
                        if int(itemNumber) <= (len(player1.room.items) - 1):
                            player1.get_item(player1.room.items[int(itemNumber)])
                            player1.room.delete_item(int(itemNumber))
                
                else:
                    keyPress = move + '_to'
                
                    try:
                        #print(getattr(player1.room, keyPress).abr)
                        room[getattr(player1.room, keyPress).abr]
                    except AttributeError:
                        print('\n---> Impossible to go to that direction! Choose different one.\n')
                        player1.getRoom()
                    except KeyError:
                        print('\n---> Impossible to go to that direction! Choose different one.\n')
                        player1.getRoom()
                    else:
                        player1.room = room[getattr(player1.room, keyPress).abr]
                        player1.getRoom()

            else:
                print('\nGame over!')

game1 = Main()
game1.start()