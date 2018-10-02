from room import Room


class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.currentRoom = 'foyer'
    def __str__(self):
        return f'{self.name}\n Health: {self.health} - Mana: {self.mana} - Room: {self.currentRoom}'
    def playerMove(self, direction):
        if direction == 'n':
            self.currentRoom = room[self.currentRoom].n_to
        elif direction == 's': 
            self.currentRoom = self.currentRoom.s_to
        elif direction == 'e': 
            self.currentRoom = self.currentRoom.e_to
        elif direction == 'w': 
            self.currentRoom = self.currentRoom.w_to

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
p = Player(input("What is your name?"))


while True: 
    print(p)
    cmd = input("What's your next move?(n, s, e, w)")
    
    if cmd == 'q':
        break
    elif cmd == 'n':
        print("you are moving north")
        p.playerMove('n')
    else:
        print("You have entered an incorrect command.")











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
