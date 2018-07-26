from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'beginning':  Room("area before the Lambda Entrance",
                       "Before you, presented in majesty, lies the Computer Science Academy of Lambda School. Regardless of your reason, you have sought it out and now it presents you with unimaginable opportunities. Head north to fulfill your destiny."),

    'entrance':    Room("beginning of Lambda School", """The entrance is neither luxurious nor exactly plain. Everything is merely functional, either it works or it doesn't, with no flair of extravagance in sight. Speaking of functions, you adjust your glasses as programmatical statements begin to swarm around you, coalescing into the form of a human man. The figure strikes an almost familiar smile as he proffers his hand. Motioning, he seems to want you to follow him north, deeper into the academy. 'If you wish to gain more knowledge and power, follow me. Otherwise, this is your one and only chance to leave this place and perhaps return another day. However, continuing now will force you to follow this path no matter where it leads.' He stops, affording you time to decide. Go north, or return south?"""),

    'JavaScript': Room("Grand JavaScript", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. Cursing into the vast empty darkness, you hear a robotic voice echo nearby "I am PatrickBot, my love you." Your confusion grows unabatedly as another voice responds, "So, you finally made it." Your eyes attempt to scan the darkness but to no avail. "Up here." The voice was now above you. Glancing up you see a speaker with a single light. """),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['beginning'].n_to = room['entrance']
room['entrance'].s_to = room['beginning']
room['entrance'].n_to = room['JavaScript']
room['entrance'].e_to = room['narrow']
room['JavaScript'].s_to = room['entrance']
room['narrow'].w_to = room['entrance']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_1 = Player("Leon", room['beginning'])

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
choice = None

while choice != 'q':
    currentRoom = player_1.currentRoom
    prettyDesc = textwrap.fill(player_1.currentRoom.description)

    print(player_1)
    print(prettyDesc)
    for item in player_1.currentRoom.items:
        print("You see a {}").format(item)

    choice = input("Choose direction('n', 'e', 'w', 's'):")

    directions = {
        "n": player_1.currentRoom.n_to,
        "e": player_1.currentRoom.e_to,
        "s": player_1.currentRoom.s_to,
        "w": player_1.currentRoom.w_to
    }

    next_room = directions.get(choice, None)

    if next_room:
        player_1.currentRoom = next_room
    else:
        if choice in ['n', 'e', 's', 'w']:
            print("You cannot go that way")
        elif choice is "q":
            print("Goodbye")
        else:
            "You must enter a direction or 'q' to quit"
