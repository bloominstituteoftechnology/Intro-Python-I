from player import Player
from room import Room
from item import Item

item = {
    'treasure_chest': Item("TREASURE_CHEST", "The chest is bejeweled and beautiful beyond your wildest dreams."),

    'peasant_sword': Item("PEASANT_SWORD", "It is a dull sword with damage of 1."),

    'pile_of_discarded_food': Item("PILE_OF_DISCARDED_FOOD", "You see it is a pile of delicious rubbish that will grant you 5+ health."),
}  


room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons.", item['treasure_chest']),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['peasant_sword']),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['pile_of_discarded_food']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


p = Player(input("What is your name? "), room['outside'])

validCmds = ['n', 's', 'e', 'w', 'get']

while True:
    print(p)
    print(p.currentRoom)
    cmd = input("\nWhat's your next move, pal? (Actions: n, s, e, w, get [item])\n").lower().split(" ")
    
    if len(cmd) == 1:
        if cmd[0] == 'q':
            break
        elif cmd[0] == 'n':
            print('\n== You stride confidently north. ==')
            try: 
                p.playerMove('n')
            except: 
                print(p.badMove)
        elif cmd[0] == 's':
            print('\n== You stride confidently south. ==')
            try: 
                p.playerMove('s')
            except: 
                print(p.badMove)
        elif cmd[0] == 'e':
            print('\n== You stride confidently east. ==')
            try: 
                p.playerMove('e')
            except: 
                print(p.badMove)
        elif cmd[0] == 'w':
            print('\n== You stride confidently west. ==')
            try: 
                p.playerMove('w')
            except: 
                print(p.badMove)
        else:
            print("\n== You wander aimlessly like a fool and will surely be eaten by goblins if you don't pick a direction soon. ==")
    else:
        if cmd[0] == 'get':
            if cmd[1] == p.currentRoom.items.name.lower():
                p.playerGet(cmd[1])
                p.currentRoom.items = None 
            else:
                print(f"\n== There are no items called {cmd[1]}. You gawk vacantly into the distance like one who has seen far too many dragons in their days. ==")
        else:
            print("\n== Nothing you are saying makes sense. Insanity is looming just beyond another fawlty keystroke. ==")

