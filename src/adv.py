# Write a text adventure that allows the player to move from room to room by
# typing "n", "w", "s", or "e" for north, west, south, and east.
import os
# These are the existing rooms. Add more as you see fit.

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.", 
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
    },

}

""" template room to copy into code
    "room": {
        "name": "",
        "description": "",
        "n_to": "",
        "s_to": "",
        "e_to": "",
        "w_to": "",
    },
"""

def clear():
    os.system('cls')
    
title = os.system('title TextAdventure')
# Write a class to hold player information, e.g. what room they are in currently
userInput = input("Please choose a username or quit with q: ")
class Player:
    
    def __init__(self, name, items, rooms, userInput="default"):
        super().__init__()
        self.name = name
        self.items = items
        self.currentRoom = rooms["outside"]

    def __str__(self):
        return f"name: {self.name}, current room: {self.currentRoom} items: {self.items}"
    def move(self):
        goto = userInput + "_to"
        if userInput == "s" or "w" or "e" or "n":
                if goto in self.currentRoom:
                    self.currentRoom = rooms[self.currentRoom[goto]]
                    clear()
                    print(f'{self.currentRoom["name"]} \n {self.currentRoom["description"]}\n\n')
        else:
            print('this is not a valid option')
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(userInput, [], rooms)
while (userInput != "q"):
    userInput = input("Where do you want to go?: ")
    p.move()




# Write a loop that:
#
"""for i in rooms:
    print(f'current room: {i["name"]}')
    print(f'description: {i["description"]}')
    print(f'current room: {i["name"]}')"""
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
