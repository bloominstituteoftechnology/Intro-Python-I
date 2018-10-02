from player import Player
  

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
