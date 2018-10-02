from room import Room



class Player():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 50
        self.currentRoom = room['outside']
        self.badMove = '==You abruptly realize it is impossible to continue in this direction, turn around, and stride confidently back from whence you came.=='
    def __str__(self):
        return f'\n{self.name}\n Health: {self.health} - Mana: {self.mana} - Room: {self.currentRoom.name}'
    def playerMove(self, direction):
        if direction == 'n':
            self.currentRoom = self.currentRoom.n_to
        elif direction == 's': 
            self.currentRoom = self.currentRoom.s_to
        elif direction == 'e': 
            self.currentRoom = self.currentRoom.e_to
        elif direction == 'w': 
            self.currentRoom = self.currentRoom.w_to
  

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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
    print(p.currentRoom)
    cmd = input("\nWhat's your next move?(n, s, e, w)\n")
    
    if cmd == 'q':
        break
    elif cmd == 'n':
        print('\n==You stride confidently north.==')
        try: 
            p.playerMove('n')
        except: 
            print(p.badMove)
    elif cmd == 's':
        print('\n==You stride confidently south.==')
        try: 
            p.playerMove('s')
        except: 
            print(p.badMove)
    elif cmd == 'e':
        print('\n==You stride confidently east.==')
        try: 
            p.playerMove('e')
        except: 
            print(p.badMove)        
    elif cmd == 'w':
        print('\n==You stride confidently west.==')
        try: 
            p.playerMove('w')
        except: 
            print(p.badMove)        
    else:
        print("\n==You wander aimlessly like a fool and will surely be eaten by goblins if don't pick a direction soon.==")











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
