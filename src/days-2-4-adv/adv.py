from room import Room
from player import Player
from item import Item

# import textwrap
# Declare all the rooms
# oh my what do we have here...

# okay so up at the top we're importing the room class

# and here we're creating a Python dictionary  
# inside this dictionary each key is just a string
# each value is an instance of Room class, with a name and a description
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
    'secret room': Room('Secret Room', """This is a secret room with a gilded treasure chest 
     inside it. Opon closer examination you find a combination lock in it. """)
}


# Link rooms together
# now this is a little weird perhaps I should stop right here and draw a map 
# of all the rooms. Yeah that should help; visualize the layout of the game map first
# before tackling anything else...

# so those .n_to, .s_to, etc appear to be methods that I haven't defined yet.
# I think I have to define those methods in the room class...
# aha! now I see something new after playing around with super simple on-the-fly classes
# in the console I see that I can add attributes to an instance of a class
# these attributes can be...anything I want! In the case below each of the attributes added are
# other instances of the Room class
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']
room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# add items to rooms
key = Item('key', 'a worn brass key with a dragon head')
torch = Item('torch', 'a simple wooden torch')
note = Item('note', 'combo: 1 - 2 - 3')
secret_door = Item('secret door', 'a locked door with a dragon symbol on it')


room['outside'].items.append(key)
room['outside'].items.append(torch)
room['narrow'].items.append(note)
room['narrow'].items.append(secret_door)
# so after mapping out the rooms I've decided that I don't like this implementation
# There has to be a better way...My intuition tells me there's a better way to implement this
# but I'll go with the way it is for now...
# okay if I think of this game as an app then this would be my top-level file
# this is where the main loop of the game is called...
# Main  
# Make a new player object that is currently in the 'outside' room.
new_player_message = """
****************************************************************************************************
                    Greetings player 1. Welcome to the Super Adventure Game. 
                    Please enter a name for your hero: 
*****************************************************************************************************
>> """
name = input(new_player_message)

player = Player(name, room['outside'])

invalid = """
          *********YOU CAN'T GO IN THAT DIRECTION!***********
          """

# main game loop
while True:
    print("""
               *************************************************************************************
                                   FOR USER ACTIONS, TYPE actions
               *************************************************************************************
          """)
    print("Player: ", player.name)
    print(player.room.name)
    print('\n')
    print(player.room.description)

    message = """
    Which direction do you go? 
    Enter n, w, e, s for North,
    West, East, or South: """

    action = input(message)
    # come back and create parsed action variable to avoid using action.split(' ')[1] all the time
    parsed_action = action.split(' ')
    if action == 'n':
        if player.room.n_to != None:
            player.room = player.room.n_to
        else:
            print(invalid)
    elif action == 'w':
        if player.room.w_to != None:
            player.room = player.room.w_to
        else: 
            print(invalid)
    elif action == 's':
        if player.room.s_to != None:
            player.room = player.room.s_to
        else:
            print(invalid)
    elif action == 'e':
        if player.room.e_to != None:
            player.room = player.room.e_to
        else: 
            print(invalid)
    elif action == 'q':
        print("Goodbye!")
        break
    elif action == 'actions':
        player.display_actions()
    elif action == 'items':
        player.display_items()
    elif action == 'light':
        print("You light your torch! You can now see better!")
    elif 'search' in action:
        if not player.room.searched:
            print(">>>>>>>>>>HERE IS WHAT YOU FIND>>>>>>>>>>")
            player.room.display_items()
            player.room.searched = True
        else:
            print("You already searched this room!")
    elif 'grab' in action:
        if len(parsed_action) > 1:
            if player.room.searched:
                player.grab_item(parsed_action[1])
            else:
                print("You haven't searched this area yet!")
        else:
            print("What are you trying to grab?")
    elif 'drop' in action:
        if len(parsed_action) > 1:
            player.drop_item(parsed_action[1])
        else:
            print("What are you trying to drop?")
    elif 'use' in action:
        if len(parsed_action) > 1:
            if parsed_action[1] == 'key' and player.room.name == 'narrow' and player.room.searched:
                secret_door.unlocked = True
                print("You unlocked the secret door! You can go through it now!")
            elif parsed_action[1] == 'note' and player.room.name == 'secret room':
                 print("Using the combination on the note, you carefully unlock the treasure chest...")
                 print("Inside it is plenty of gold, silver, and gems, more than you can carry...")
                 print("Congratulations! You win!")
            else:
                print("You can't use that item here!")
        else:
            print("What are you trying to use?")
    
    


    # elif action == 'search':
    #     if len(player.room.items) > 0 and not player.room.searched:
    #         print(">>>>>>>>>>HERE IS WHAT YOU FIND>>>>>>>>>>")
    #         player.room.display_items()
    #         player.room.searched = True
    #     else:
    #         print("You have already searched this room.")
    # elif 'grab' in action:
    #     # okay so I don't like this...need to parse multiple values in one string...
    #     if len(player.room.items) > 0 and player.room.searched == True:
    #         if len(parsed_action) > 1:
    #             if parsed_action[1] in player.room.items:
    #                 for i in range(len(player.room.items)):
    #                     if player.room.items[i] == parsed_action[1]:
    #                         player.items.append(player.room.items[i])
    #                         del player.room.items[i]
    #             else:
    #                 print("There is no item named %s in this room!" % parsed_action[1])
    #         else:
    #             print("What are you trying to grab?")
    #     else:
    #         print("You haven't searched enough or there is nothing left to grab!")
    # elif 'drop' in action:
    #     if len(player.items) > 0:
    #         if len(parsed_action) > 1:
    #             if parsed_action[1] in player.items:
    #                 for i in range(len(player.items)):
    #                     if parsed_action[1] == player.items[i]:
    #                         player.room.items.append(player.items[i])
    #                         del player.items[i]
    #                         player.room.searched = False
    #             else:
    #                 print("You have no item named %s in your inventory!" % parsed_action[1])
    #         else:
    #             print("What are you trying to drop?")
    #     else:
    #         print("Player %s has no items to drop!" % player.name)
    # elif 'light' in action:
    #     print("You light your torch! You can now see better!")
    # elif 'use' in action:
    #     if len(player.items) == 0:
    #         print("Player has no items to use!")
    #         continue
    #     if len(parsed_action) > 1:
    #         if parsed_action[1] == 'key' and player.room.name == 'treasure' and room['treasure'].searched:
    #             room['treasure'].secret_door.locked = False
    #             room['treasure'].n_to = room['secret room']
    #         elif parsed_actoin[1] == 'key':
    #             print("You don't see anywhere to use the key in this room...")
    #         else:
    #             print("That item cannot be used here.")
    #     else:
    #         print("What are you trying to use?")
    # else:
    #     print("Invalid input!")
        
    
    

    
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
