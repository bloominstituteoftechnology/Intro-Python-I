from room import Room
from player import Player
import PlayerActions

# Intro
play = True
PlayerActions.player.name = input('Enter Your Name -> ')
print(f"""

~~~~~~~~~~ Welcome {PlayerActions.player.name}! ~~~~~~~~~~

    Starting Point
    ``````````````
    {PlayerActions.room['outside cave entrance'].place}


    Hint
    ````
    {PlayerActions.room['outside cave entrance'].description}

""")

# Play
while play:
    cmd = input('Where Shall You Go? -> ').lower().split(" ")
    if len(cmd) == 1:
        if cmd[0] == 'q':
            break

        # movement
        elif cmd[0] == 'n' or cmd[0] == 's' or cmd[0] == 'e' or cmd[0] == 'w':
            PlayerActions.routeMovement(cmd[0])
            PlayerActions.player.health -= 5

        # looking ahead
        elif cmd[0] == 'ln' or cmd[0] == 'ls' or cmd[0] == 'le' or cmd[0] == 'lw':
            PlayerActions.routeLookAhead(cmd[0])
        
        # item PlayerActions
        elif cmd[0] == 'bag' or cmd[0] == 'status' or cmd[0] == 'look' or cmd[0] == 'get' or cmd[0] == 'drop':
            PlayerActions.routePlayerActions(cmd[0])
        else:
            PlayerActions.brickWall('e')

    # item Actions
    elif len(cmd) > 1:
        if cmd[0] == 'get' or cmd[0] == 'drop':
            if cmd[1] == 'sword' or cmd[1] == 'light' or cmd[1] == 'treasure' or cmd[1] == 'key':
                PlayerActions.routeItemActions(cmd[0], cmd[1])
            else:
                PlayerActions.brickWall('e')
        else:
            PlayerActions.brickWall('e')
    else:
        PlayerActions.brickWall('e')
