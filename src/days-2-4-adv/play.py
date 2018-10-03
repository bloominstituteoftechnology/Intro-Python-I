from room import Room
from player import Player
import PlayerActions


play = True

while play:

    cmd = input('Where Shall You Go? -> ').lower().split(" ")

    if len(cmd) == 1:
        if cmd[0] == 'q':
            break

        # movement
        elif cmd[0] == 'n':
            if PlayerActions.player.room.n_to is not None:
                PlayerActions.player.updateRoom(PlayerActions.player.room.n_to)
                PlayerActions.currentLocation()
            else:
                PlayerActions.brickWall('m')
        elif cmd[0] == 's':
            if PlayerActions.player.room.s_to is not None:
                PlayerActions.player.updateRoom(PlayerActions.player.room.s_to)
                PlayerActions.currentLocation()
            else:
                PlayerActions.brickWall('m')
        elif cmd[0] == 'e':
            if PlayerActions.player.room.e_to is not None:
                PlayerActions.player.updateRoom(PlayerActions.player.room.e_to)
                PlayerActions.currentLocation()
            else:
                PlayerActions.brickWall('m')
        elif cmd[0] == 'w':
            if PlayerActions.player.room.w_to is not None:
                PlayerActions.player.updateRoom(PlayerActions.player.room.w_to)
                PlayerActions.currentLocation()
            else:
                PlayerActions.brickWall('m')

        # looking ahead
        elif cmd[0] == "ln":
            if PlayerActions.player.room.n_to is not None:
                PlayerActions.player.lookNextRoom(PlayerActions.player.room.n_to)
                PlayerActions.lookAhead()
            else:
                PlayerActions.brickWall('l')
        elif cmd[0] == "ls":
            if PlayerActions.player.room.s_to is not None:
                PlayerActions.player.lookNextRoom(PlayerActions.player.room.s_to)
                PlayerActions.lookAhead()
            else:
                PlayerActions.brickWall('l')
        elif cmd[0] == "le":
            if PlayerActions.player.room.e_to is not None:
                PlayerActions.player.lookNextRoom(PlayerActions.player.room.e_to)
                PlayerActions.lookAhead()
            else:
                PlayerActions.brickWall('l')
        elif cmd[0] == "lw":
            if PlayerActions.player.room.w_to is not None:
                PlayerActions.player.lookNextRoom(PlayerActions.player.room.w_to)
                PlayerActions.lookAhead()
            else:
                PlayerActions.brickWall('l')

        # item PlayerActions
        elif cmd[0] == "bag":
            PlayerActions.checkBag()
        elif cmd[0] == "look":
            if PlayerActions.player.room.place.lower() == 'outside cave entrance':
                PlayerActions.checkForItems('outside cave entrance')

            elif PlayerActions.player.room.place.lower() == 'foyer':
                PlayerActions.checkForItems('foyer')

            elif PlayerActions.player.room.place.lower() == 'grand overlook':
                PlayerActions.checkForItems('grand overlook')

            elif PlayerActions.player.room.place.lower() == 'narrow passage':
                PlayerActions.checkForItems('narrow passage')

            elif PlayerActions.player.room.place.lower() == 'treasure chamber':
                PlayerActions.checkForItems('treasure chamber')

            elif PlayerActions.player.room.place.lower() == 'secret room':
                PlayerActions.checkForItems('secret room')
        elif cmd[0] == "get":
            if PlayerActions.player.room.place.lower() == 'outside cave entrance':
                PlayerActions.getItems('outside cave entrance')

            elif PlayerActions.player.room.place.lower() == 'foyer':
                PlayerActions.getItems('foyer')

            elif PlayerActions.player.room.place.lower() == 'grand overlook':
                PlayerActions.getItems('grand overlook')

            elif PlayerActions.player.room.place.lower() == 'narrow passage':
                PlayerActions.getItems('narrow passage')

            elif PlayerActions.player.room.place.lower() == 'treasure chamber':
                PlayerActions.getItems('treasure chamber')

            elif PlayerActions.player.room.place.lower() == 'secret room':
                PlayerActions.getItems('secret room')
        elif cmd[0] == "drop":
            if PlayerActions.player.room.place.lower() == 'outside cave entrance':
                PlayerActions.dropItems('outside cave entrance')

            elif PlayerActions.player.room.place.lower() == 'foyer':
                PlayerActions.dropItems('foyer')

            elif PlayerActions.player.room.place.lower() == 'grand overlook':
                PlayerActions.dropItems('grand overlook')

            elif PlayerActions.player.room.place.lower() == 'narrow passage':
                PlayerActions.dropItems('narrow passage')

            elif PlayerActions.player.room.place.lower() == 'treasure chamber':
                PlayerActions.dropItems('treasure chamber')

            elif PlayerActions.player.room.place.lower() == 'secret room':
                PlayerActions.dropItems('secret room')
        else:
            PlayerActions.brickWall('e')
