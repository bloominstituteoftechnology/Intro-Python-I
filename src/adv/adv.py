# importing room file into adv
from room import Room
# import player file into adv
from player import Player
#import item file into adv
from item import Item
#import treasure subclass
from item import Treasure

# Declare all the rooms
# an object called room holding a location string, and an instance of room
# each one has a value of a room object. imported above.
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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
# setting up possible movements between rooms.
# can use these to create controls. 
# .x_to is a reference to another room. 
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#add items to the rooms
#overlook room, lets append a new item to the contains list

#outside
room['outside'].contains.append(Item("stick", "Stick. a simple tree branch."))
room['outside'].contains.append(Item("matches", "Matches. an old book of matches."))
#foyer
room['foyer'].contains.append(Item("grapes", "Grapes.. need a snack?"))
room['foyer'].contains.append(Item("dagger", "Dagger. letter opener, or stabby thing?"))
room['foyer'].contains.append(Treasure("diamond", "A priceless Diamond. treasure", 1000))
#overlook
room['overlook'].contains.append(Item("pouch", "Pouch. A small leather pouch of silver coins. Good, but we're looking for bigger treasure."))
room['overlook'].contains.append(Item("letter", "Letter. A wax-sealed letter, but not addressed to us."))
room['overlook'].contains.append(Item("book", "Book. A leather book. Seems to be a journal. Maybe the land owners."))
room['overlook'].contains.append(Treasure("ruby", "A priceless Ruby. treasure", 1000))
#narrow
room['narrow'].contains.append(Item("lantern", "Lantern. An oil lantern, has some light left. do I have matches?"))
room['narrow'].contains.append(Item("coin", "Coin. A single coin, its spanish gold, we must be going the right way.."))
room['narrow'].contains.append(Treasure("sapphire", "A priceless Sapphire. treasure", 1000))
#treasure
room['treasure'].contains.append(Item("note", "Note. A small note. It reads: your next adventure is coming soon.."))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# a new instance of the player class. Passed with the params
# playerName = "Falcorn"
#startRoom = room['outside']
main_player = Player("Falcorn", room['outside'])

#start game a line down 
print("\n")
#player name should display at the top. 
print("Your player: " + main_player.name + " defender of the alliance")

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

# setting a flag. We can use this to make stuff work!
done = False

while not done:
    current_room = main_player.room 
    #room is what startRoom is set as. 
    #self.room = startRoom
    print(f'{current_room.name}\n{current_room.description}\n')

    #print room contents
    if len(current_room.contains) > 0:
        print(f'in this area {main_player.name} sees:')
        #iterate through the contents in the current room
        #print them all out
        for i in current_room.contains:
            print("  " + i.description)
        print()

#ask for user input
#this is going to take all the white space off
#and convert the command to lowercase
    command = input("Command> ").strip().lower()

    #second command
    command = command.split(' ')

    #set total score
    total_score = 0

    #check command
    if len(command) == 1:
    
        #set quit command
        if command[0] == 'q' or command[0] == 'quit' or command[0] == 'exit':
            print('Your quest will continue some day. Thanks for playing!')
            done = True
            # these are our movement options
        elif command[0] in ["n", "s", "e", "w"]:
            #sets the _to on each command. 
            dirAttr = command[0] + "_to"

            #check if the current room has the proper _to attached, 
            if hasattr(current_room, dirAttr):
                #if so, set the room to the proper room.
                main_player.room = getattr(current_room, dirAttr)
            else:
                #if it does not, you cant go that way 
                print("you cant go that way")

        elif command[0] == 'score':
            print(f'{main_player.name} has a current score of: {main_player.score}')

        #check inventory
        # is an i or inventory inputted by player?
        elif command[0] in ["i", "inventory"]:
            #if so, do they have anything in inventory?
            if len(main_player.contains) > 0:
                #if so, print it. 
                print(f'{main_player.name} is currently carrying: {main_player.contains}')
            else:
                #if not, remind them.
                print("You're not carrying anything")

        else:
                print("Invalid command. Move with n, s, e, w")

    elif len(command) == 2:
        #desctructuring. Command will take in a verb, and an object
        verb, obj = command
        # user needs to use these verbs
        if verb in ['get', 'take']:
            #te user can choose from a list of what is in the room
            candidates = [item for item in current_room.contains if item.name == obj]
            treasures = [treasure for treasure in current_room.contains if treasure.name == obj]

            #if the room is empty, tell them.
            if len(candidates) == 0:
                print("You dont see that item")

            else:
                print(candidates)
                print(candidates[0].name)
                print(treasures)
                print(treasures[0].name)
                main_player.score += treasures[0].value
                #add the item to the players inventpory, and remove from room. 
                main_player.contains.append(candidates[0])
                current_room.contains.remove(candidates[0])
        #if the user types drop, prepare to check for item, and remove from player
        #then add to the rooms item list. 
        if verb == 'drop':
            candidates = [item for item in main_player.contains if item.name == obj]

            #if they try to drop something they dont have, tell them.
            if len(candidates) == 0:
                print("You're not carrying that item")

            else:
                #remove from the player, add to the room. 
                print(candidates)
                print(candidates[0])
                main_player.contains.remove(candidates[0])
                current_room.contains.append(candidates[0])