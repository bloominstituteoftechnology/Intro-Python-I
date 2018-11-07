from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

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
def main():
    new_player_name = input('Please enter your name: ')


# Make a new player object that is currently in the 'outside' room.
    new_player = Player(new_player_name, room['outside'])


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

    while True:
        # display current room info
        print(f"You are in the {new_player.room.name}")
        print(textwrap.wrap(new_player.room.description))

        # promp for next move
        print("What do you want to do next?")
        print("('n': go north")
        print("('s': go south")
        print("('e': go east")
        print("('w': go west")
        print("('q': quit game")
        next_move = input("")

        # type check next_move input
        try:
            next_move = str(next_move) 
        except ValueError:
            print("Please enter an appropriate letter.")
        
        if len(next_move) == 1:

            #handle quit
            if next_move == 'q':
                print("Thank you for playing.  Goodbye!")
                break

            elif next_move == 'n':
                if hasattr(new_player.room, 'n_to'):
                    new_player.room = new_player.room.n_to
                    if new_player.room.name == 'Treasure Chamber':
                        print("You won!!")
                        break
                else:
                    print("This move is not allowed.  Please try again.")
            
            elif next_move == 's':
                if hasattr(new_player.room, 's_to'):
                    new_player.room = new_player.room.s_to
                    if new_player.room.name == 'Treasure Chamber':
                        print("You won!!")
                        break
                else:
                    print("This move is not allowed.  Please try again.")
            elif next_move == 'e':
                if hasattr(new_player.room, 'e_to'):
                    new_player.room = new_player.room.e_to
                    if new_player.room.name == 'Treasure Chamber':
                        print("You won!!")
                        break
                else:
                    print("This move is not allowed.  Please try again.")
            elif next_move == 'w':
                if hasattr(new_player.room, 'w_to'):
                    new_player.room = new_player.room.w_to
                    if new_player.room.name == 'Treasure Chamber':
                        print("You won!!")
                        break
                else:
                    print("This move is not allowed.  Please try again.")
            
            # elif        or next_move == 's' or next_move == 'e' or next_move == 'w':
                # print('here')
                # break

                # move_str = next_move + '_to'
                # if hasattr(new_player.room, move_str):
                #     new_player.room = new_player.room[move_str]
        else:
            print("Please enter an appropriate letter.")

main()