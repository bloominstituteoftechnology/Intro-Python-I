
class Player():
    def __init__(self,name):
        self.name = name
        self.currentRoom= ""
    def __str__(self):
        return f"\n{self.currentRoom}\n{priorRoom} - {self.losses} - {self.ties}\n"



class Room():
    def __init__(myRoom,name,description):
        myRoom.name = name
        myRoom.description = description
        myRoom.currentRoom= 0
        myRoom.priorRoom = 0

    def __str__(myRoom):
        return f"\n{myRoom.name}\n{myRoom.currentRoom} - {myRoom.priorRoom}\n"
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



print(room['outside'])
currentRoom = player.room



    print(f'{currentRoom.name}\n{currentRoom.description}')

    command = input('Command> ')

    if command == 'q' or command == 'quit' or command == 'exit':
        done = True

    elif command in ['n', 's', 'e', 'w']:
        directionAttribute = command + '_to'

        if hasattr(currentRoom, directionAttr):
            player.room = getattr(currentRoom, directionAttr)

        else:
            print("Can't go that way.")

    else:
        print('Please try again.')
