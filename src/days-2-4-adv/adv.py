from room import Room
from player import Player
import random
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

# Make a new player object that is currently in the 'outside' room.


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

def moving():

    print("Welcome to the treasure finding game!")

    character_name = input("What is your Character name?")
    character_item = input("Choose your starter Item! Stick, Stone, or Leaf")

    player = Player(character_name, "outside", character_item)

    print("You will start outside")
    print("You can move north, west, east, south to discover the mysterious treasure box!")
    print("Goodluck finding the treasure!")
    print("You chose the", player.equipped, " and your name is", player.name)
    randomItem = random.randrange(1, 3)

    while True:
        direction = input("Enter a Cardinal Direction!")

        if direction == "north":
            direction = str(direction)
        elif direction == "east":
            direction = str(direction)
        elif direction == "west":
            direction = str(direction)
        elif direction == "south":
            direction = str(direction)
        else:
            print("Enter only north, west, south, or east!")
        # """ OUTSIDE """
        if player.location == "outside":
            if direction == "north":
                player.location = "foyer"
                print("You are now in the, ", player.location)
            elif direction == "east":
                print("There is no room heading %s, please try another direction"%(direction))
                print("You are still in the, ", player.location)
            elif direction == "south":
                print("There is no room heading %s, please try another direction"%(direction))
                print("You are still in the, ", player.location)
            elif direction == "west":
                print("There is no room heading %s, please try another direction"%(direction))
                print("You are still in the, ", player.location)
        # """ FOYER """
        elif player.location == "foyer":
            if direction == "north":
                player.location = "overlook"
                print("You are now in the, ", player.location) 
            elif direction == "east":
                player.location = "narrow"
                print("You are now in the, ", player.location)
            elif direction == "south":
                player.location = "outside"
                print("You are now ", player.location) 
            elif direction == "west":
                print("You are still in the, ", player.location)
                print("There is no room heading %s, please try another direction"%(direction))
        # """ OVERLOOK """
        elif player.location == "overlook":
            if direction == "north":
                print("You are still in the, ", player.location) 
                print("There is no room heading %s, please try another direction"%(direction))
            elif direction == "east":
                player.location = "treasure"
                print("Congratulations! You've made it to the treasure room!")
                print("The treasure is all yours for the taking!")
                if(randomItem == 1):
                    print("You've opened the treasure chest and found the Telescope of Light!")
                    player.location = "outside"
                    player.equipped = "Telescope of Light"
                    print(player.equipped)
                elif(randomItem == 2):
                    print("You've opened the treasure chest and found the Golden Lantern!")
                    player.location = "outside"
                    player.equipped = "Golden Lantern"
                    print(player.equipped)
                    # break
            elif direction == "south":
                player.location = "foyer"
                print("You are now in the, ", player.location) 
            elif direction == "west":
                print("You are still in the, ", player.location)
                print("There is no room heading %s, please another direction"%(direction))
        # """ NARROW """
        elif player.location == "narrow":
            if direction == "north":
                player.location = "treasure"
                print("Congratulations! You've made it to the treasure room!")
                print("The treasure is all yours for the taking!")
                if(randomItem == 1):
                    print("You've opened the treasure chest and found the Telescope of Light!")
                    player.location = "outside"
                    player.equipped = "Telescope of Light"
                    print(player.equipped)
                elif(randonItem == 2):
                    print("You've opened the treasure chest and found the Golden Lantern!")
                    player.location = "outside"
                    player.equipped = "Golden Lantern"
                    print(player.equipped)
                    # break
            elif direction == "east":
                print("You are still in the, ", player.location)
                print("There is no room heading %s, please try another direction"%(direction))
            elif direction == "south":
                print("You are still in the, ", player.location)
                print("There is no room heading %s, please try another direction"%(direction))
            elif direction == "west":
                player.location = "foyer"
                print ("You are now in the, ", player.location) 
        # """ TREASURE """
        elif player.location == "treasure":
            player.location = "outside"
            print("You are back outside now")

if __name__ == '__main__':
    moving()