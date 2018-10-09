from room import Room
from player import Player
from item import Item, Treasure, LightSource

items = {
    'club': Item('Club', 'An old worn stick. Good for bashing things'),
    'ring': Treasure(100, 'Ring', 'A plain looking ring that gives off a mystical glow'),
    'key': Treasure(100, 'Key', 'A golden Key'),
    'ruby': Treasure(500, 'Ruby', 'A large ruby'),
    'lamp': LightSource('Lamp', 'A common lamp. No genies here!')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True, [items['club'], items['key'], items['lamp']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False, [items['ring']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False, [items['ruby']]),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


print('Welcome player!')
name = input('What is your name?  ')
player = Player(name, room['outside'])

while True:
    player.printStatus()
    if player.location.is_light or player.hasLightSource() or player.location.hasLightSource():
        itsDark = False
        player.location.printRoom()
    else:
        itsDark = True
        print("It's pitch black!")
    cmd = input("\nWhat do you want to do? ").lower().split(' ')

    if cmd[0] == 'q':
        break
    elif cmd[0] == 'help':
        print('======================================================')
        print('Press "n, e, w, s" to move North, East, West, or South')
        print('Press "q" to quit')
        print('======================================================')
    elif cmd[0] == 'score':
        print('Score: ', player.score)
    elif cmd[0] == 'n':
        if player.location.n_to == None:
            if player.location.name == 'Grand Overlook':
                print('You\'ve walked off the cliff and fallen to your death!')
                break
            print('Whoops, there\'s a wall there!')
        else:
            player.location = player.location.n_to
    elif cmd[0] == 'e':
        if player.location.e_to == None:
            print('Whoops, there\'s a wall there!')
        else:
            player.location = player.location.e_to
    elif cmd[0] == 'w':
        if player.location.w_to == None:
            print('Whoops, there\'s a wall there!')
        else:
            player.location = player.location.w_to
    elif cmd[0] == 's':
        if player.location.s_to == None:
            print('Whoops, there\'s a wall there!')
        else:
            player.location = player.location.s_to
    elif cmd[0] == 'i' or cmd[0] == 'inventory':
        player.getInv();
    elif cmd[0] == 'get' or cmd[0] == 'take':
        if not player.hasLightSource() and not player.location.is_light and not player.location.hasLightSource():
            print("Good luck finding that in the dark!")
            continue
        elif player.location.contains(items[cmd[1]]):
            player.addItem(items[cmd[1]])
        else:
            print('Can\'t find the item')
    elif cmd[0] == 'drop':
        if items[cmd[1]] in player.inventory:
            player.dropItem(items[cmd[1]])
        else:
            print('You don\'t have this item')
    else:
        print('Not a valid command')
